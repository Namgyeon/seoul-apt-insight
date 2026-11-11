# 배운 것 노트

## 2026-11-01 — 1주차 완료 (GET / POST / pydantic)
- **pydantic = zod**: 함수 파라미터에 `pc: PcCreate`라고 쓰면 FastAPI가 알아서 검증하고, 실패하면 내 함수 실행 전에 422를 돌려준다. (path param도 body도 같은 원리)
- **점 vs 대괄호**: dict는 `pc["name"]`, 클래스 인스턴스(pydantic 모델)는 `pc.name`. JS는 둘이 같지만 Python은 구분한다. `len(pcs)`는 함수이고 `.length`가 아니다.
- **메모리 변수는 서버 끄면 사라진다**: `pcs` 리스트는 프로세스 RAM에 있어서 재시작하면 코드의 초기값 3개로 돌아감 (`useState` 새로고침과 같음). 그래서 DB가 필요하다.
- 다음 할 일: SQLite로 `pcs`를 디스크에 저장하기

## 2026-11-02 — 2주차 시작 (sqlite3 기본)
- **SQLite = 파일 하나짜리 DB**: `sqlite3.connect("app.db")`로 열고, SQL 문자열을 `cur.execute()`로 던진다. Python이 SQL로 바뀌는 게 아니라, Python이 SQL을 DB에 전달하는 구조. 서버 꺼도 파일은 남는다.
- **흐름은 항상 connect → cursor → execute → (commit) → fetch → close**. INSERT/UPDATE/DELETE는 `commit()` 없으면 저장 안 됨. 서버 안에선 요청마다 함수 **안에서** 열고 꼭 `close()`.
- **fetchone()은 없으면 None** (JS의 null). 그래서 `if row is None: 404`. 원소 1개 튜플은 `(2,)` 쉼표 필수, `(2)`는 그냥 숫자. SELECT 결과 기본은 튜플이라 `row[1]`로 꺼내야 함.
- 다음 할 일: `conn.row_factory = sqlite3.Row` + `[dict(row) for row in rows]`로 `/pcs` 응답을 `{"id":1,"name":"mac"}` 모양으로 바꾸기. 그다음 GET /pcs/{id}, POST 순서로 DB화.

## 2026-11-03 — 로드맵 개정 (코딩 없음)
- **학습법 전환**: 빈칸 채우기 폐기. Claude가 코드 짜고 나는 읽고 질문 답하기. 직접 치는 건 단계당 수정 1개. 근거: 공식 가이드들 공통 "코스 1개 + 깨지는 프로젝트 2~3개 + evals/배포".
- **12주 로드맵 확정** (ROADMAP.md): CRUD → Claude SDK 직접 → tool use/에이전트 루프 → MCP → RAG → 자동화·evals → Docker 배포. 수학·파인튜닝 스킵. 채용공고 필수 = Python·LLM·RAG·API·모니터링.
- **주제 = 내 실제 업무**: 콘솔PC → 원격으로 각 PC 들어가 용량·캡쳐 받아적고 PPT 결재. 구조: 각 PC 수집 스크립트 → FastAPI 서버+DB → LLM 요약/이상탐지 → PPT 자동 생성. 공부할 땐 맥에서 가짜 PC 스크립트로 시뮬레이션.
- 다음 할 일: PC마다 실제로 기록하는 항목(드라이브별 용량? 백업 성공/실패? 캡쳐?) 알려주기 → 그걸로 SQLModel `Pc` 모델 + CRUD 4개 작성.

## 2026-11-09 — 주제 변경 (코딩 없음)
- 백업일지는 "의미 없음"으로 폐기. 기준을 "이직 시장에서 눈에 띄는 것 + 데이터 많고 예측으로 인사이트 내는 것"으로 잡음.
- **새 주제: 서울 아파트 실거래가 인사이트.** 공공 API → DB → pandas 분석 → scikit-learn 예측 → Claude가 자연어 인사이트 + 채팅/MCP/자동 리포트. 공고에서 ML 38%, 데이터 파이프라인 18%까지 커버.
- 로드맵 구조는 동일(수집→분석→예측→LLM→MCP→RAG→자동화→배포), ML 2~5주 추가.
- 다음 할 일: 공공데이터포털 인증키 발급(숙제) → 1주차 데이터 수집 코드.

## 2026-11-11 — API 키 확인 (코딩 없음)
- 키 복사 실수(한글/특수문자 섞임)로 "등록되지 않은 서비스키". 공공데이터 키는 영문·숫자·`+/=` 88자, Decoding 키를 써야 함.
- 쿼리스트링에 넣을 땐 URL 인코딩 필요(`urllib.parse.quote`). 안 하면 400.
- 실거래가 API는 XML 응답. 가격은 `"260,000"` 문자열(만원), 날짜는 년/월/일 분리 → 적재할 때 변환 필요.
- 다음 할 일: fetch_trades.py + Trade 모델 + 마포구 1년치 적재.
