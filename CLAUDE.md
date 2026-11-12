# AI 엔지니어 전환 프로젝트 — 리뷰 모드

이 폴더는 **AI 엔지니어 커리어 전환**을 위한 포트폴리오 프로젝트다. 결과물은 **서울 부동산 실거래가 인사이트 서비스**(공공데이터 → pandas/scikit-learn 예측 → Claude가 인사이트 설명, 채팅·MCP·자동 리포트) 하나를 끝까지 배포하는 것.
학습자는 프론트엔드(React, zod, React Query) 경험이 있고, Python/백엔드는 1주차 수준.
전체 계획은 `ROADMAP.md`. 환경: macOS, zsh, VS Code, `.venv`.

## 학습 방식 (2026-11-03 개정)
빈칸 채우기·한 줄씩 실험 방식은 **폐기**. 목표는 "코드를 읽고 판단하는 능력"이고, 이건 Claude가 짠 코드를 리뷰하면서 기른다.

1. **코드는 Claude가 짠다.** 단계 단위로 통째로 작성한다. 학습자가 치는 건 단계당 작은 수정 1개.
2. **작성 후 확인 질문 1~2개.** "이 줄 없으면?", "여기서 터지면 어디 봐야 해?" 수준. 답하면 통과. 못 답하면 그 부분만 다시 설명.
3. **개념은 압축 브리핑.** 새 문법·개념은 JS/React 비교로 3줄 안에. 길게 안 끈다.
4. **에러는 트레이스백 마지막 줄 같이 읽기.** 바로 고치되, 어디서 왜 났는지 한 줄은 짚는다.
5. **커밋은 학습자가 설명할 수 있을 때.** 설명 못 하면 상기시키고 커밋 보류. 커밋 메시지는 Claude가 초안.
6. **단계 끝나면 깨뜨리기 1개 + 배포 가능한 상태 확인.** 포트폴리오니까 항상 돌아가는 상태 유지.
7. **세션 끝**: NOTES.md에 "배운 개념 3줄 + 다음 할 일 1개", ROADMAP.md 진행 기록 갱신 제안.
8. 짧은 반말. 공식 코스는 해당 주차에 링크로 안내.

## 기술 스택 (확정)
- Python / FastAPI / SQLModel / SQLite(→ 필요 시 Postgres) / httpx
- pandas, scikit-learn (딥러닝 없음)
- Claude SDK 직접 호출 (LangGraph는 9~10주에 한 번 포팅)
- React(Vite) 채팅 UI, SSE 스트리밍
- FastMCP, sqlite-vec 또는 pgvector, Docker

## 현재 진도
- 2026-11-01: 1주차(구 로드맵) 완료. GET/POST, pydantic, 404/422.
- 2026-11-02: sqlite3 기본 (CREATE/INSERT/SELECT, fetchone/None, commit). GET /pcs를 DB 조회로 교체.
- 2026-11-03: 로드맵 개정(ROADMAP.md). git init + GitHub 공개 레포.
- 2026-11-09: 주제 변경 → **서울 부동산 실거래가 인사이트** (레포명 seoul-apt-insight). 기존 pcs 코드는 1주차에 Trade 테이블로 교체 예정. 코딩은 안 함.
- 2026-11-11: 공공데이터포털 인증키 발급 완료, API 호출 성공 확인(마포구 202510, 441건). 응답은 XML, dealAmount는 "260,000" 문자열, 거래일은 dealYear/Month/Day 분리.
- 2026-11-12: `fetch_trades.py` 작성(httpx + XML 파싱, 마포구 202510 441건 성공). PYTHON_CHEATSHEET.md 생성(JS 비교 문법표, 새 문법 나오면 계속 추가). 기술문서는 docs/에.
- 2026-11-12 (2차): 학습자가 03 처리 직접 수정. `models.py`(Trade) + `load_trades.py`(월별 지우고 넣기, 트랜잭션) 작성, 마포구 202411~202510 4,323건 적재. 컬럼은 영어 유지, docs/COLUMNS.md에 한글 대조표.
- 다음 할 일: main.py의 pcs 코드 제거 → `GET /trades`(구·기간 필터, SQLModel select) API. 학습자는 문법을 모름: 새 코드마다 처음 나온 문법을 치트시트에 추가하고 JS 비교로 짧게 설명할 것. 확인 질문은 "코드 지우면?" 대신 구체적 상황과 숫자로 물을 것.
