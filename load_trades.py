import sys
from datetime import date

from sqlalchemy import delete
from sqlmodel import Session, SQLModel, func, select

from fetch_trades import fetch_month
from models import Trade, engine


def month_range(start: str, end: str) -> list[str]:
    """'202411', '202502' → ['202411', '202412', '202501', '202502']"""
    y, m = int(start[:4]), int(start[4:])
    result = []
    while f"{y}{m:02d}" <= end:
        result.append(f"{y}{m:02d}")
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return result


def load(lawd_cd: str, start: str, end: str) -> None:
    SQLModel.metadata.create_all(engine)  # 테이블 없으면 만들고, 있으면 그냥 둠

    with Session(engine) as session:
        for ym in month_range(start, end):
            trades = fetch_month(lawd_cd, ym)

            # 같은 달을 다시 받아도 중복 안 되게: 그 구·그 달 기존 행을 지우고 새로 넣는다
            y, m = int(ym[:4]), int(ym[4:])
            first_day = date(y, m, 1)
            next_first_day = date(y + 1, 1, 1) if m == 12 else date(y, m + 1, 1)
            session.execute(
                delete(Trade).where(
                    Trade.lawd_cd == lawd_cd,
                    Trade.deal_date >= first_day,
                    Trade.deal_date < next_first_day,
                )
            )
            session.add_all([Trade(**t) for t in trades])
            session.commit()  # 지우기 + 넣기가 여기서 한 번에 확정된다

            print(f"{ym}: {len(trades)}건")

        total = session.exec(select(func.count()).select_from(Trade)).one()
        print(f"DB 전체: {total}건")


if __name__ == "__main__":
    # 사용법: python load_trades.py 11440 202411 202510
    lawd_cd, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
    load(lawd_cd, start, end)
