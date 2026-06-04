# MagicSquare_260604

4×4 **부분 마방진**(빈칸 2개, 1~16, 합 **34**) 과제에서 **10선**(행4·열4·`\`·`/`) 판정을 빠짐없이 검증하기 위한 프로젝트입니다.

> **Mom Test:** 행·열·주대각선(`\`)만 확인하고 **반대 대각선(`/`)** 을 빼먹어, 조교에게 보이기 전에 틀림을 알게 되고 **약 15분**을 추가로 쓴 경험을, **기계적·재현 가능한 판정**으로 바꾸는 것이 목표입니다.

## 진짜 문제 (한 문장)

빈칸 두 칸을 채운 뒤 행·열과 주대각선(`\`)만 확인하고 완료로 여겼고, 반대 대각선(`/`)을 빼먹어 조교에게 보이기 전에 틀림을 알게 되어 약 15분을 추가로 썼다.

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (중복 없음) |
| 빈칸 | **정확히 2개** (`0` 또는 `?`) |
| 마법 상수 | **34** |
| 검증 대상 | **10선** — 행 4 + 열 4 + `\` + `/` |

## 성공 기준 (Mom Test)

| ID | 기준 |
|----|------|
| SC-1 | **10선 합 전부** 계산·검증 (행·열만 X, **`/` 포함**) |
| SC-2 | 한 줄이라도 ≠34 → **실패 + 깨진 줄 식별** |
| SC-3 | 동일 유형 문제에서 원인 특정 **1분 이내** (기준: 과거 15분) |

## 아키텍처

- **ECB:** Entity(판정·풀이) / Control(흐름) / Boundary(UI·I/O)
- **Dual-Track TDD:** Logic Track (`D-*`) + UI Track (`U-*`)
- **RED 우선:** pytest FAIL 확인 → GREEN → REFACTOR

| 계층 | 후보 | 역할 |
|------|------|------|
| Entity | `MagicSquare`, `Cell`, `SolveResult` | 10선 판정·빈칸 탐색·풀이 |
| Control | `SquareValidator`, `MissingFinder`, `Solver` | 흐름·entity 호출·결과 매핑 |
| Boundary | `GridUI`, `InputHandler`, `ResultDisplay` | 입력 검증·UI·E001~E007 반환 |

의존 방향: **boundary → control → entity** (단방향). E001~E007 최종 반환은 **boundary**.

## 프로젝트 구조

```
MagicSquare_260604/
├── README.md
├── .cursorrules                    # ECB·Dual-Track TDD 헌법
├── pyproject.toml                  # pytest harness (pythonpath=src)
├── .gitignore
├── docs/
│   └── PRD.md
├── Report/
│   ├── 01.MagicSquare_ProblemDefinition_Report.md
│   ├── 02.MagicSquare_Session3_CursorDesign_Report.md
│   ├── 03.MagicSquare_TDD_RED_Report.md
│   ├── 04.MagicSquare_GREEN_GoldenMaster_Report.md
│   └── 05.MagicSquare_DVAL04_GREEN_Report.md
├── Prompting/
│   ├── 01.MagicSquare_ProblemDefinition-Transcript.md
│   ├── 02.MagicSquare_Session3_CursorDesign-Transcript.md
│   ├── 03.MagicSquare_TDD_RED-Transcript.md
│   └── 04.MagicSquare_GREEN_GoldenMaster-Transcript.md
├── .cursor/
│   ├── commands/
│   │   └── tdd-red.md              # RED 단계 Command
│   └── skills/
│       └── magic-square-tdd/       # TDD·ECB 절차 Skill
│           ├── SKILL.md
│           └── reference.md        # D-* Test ID SSOT
├── tests/
│   ├── conftest.py                 # grid_g1, grid_g1_solved (로직 없음)
│   ├── entity/
│   │   ├── test_d_val_04.py        # D-VAL-04 GREEN (Mom Test `/`)
│   │   ├── test_d_loc_01.py        # D-LOC-01 GREEN
│   │   └── test_d_sol_01.py        # D-SOL-01 GREEN + golden
│   ├── golden/
│   │   └── d_sol_01_g1_step_a.approved.txt
│   ├── _approval.py                # Golden Master 헬퍼
│   ├── control/
│   └── boundary/
└── src/
    ├── entity/
    │   ├── constants.py
    │   ├── locator.py
    │   ├── validator.py
    │   └── solver.py
    ├── control/
    └── boundary/
```

## 테스트 ID

### Logic Track (`D-*`) — `tests/entity/` · `tests/control/`

| Test ID | PRD | 대상 |
|---------|-----|------|
| D-VAL-04 | FR-VAL-04 | 반대 `/` 합 = 34 **(Mom Test, GREEN ✅)** |
| D-VAL-05 | FR-VAL-05 | 10선 전체 = 34 |
| D-LOC-01 | FR-LOC-01 | 빈칸 2곳 좌표 (1-index) **(GREEN ✅)** |
| D-SOL-01 | FR-SOL-01 | 빈칸 2개 풀이 → `int[6]` **(GREEN ✅ + golden)** |

**권장 RED 순서:** D-VAL-04 → D-VAL-05 → D-LOC-01 → D-SOL-01

전체 목록: [`.cursor/skills/magic-square-tdd/reference.md`](.cursor/skills/magic-square-tdd/reference.md)

### UI Track (`U-*`) — `tests/boundary/`

| Test ID | PRD | Given → Then |
|---------|-----|--------------|
| U-IN-01 | FR-IN-01 | `grid=None` → `"E003"` |
| U-IN-02 | FR-IN-02 | 3×3 격자 → `"E001"` |

## 개발

### 요구 사항

- Python **3.10+**
- pytest **8+** (`pip install pytest`)

### 테스트 실행

```bash
# tests/ 전체 (현재 3 passed)
python -m pytest tests/ -v

# D-VAL-04 GREEN (Mom Test `/`)
python -m pytest tests/entity/test_d_val_04.py::test_d_val_04_anti_diagonal_sum -v
```

GREEN 성공 기준: exit code = 0 · 대상 Test ID PASS.

### Git 브랜치 (관례)

| 브랜치 | 용도 |
|--------|------|
| `main` | 안정 기준 |
| `red` | RED — 실패 테스트만 (`tests/`·`conftest`) |
| `green` | GREEN — `src/` 구현으로 테스트 통과 |
| `refactoring` | REFACTOR — 동작 불변 정리 |
| `staging` | 통합·검토 |

Logic Track RED 작업 시 **`red`** 브랜치에서 진행.

### Cursor 워크플로

| 리소스 | 경로 | 설명 |
|--------|------|------|
| Skill | `.cursor/skills/magic-square-tdd/SKILL.md` | Dual-Track TDD·ECB 절차 SSOT |
| Command | `.cursor/commands/tdd-red.md` | RED 단계 전용 |
| Test ID | `.cursor/skills/magic-square-tdd/reference.md` | `D-*` 목록 |

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 기능 요구(FR)·도메인 규칙·C2C·SC |
| [Report/01](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test · R-G-I-O · 문제 정의 |
| [Report/02](Report/02.MagicSquare_Session3_CursorDesign_Report.md) | 세션 3 Harness · `.cursorrules` · Git 동기화 |
| [Report/03](Report/03.MagicSquare_TDD_RED_Report.md) | spec→red 통합 · RED 스켈레톤 · green 전략 |
| [Report/04](Report/04.MagicSquare_GREEN_GoldenMaster_Report.md) | D-LOC/D-SOL GREEN · Golden Master |
| [Report/05](Report/05.MagicSquare_DVAL04_GREEN_Report.md) | D-VAL-04 GREEN · Mom Test `/` |
| [Prompting/01](Prompting/01.MagicSquare_ProblemDefinition-Transcript.md) | STEP 1 Mom Test 인터뷰 Export |
| [Prompting/02](Prompting/02.MagicSquare_Session3_CursorDesign-Transcript.md) | STEP 3 Harness 세션 Export |
| [Prompting/03](Prompting/03.MagicSquare_TDD_RED-Transcript.md) | TDD RED 루프 세션 Export |
| [Prompting/04](Prompting/04.MagicSquare_GREEN_GoldenMaster-Transcript.md) | GREEN · Golden Master 세션 Export |

## 범위 (In / Out)

**In:** 4×4·빈칸 2·10선=34 판정, ECB, Dual-Track TDD, Rule / Command / Skill / Test Loop

**Out:** PyQt 완성 앱·배포, 3×3/5×5 확장, Domain GREEN·UI 완료를 1차 목표로 삼지 않음

## 현재 진행 · 다음 단계

| 상태 | 항목 |
|------|------|
| ✅ | PRD · Mom Test · ECB · Harness (`spec`/`red`) |
| ✅ | **D-LOC-01** · **D-SOL-01** · **D-VAL-04** GREEN (+ golden) |
| ✅ | `tests/` **3 passed** · `origin/green` (`4f82550`까지) |
| 🔲 | D-VAL-05 · U-IN-01/02 RED/GREEN |
| 🔲 | REFACTOR (`/refactor-smell` → `/refactor-safe`) |

## 표면 문제 (하지 않을 것)

「4×4 마방진 **검증/풀이 프로그램**」 또는 **ECB·UI 완성 앱**을 1차 목표로 삼지 않는다. 1차 목표는 **10선 판정 누락(특히 `/`)** 을 드러내는 것이다.
