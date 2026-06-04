# MagicSquare_260604

4×4 **부분 마방진**(빈칸 2개, 1~16, 합 **34**) 과제에서 **10선**(행4·열4·`\`·`/`) 판정을 빠짐없이 검증하기 위한 프로젝트입니다.

> **Mom Test:** 행·열·주대각선(`\`)만 확인하고 **반대 대각선(`/`)** 을 빼먹어, 조교에게 보이기 전에 틀림을 알게 되고 **약 15분**을 추가로 쓴 경험을, **기계적·재현 가능한 판정**으로 바꾸는 것이 목표입니다.

**저장소:** https://github.com/somin926kim/MagicSquare_260604

## 진짜 문제 (한 문장)

빈칸 두 칸을 채운 뒤 행·열과 주대각선(`\`)만 확인하고 완료로 여겼고, 반대 대각선(`/`)을 빼먹어 조교에게 보이기 전에 틀림을 알게 되어 약 15분을 추가로 썼다.

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (중복 없음) |
| 빈칸 | **정확히 2개** (`0` — `BLANK_CELL`) |
| 마법 상수 | **34** (`MAGIC_CONSTANT`) |
| 검증 대상 | **10선** — 행 4 + 열 4 + `\` + `/` |

상수 SSOT: [`src/entity/constants.py`](src/entity/constants.py)

## 성공 기준 (Mom Test)

| ID | 기준 |
|----|------|
| SC-1 | **10선 합 전부** 계산·검증 (행·열만 X, **`/` 포함**) |
| SC-2 | 한 줄이라도 ≠34 → **실패 + 깨진 줄 식별** |
| SC-3 | 동일 유형 문제에서 원인 특정 **1분 이내** (기준: 과거 15분) |

## 아키텍처

- **ECB:** Entity(판정·풀이) / Control(흐름) / Boundary(UI·I/O)
- **Dual-Track TDD:** Logic Track (`D-*`) + UI Track (`U-*`)
- **RED → GREEN → REFACTOR**

| 계층 | 구현 상태 | 역할 |
|------|-----------|------|
| **Entity** | ✅ 부분 (`locator`, `solver`, `validator`) | 10선·빈칸·풀이 — E001~E005 emit 없음 |
| Control | 🔲 미구현 | 흐름·entity 호출·결과 매핑 |
| Boundary | 🔲 미구현 | 입력·UI·E001~E007 반환 |

의존 방향: **boundary → control → entity** (단방향). E001~E007 최종 반환은 **boundary**.

## 구현 현황 (entity)

| 모듈 | 함수 | Test ID | 상태 |
|------|------|---------|------|
| `locator.py` | `find_blank_coords` | D-LOC-01 | GREEN ✅ |
| `solver.py` | `solve` → `int[6]` | D-SOL-01 | GREEN ✅ + [golden](tests/golden/d_sol_01_g1_step_a.approved.txt) |
| `validator.py` | `anti_diagonal_sum`, `validate_anti_diagonal` | D-VAL-04 | GREEN ✅ (Mom Test `/`) |
| `solver.py` | `_all_lines_match_magic_constant` | (내부) | D-VAL-05 전에 **REFACTOR P0** — 10선 SSOT 중복 |

**G1 풀이:** `[2, 3, 11, 4, 4, 1]` — blank (2,3)←11, (4,4)←1

## 프로젝트 구조

```
MagicSquare_260604/
├── README.md
├── .cursorrules                    # ECB·Dual-Track TDD 헌법
├── pyproject.toml                  # pytest harness (pythonpath=src)
├── docs/PRD.md
├── Report/                         # 01~06 세션 보고서
├── Prompting/                      # 01~05 Transcript Export
├── .cursor/
│   ├── commands/tdd-red.md
│   └── skills/magic-square-tdd/
├── tests/
│   ├── conftest.py                 # grid_g1, grid_g1_solved
│   ├── _approval.py              # Golden Master
│   ├── entity/                     # D-* Logic tests
│   ├── golden/
│   ├── control/                    # (예정)
│   └── boundary/                   # (예정)
└── src/
    ├── entity/
    │   ├── constants.py
    │   ├── locator.py
    │   ├── solver.py
    │   └── validator.py
    ├── control/
    └── boundary/
```

## 테스트 ID

### Logic Track (`D-*`)

| Test ID | PRD | 상태 | 비고 |
|---------|-----|------|------|
| D-LOC-01 | FR-LOC-01 | GREEN ✅ | `[(2,3),(4,4)]` 1-index |
| D-SOL-01 | FR-SOL-01 | GREEN ✅ | `int[6]` + Golden Master |
| D-VAL-04 | FR-VAL-04 | GREEN ✅ | `/` 합 = 34 · `grid_g1_solved` |
| D-VAL-05 | FR-VAL-05 | 🔲 | 10선 전체 = 34 |

전체 목록: [`.cursor/skills/magic-square-tdd/reference.md`](.cursor/skills/magic-square-tdd/reference.md)

### UI Track (`U-*`)

| Test ID | PRD | 상태 | Then |
|---------|-----|------|------|
| U-IN-01 | FR-IN-01 | 🔲 | `grid=None` → `"E003"` |
| U-IN-02 | FR-IN-02 | 🔲 | 3×3 격자 → `"E001"` |

## 개발

### 요구 사항

- Python **3.10+**
- dev: `pytest>=8` (`pyproject.toml` `[project.optional-dependencies]`)

### 가상환경 · 설치

```powershell
cd MagicSquare_260604
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

### 테스트 실행

```bash
# 전체 Logic GREEN (현재 3 passed)
python -m pytest tests/ -v

# 단일 Test ID
python -m pytest tests/entity/test_d_val_04.py -v
python -m pytest tests/entity/test_d_sol_01.py -v
python -m pytest tests/entity/test_d_loc_01.py -v
```

### Golden Master (D-SOL-01)

```powershell
$env:UPDATE_GOLDEN="1"
python -m pytest tests/entity/test_d_sol_01.py -v
Remove-Item Env:UPDATE_GOLDEN
# 이후 일반 실행으로 approved.txt와 일치 확인
```

### Git 브랜치 (관례)

| 브랜치 | 용도 |
|--------|------|
| `main` | 안정 기준 |
| `spec` | PRD·설계 SSOT |
| `red` | RED — `tests/`만 (FAIL 확인) |
| `green` | GREEN — `src/entity` 구현 |
| `refactoring` | REFACTOR — 동작 불변 정리 |

Logic RED → **`red`** · GREEN/REFACTOR → **`green`** (또는 `refactoring`).

### Cursor 워크플로

| 리소스 | 경로 |
|--------|------|
| Skill (TDD·ECB SSOT) | `.cursor/skills/magic-square-tdd/SKILL.md` |
| Command RED | `.cursor/commands/tdd-red.md` |
| Test ID 목록 | `.cursor/skills/magic-square-tdd/reference.md` |

**REFACTOR (현재):** `/refactor-smell` 완료 → 다음 `/refactor-safe` (P0: 10선 SSOT, [Report/06](Report/06.MagicSquare_REFACTOR_Smell_Report.md))

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | FR·도메인·C2C·SC |
| [Report/01](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test · 문제 정의 |
| [Report/02](Report/02.MagicSquare_Session3_CursorDesign_Report.md) | Harness · `.cursorrules` |
| [Report/03](Report/03.MagicSquare_TDD_RED_Report.md) | spec→red · RED 스켈레톤 |
| [Report/04](Report/04.MagicSquare_GREEN_GoldenMaster_Report.md) | D-LOC/D-SOL GREEN · Golden |
| [Report/05](Report/05.MagicSquare_DVAL04_GREEN_Report.md) | D-VAL-04 GREEN · `/` |
| [Report/06](Report/06.MagicSquare_REFACTOR_Smell_Report.md) | 코드 스멜 · `/refactor-safe` 후보 |
| [Prompting/01–05](Prompting/) | 세션 Transcript Export |

## 범위 (In / Out)

**In:** 4×4·빈칸 2·10선=34, ECB, Dual-Track TDD, Rule / Command / Skill / Test Loop

**Out:** PyQt 완성 앱·배포, 3×3/5×5 확장, 「완성 앱」을 1차 목표로 삼지 않음

## 현재 진행 · 다음 단계

| 상태 | 항목 |
|------|------|
| ✅ | PRD · Mom Test · ECB · Harness |
| ✅ | **D-LOC-01** · **D-SOL-01** · **D-VAL-04** GREEN |
| ✅ | `tests/` **3 passed** · golden `d_sol_01_g1_step_a` |
| ✅ | `/refactor-smell` ([Report/06](Report/06.MagicSquare_REFACTOR_Smell_Report.md)) |
| 🔲 | **`/refactor-safe`** — P0: `validator` 10선 SSOT · `solver` 위임 |
| 🔲 | **D-VAL-05** — 10선 전체 검증 |
| 🔲 | **U-IN-01/02** — boundary RED/GREEN |

**원격 `green`:** `7736146` (`docs: D-VAL-04 GREEN…`). 로컬에 Report/06·Prompting/05·본 README 갱신이 있으면 commit/push로 동기화.

## 표면 문제 (하지 않을 것)

「4×4 마방진 **검증/풀이 프로그램**」 또는 **ECB·UI 완성 앱**을 1차 목표로 삼지 않는다. 1차 목표는 **10선 판정 누락(특히 `/`)** 을 드러내는 것이다.
