# Python 문법 치트시트 (JS 비교)

프로젝트 코드에 처음 나온 문법만 쌓는다. 모르는 줄 나오면 여기부터 확인.

## 기본
| Python | JS | 메모 |
|---|---|---|
| `import os` | `import os from 'os'` | 모듈 통째로 가져오기 |
| `from datetime import date` | `import { date } from 'datetime'` | 일부만 가져오기 |
| `x = 1` | `const x = 1` | 선언 키워드 없음 |
| `API_KEY = ...` (대문자) | `const API_KEY` | 대문자 = "바꾸지 마" 관례일 뿐, 강제 아님 |
| 들여쓰기 | `{ }` | 들여쓰기가 곧 블록. 틀리면 에러 |
| `# 주석` | `// 주석` | |
| `"""설명"""` (함수 첫 줄) | `/** JSDoc */` | docstring. 함수 설명 |
| `None` | `null` | 비교는 `is None` |
| `True` / `False` | `true` / `false` | 대문자 |

## 함수
| Python | JS | 메모 |
|---|---|---|
| `def f(a: str) -> list[dict]:` | `function f(a: string): Record[]` | `: 타입`, `-> 리턴타입`. TS 타입처럼 실행엔 영향 없음 |
| `lambda tag: ...` | `(tag) => ...` | 한 줄짜리 화살표 함수 |
| `return` 없으면 | `undefined` 리턴 | Python은 `None` 리턴 |

## 자료형
| Python | JS | 메모 |
|---|---|---|
| `[1, 2]` | `[1, 2]` | list |
| `{"a": 1}` | `{ a: 1 }` | dict. 키에 따옴표 필수, `d["a"]`로 접근 (`d.a` 안 됨) |
| `(1, 2)` | 없음 | tuple. 수정 못 하는 list. 원소 1개면 `(1,)` |
| `[f(x) for x in xs]` | `xs.map(f)` | 리스트 컴프리헨션 |
| `[x for x in xs if x > 0]` | `xs.filter(x => x > 0)` | |
| `len(xs)` | `xs.length` | 함수임 |
| `f"{n}건"` | `` `${n}건` `` | f-string = 템플릿 리터럴 |

## 문자열 / 숫자 변환
| Python | JS | 메모 |
|---|---|---|
| `int("260000")` | `parseInt("260000")` | 실패하면 에러 (NaN 아님) |
| `float("84.98")` | `parseFloat("84.98")` | |
| `s.replace(",", "")` | `s.replaceAll(",", "")` | Python replace는 기본이 전부 바꿈 |
| `s.strip()` | `s.trim()` | |
| `a or b` | `a \|\| b` | |

## 에러
| Python | JS | 메모 |
|---|---|---|
| `raise RuntimeError("msg")` | `throw new Error("msg")` | |
| `try: / except X:` | `try { } catch { }` | |

## 파일 실행
| Python | JS | 메모 |
|---|---|---|
| `if __name__ == "__main__":` | `if (require.main === module)` | "직접 실행했을 때만" 돌리는 블록. import되면 안 돌음 |

## 라이브러리 (이 프로젝트)
| Python | JS | 메모 |
|---|---|---|
| `load_dotenv()` + `os.environ["K"]` | `import.meta.env.K` | `.env` 읽기 |
| `httpx.get(url, params=p)` | `fetch(url + '?' + new URLSearchParams(p))` | 쿼리 인코딩 자동 |
| `resp.raise_for_status()` | `if (!res.ok) throw ...` | 4xx/5xx면 에러 |
| pydantic `BaseModel` | zod schema | 타입 검증 |

## 2026-11-12 추가 (models.py, load_trades.py)
| Python | JS | 메모 |
|---|---|---|
| `class Trade(SQLModel, table=True):` | `class Trade extends SQLModel` | 괄호 안이 부모 클래스. `table=True`면 DB 테이블도 됨 |
| `price: int` (클래스 안) | TS `price: number` | 필드 선언. SQLModel이 이걸 보고 컬럼을 만듦 |
| `int \| None = None` | `number \| null = null` | 없어도 되는 값 |
| `y, m = 2025, 10` | `const [y, m] = [2025, 10]` | 구조 분해 |
| `a if 조건 else b` | `조건 ? a : b` | 삼항 연산자. 순서가 다름 |
| `f"{m:02d}"` | `String(m).padStart(2, "0")` | 2자리 0 채우기. 3 → "03" |
| `while 조건:` | `while (조건) { }` | |
| `Trade(**t)` | `new Trade({ ...t })` | dict를 펼쳐서 인자로 넘김 |
| `with Session(engine) as s:` | `try { ... } finally { s.close() }` | 블록 끝나면 자동으로 닫아줌 |
| `sys.argv[1]` | `process.argv[2]` | 명령줄 인자. Python은 1부터 |
