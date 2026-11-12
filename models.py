from datetime import date

from sqlmodel import Field, SQLModel, create_engine


class Trade(SQLModel, table=True):
    """아파트 매매 실거래 1건 = 테이블의 한 행."""

    id: int | None = Field(default=None, primary_key=True)  # DB가 자동으로 1, 2, 3... 채움
    lawd_cd: str = Field(index=True)  # 구 코드 (마포구 11440)
    apt_seq: str = Field(index=True)  # 단지 고유번호
    apt_name: str
    dong: str
    price: int  # 만원 단위
    area: float  # 전용면적 ㎡
    floor: int
    build_year: int
    deal_date: date = Field(index=True)


# DB 파일 연결 설정. 실제 연결은 Session을 열 때 생긴다.
engine = create_engine("sqlite:///trades.db")
