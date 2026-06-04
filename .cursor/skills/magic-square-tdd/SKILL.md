---
name: magic-square-tdd
description: MagicSquare_260604 Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. TDD, RED/GREEN/REFACTOR, Logic/UI Track, 10선 검증, pytest, ECB, Mom Test 작업 시 사용.
---

# magic-square-tdd

MagicSquare_260604 **Dual-Track TDD + ECB** 절차 SSOT. `.cursorrules`·PRD·Report와 충돌 시 `.cursorrules` 우선.

## 언제 이 Skill을 켜는가

다음 중 **하나라도** 해당하면 본 Skill을 읽고 따른다.

- 사용자가 TDD, RED/GREEN/REFACTOR, Logic/UI Track, ECB, 10선, Mom Test, `D-*`/`U-*` 테스트를 언급
- `tests/` 또는 `src/{entity,control,boundary}/` 코드·테스트 작성·수정
- `/tdd-red` 등 Command가 **아직 없거나** Command만으로 절차가 불충분할 때 — **본 Skill이 실행 절차 SSOT**
- `@magic-square-tdd` 또는 Skill 자동 매칭

**켜지 않음:** Report/Transcript Export만, git commit/push만, 범위 밖(3×3/5×5, PyQt 완성 앱).

## 시작 선언 (매 Phase 필수)

```
Phase: red|green|refactor | Layer: entity|control|boundary | Track: Logic|UI
Test ID: D-xxx-01 (또는 U-xxx-01) | PRD: FR-xxx-xx
```

한국어로 응답. git commit/push는 **사용자 요청 시만**.

---

## Logic Track vs UI Track

| 항목 | Logic Track | UI Track |
|------|-------------|----------|
| Layer | entity, control | boundary |
| 테스트 ID | `D-*` | `U-*` |
| 파일 | `tests/entity/test_d_*.py`, `tests/control/test_d_*.py` | `tests/boundary/test_u_*.py` |
| Mock | **Domain Mock 금지** (`@patch` entity/control 금지) | **Mock 허용** (I/O·위젯·control) |
| RED Then | `pytest.fail("RED: {ID} — …")` 또는 ImportError | 동일 |
| 10선 | D-VAL-* 에서 `\`·`/` **필수** (Mom Test) | 입력 E001~E003 위주 |

D-* 목록: [reference.md](reference.md)

---

## ECB · Mock · E001~E007

| 규칙 | 내용 |
|------|------|
| import | **boundary → control → entity** 단방향 |
| entity | **entity → \* import 금지** |
| entity E001~E005 | raise·return·문자열 emit **금지** (10선 **로직**만) |
| E004 | 줄 합 **판별** = entity · **코드 반환** = boundary/control |
| E006/E007 | entity **결과** → control/boundary가 코드 매핑 |
| E001~E007 최종 반환 | **boundary** |
| Logic Mock | entity/control `@patch` **금지** |
| UI Mock | boundary 테스트에서 **허용** |
| MagicConstant | `entity.constants` SSOT — `34`/`16`/`4` 리터럴 산재 금지 |

---

## RED (7단계)

1. **C2C 확인** — PRD FR ↔ Test ID ↔ Then ([reference.md](reference.md))
2. **선언** — `Phase: red | Layer: … | Track: … | Test ID: …`
3. **브랜치** — Logic → `red` (관례)
4. **테스트만 작성** — AAA 주석; 파일명 `test_d_*` / `test_u_*`
5. **Then** — `pytest.fail("RED: {TestID} — …")` 한 줄 **또는** 미구현 import (assert 본문·skip·xfail **금지**)
6. **`src/` 수정 금지** — RED는 `tests/`·`conftest`만
7. **pytest 실행** — 대상 테스트 **FAIL** 확인 후 보고

```bash
python -m pytest tests/entity/test_d_val_04.py -v
# 또는 ::test 함수 단위
```

**통과 기준:** exit code ≠ 0, FAIL 메시지에 Test ID 포함.

---

## GREEN (7단계)

1. **선언** — `Phase: green | Layer: … | Track: … | Test ID: …`
2. **브랜치** — Logic → `green` (관례)
3. **최소 구현** — 해당 Test ID를 통과시키는 **최소** `src/` 코드만
4. **ECB 준수** — import 방향, entity E001~E005 금지, SSOT 상수
5. **RED Then 교체** — `pytest.fail` 제거 → 실제 assert / golden
6. **pytest 실행** — 대상 테스트 **PASS**
7. **회귀** — 동일 Track 기존 테스트 PASS (`python -m pytest tests/entity/ -v`)

**통과 기준:** 대상 PASS + 기존 Logic/UI Track 회귀 없음.

---

## REFACTOR (7단계)

1. **선언** — `Phase: refactor | Layer: … | Track: …`
2. **전제** — 해당 Track **전체 GREEN** 상태
3. **브랜치** — `refactoring` (관례)
4. **범위** — smell 제거·이름·추출만; **기능·계약·assert 불변**
5. **금지** — 새 FR, 버그 수정, assert 완화, E001~E005 entity emit
6. **pytest 실행** — Track 전체 + golden (`UPDATE_GOLDEN` 없이 matched)
7. **보고** — 변경 요약 + 회귀 PASS 증거

```bash
python -m pytest tests/entity/ -v
python -m pytest tests/ -v   # REFACTOR 마무리 전 전체
```

---

## Test / Review Loop — pytest 언제 무엇을

| 시점 | 명령 | 통과 기준 |
|------|------|-----------|
| RED 직후 | `pytest {대상 파일}::test_* -v` | **FAIL** (의도적) |
| GREEN 직후 | 동일 + `pytest tests/{layer}/ -v` | 대상 **PASS**, 회귀 PASS |
| REFACTOR 중 | `pytest tests/entity/ -v` (Logic) | 전부 PASS |
| REFACTOR 후 | `pytest tests/ -v` | Logic+UI 전부 PASS |
| golden (D-SOL 등) | `pytest {test} -v` | approved 파일 **matched** |
| ECB 리뷰 (선택) | 코드 읽기 + grep `E00[1-5]`, `@patch`, `34` 리터럴 | 위반 0건 |

**설치:** `pip install -e ".[dev]"` · `pythonpath = ["src"]` (`pyproject.toml`).

**주의:** `tests/entity/__init__.py`가 `src/entity` import를 가릴 수 있음 — shadow 시 삭제 검토.

---

## 10선 체크리스트 (Mom Test)

D-VAL / 10선 관련 작업 시 **전부** 포함했는지 확인:

- [ ] 행 R1~R4
- [ ] 열 C1~C4
- [ ] 주대각 `\`
- [ ] 반대 `/` ← Mom Test 누락 지점

---

## 완료 보고 (매 Phase 끝)

```markdown
## TDD 보고
- Phase / Layer / Track / Test ID:
- 변경 파일: (tests/ 또는 src/ 목록)
- pytest: (명령 + exit code + PASS/FAIL 요약)
- ECB: import 방향 OK / entity E001~E005 없음 / SSOT OK
- 10선: (해당 시 `\`·`/` 포함 여부)
- 다음: (GREEN / REFACTOR / 다음 Test ID)
```

---

## 추가 자료

- D-* Test ID: [reference.md](reference.md)
- 헌법: `.cursorrules` · `docs/PRD.md` · `Report/01`~`02`
