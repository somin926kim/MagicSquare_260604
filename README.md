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

## 아키텍처 (목표)

- **ECB:** Entity(판정·풀이) / Control(흐름) / Boundary(UI·I/O)
- **Dual-Track TDD:** Logic Track + UI Track
- **RED 우선:** pytest FAIL 확인 → GREEN → REFACTOR

| 계층 | 후보 (슬라이드 4.1) |
|------|---------------------|
| Entity | `MagicSquare`, `Cell`, `SolveResult` |
| Control | `SquareValidator`, `MissingFinder`, `Solver` |
| Boundary | `GridUI`, `InputHandler`, `ResultDisplay` |

## 프로젝트 구조 (현재)

```
MagicSquare_260604/
├── README.md
├── docs/
│   └── PRD.md
├── Report/
│   └── 01.MagicSquare_ProblemDefinition_Report.md
└── Prompting/
    └── 01.MagicSquare_ProblemDefinition-Transcript.md
```

`src/`, `tests/`, `.cursorrules` — **후속 세션** (Rule · Command · Test Loop)

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 기능 요구(FR)·도메인 규칙·C2C·SC |
| [Report/01](Report/01.MagicSquare_ProblemDefinition_Report.md) | Mom Test · R-G-I-O · 세션 3 워크북 · 범위 In/Out |
| [Prompting/01](Prompting/01.MagicSquare_ProblemDefinition-Transcript.md) | STEP 1 인터뷰 Export |

## 세션 3 범위 (In / Out)

**In:** 4×4·빈칸 2·10선=34 판정, ECB 분류, Rule / Command / (Skill) / Test Loop 설계  

**Out:** PyQt 완성 앱·배포, 3×3/5×5 확장, Domain GREEN·UI 완료를 STEP 1 목표로 삼지 않음

## 다음 단계

1. `.cursorrules` — 4×4·10선·34·TDD/ECB 용어 고정  
2. `/tdd-red` — **D-VAL-04** (`/`) RED → FAIL 확인 (Mom Test 재현)  
3. `src/` · `tests/` ECB 골격 및 `pytest` harness

## 표면 문제 (하지 않을 것)

「4×4 마방진 **검증/풀이 프로그램**」 또는 **ECB·UI 완성 앱**을 1차 목표로 삼지 않는다. 1차 목표는 **10선 판정 누락(특히 `/`)** 을 드러내는 것이다.
