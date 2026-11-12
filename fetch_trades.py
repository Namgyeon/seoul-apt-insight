import os
import xml.etree.ElementTree as ET
from datetime import date

import httpx
from dotenv import load_dotenv

load_dotenv()  # .env 파일을 읽어서 os.environ에 넣는다 (Vite의 import.meta.env 같은 것)

API_URL = (
    "https://apis.data.go.kr/1613000/RTMSDataSvcAptTradeDev/getRTMSDataSvcAptTradeDev"
)
API_KEY = os.environ["DATA_GO_KR_KEY"]  # 없으면 KeyError로 바로 죽는다. 의도한 것.


def fetch_month(lawd_cd: str, deal_ymd: str) -> list[dict]:
    """구 코드(lawd_cd)와 년월(deal_ymd, 'YYYYMM') 하나에 대한 거래 전부를 가져온다."""
    params = {
        "serviceKey": API_KEY,  # httpx가 URL 인코딩을 알아서 해준다
        "LAWD_CD": lawd_cd,
        "DEAL_YMD": deal_ymd,
        "pageNo": 1,
        "numOfRows": 1000,  # 한 구의 한 달 거래는 보통 1000건 미만
    }
    resp = httpx.get(API_URL, params=params, timeout=30)
    resp.raise_for_status()  # 4xx/5xx면 여기서 예외

    root = ET.fromstring(resp.text)
    result_code = root.findtext("header/resultCode")
    if result_code != "000":
        if result_code == "03":
            return []
        raise RuntimeError(f"API 오류: {root.findtext('header/resultMsg')}")

    trades = [parse_item(item) for item in root.iter("item")]

    # 한 페이지(1000건)에 다 안 담긴 경우: 조용히 잘리지 않게 바로 알린다
    total = int(root.findtext("body/totalCount") or 0)
    if total > len(trades):
        raise RuntimeError(f"{lawd_cd} {deal_ymd}: 전체 {total}건 중 {len(trades)}건만 받음. 페이지 순회 필요")

    return trades


def parse_item(item: ET.Element) -> dict:
    """XML <item> 하나를 우리 컬럼 이름의 dict로 바꾼다."""
    text = lambda tag: (item.findtext(tag) or "").strip()

    return {
        "lawd_cd": text("sggCd"),  # 구 코드. 여러 구를 한 테이블에 넣을 때 구분용
        "apt_seq": text("aptSeq"),
        "apt_name": text("aptNm"),
        "dong": text("umdNm"),
        "price": int(text("dealAmount").replace(",", "")),  # "260,000" → 260000 (만원)
        "area": float(text("excluUseAr")),
        "floor": int(text("floor")),
        "build_year": int(text("buildYear")),
        "deal_date": date(
            int(text("dealYear")), int(text("dealMonth")), int(text("dealDay"))
        ),
    }


if __name__ == "__main__":
    trades = fetch_month("11440", "202510")  # 마포구, 2025년 10월
    print(f"{len(trades)}건")
    for t in trades[:3]:
        print(t)
