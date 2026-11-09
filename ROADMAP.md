# AI 엔지니어 전환 로드맵 (12주) — 서울 부동산 실거래가 인사이트

**목표**: AI 엔지니어로 커리어 전환. 포트폴리오 = "데이터 → 예측 → LLM이 인사이트 설명" 서비스 하나를 끝까지 배포.
**주제**: 서울 아파트 실거래가(매매·전세) 공공데이터로 지역별 추세·전세가율·이상거래를 분석/예측하고, 채팅·자동 리포트·MCP로 제공.
**조건**: 주 3~5시간, 세션은 밤 11:30 전 종료. Python/FastAPI, React UI, Claude SDK 직접.
**학습법**: 코드는 Claude가 짜고, 나는 읽고 판단한다. 단계마다 직접 치는 것 1개, 읽을 자료 1개, 배포되는 결과물 1개.

## 조사 근거 (2026-11-03)
- 채용공고 3,449건 분석: Python 71%, LLM 66%, RAG 40%, ML 38%, API 33%, 모니터링 31%, SQL 19%, Docker 18%, 데이터 파이프라인 18%. 신입 공고 6%, 대부분 "배포한 프로젝트 1개 이상" 요구. ([dev.to](https://dev.to/gnana_6392e836fd500a957dc/ai-engineer-skills-companies-want-in-2026-3449-posting-analysis-5f9l))
- Anthropic "Building Effective Agents": API 직접 호출부터, 에이전트보다 워크플로우 패턴 먼저. ([원문](https://www.anthropic.com/research/building-effective-agents))
- 오픈소스 로드맵 공통: 코스 1개 + 깨지는 프로젝트 2~3개 → evals/트레이싱/배포. 딥러닝·파인튜닝 스킵. ([start-ai-engineering](https://github.com/louisfb01/start-ai-engineering), [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch))
- 무료 코스: [Anthropic Academy](https://anthropic.skilljar.com/) (Claude API, MCP), [MS ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)

## 데이터 소스
- 국토교통부 아파트 매매/전월세 실거래가 API (공공데이터포털, 무료, 인증키 필요)
- 한국은행 ECOS 기준금리 API
- (선택) 서울 열린데이터 인구·공급 통계

## 주차별 계획

| 주 | 단계 | 결과물 | 병행 자료 |
|---|---|---|---|
| 1 | **데이터 수집 + DB**: 공공 API 호출(httpx) → SQLModel `Trade` 테이블 적재, CRUD/조회 API, `.env`로 키 관리, router 분리 | 한 구(區) 1년치 거래가 DB에 들어간 FastAPI | - |
| 2~3 | **pandas + 기초 분석**: 월별 평균가·거래량·전세가율, 이상 거래(시세 대비 ±20%) 탐지, 분석 결과 API | `/stats/{구}` 엔드포인트 + React 차트 | pandas 10 minutes 문서 |
| 4~5 | **scikit-learn 예측**: 베이스라인(이동평균) → 회귀 모델, 교차검증, 지표(MAE). 금리 피처 추가 | 3개월 뒤 평균가 예측 + 평가 리포트 | scikit-learn 튜토리얼 |
| 6~7 | **Claude SDK**: 분석·예측 결과를 LLM이 자연어 인사이트로. 구조화 출력, 스트리밍 → React 채팅 UI. Tool use로 DB·모델 호출 ("마포구 전세 요즘 어때?") | 채팅으로 데이터 질의 | Academy: Building with the Claude API |
| 8 | **MCP 서버**: 데이터 조회·예측 도구를 Claude Code/데스크탑에 노출 | MCP 서버 | Academy: Intro to MCP |
| 9 | **RAG**: 부동산 정책·뉴스 문서 임베딩, 출처 달아서 "왜 올랐나" 답변 | 문서 질의 | - |
| 10 | **자동화 + Evals + 관측**: 스케줄러로 주간 데이터 갱신·리포트 생성, 예측 정확도 추적, LLM 답변 eval | 주간 자동 리포트 | Hamel Husain evals 글 |
| 11~12 | **Docker + 배포 + README** | 실제 URL + 포트폴리오 README | - |

## 스킵하는 것
딥러닝/PyTorch, 파인튜닝, 멀티 에이전트, 자체 모델 서빙, Kubernetes. 주식·코인 예측.

## 진행 기록
- 2026-11-03: 1차 로드맵(백업일지) 확정.
- 2026-11-09: 주제를 **서울 부동산 실거래가 인사이트**로 변경. ML(pandas/scikit-learn) 2~5주 추가, 멀티에이전트 제외.
