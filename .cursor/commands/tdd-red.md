# TDD RED — 실패 테스트 먼저

MagicSquare_260604 **Dual-Track TDD** — **RED 단계만**. GREEN/REFACTOR·`src/` 구현은 하지 않는다.  
상세 절차: `.cursor/skills/magic-square-tdd/SKILL.md` · D-* ID: `reference.md` · 헌법: `.cursorrules`

---

## 필수 선언

**응답 첫 줄:**

```
Phase: red | Layer: entity|control|boundary | Track: Logic|UI | Test ID: D-xxx-01 (또는 U-xxx-01)
```

한국어. git commit/push는 사용자 요청 시만.

---

## 절차

1. **Test ID 확인** — Report/02 · `.cursor/skills/magic-square-tdd/reference.md` · PRD §8 C2C. 없으면 사용자에게 ID 확인.
2. **C2C 고정** — PRD FR ↔ Test ID ↔ Then (Given/When/Then) 주석으로 기록.
3. **파일 위치**
   - Logic: `tests/entity/test_d_*.py` 또는 `tests/control/test_d_*.py`
   - UI: `tests/boundary/test_u_*.py`
4. **AAA 테스트 작성** — Given/When/Then 주석. When은 주석 또는 미호출(스켈레톤).
5. **Then (RED)** — `pytest.fail("RED: {TestID} — …")` **한 줄** 또는 미구현 import. assert 본문·통과 더미 없음.
6. **`tests/`·`conftest`만 수정** — `src/` **수정 금지**.
7. **pytest 실행** — 대상 테스트 **FAIL** (exit ≠ 0) 확인 후 보고.

**Logic Track RED 권장 순서 (Mom Test):** D-VAL-04 (`/`) → D-VAL-05 (10선) → D-LOC-01 → D-SOL-01  
**UI Track 예:** U-IN-01 (`None` → `"E003"`), U-IN-02 (3×3 → `"E001"`)

---

## pytest 예시 (bash)

```bash
# 단일 테스트 (권장)
python -m pytest tests/entity/test_d_val_04.py::test_d_val_04_anti_diagonal_sum -v

# 파일 전체
python -m pytest tests/entity/test_d_val_04.py -v

# Test ID 키워드
python -m pytest tests/ -k "d_val_04" -v
```

**RED 성공 기준:** exit code ≠ 0 · FAIL 메시지에 Test ID 포함 · `pytest.fail("RED: …")` 또는 ImportError/ModuleNotFoundError.

---

## 보고

```markdown
## RED 보고
- Test ID / PRD / Track / Layer:
- pytest: (명령 + exit code + FAIL 한 줄 요약)
- 변경 파일: tests/ … 만 (src/ 없음)
- 다음: GREEN (사용자 지시 또는 GREEN Command)
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` 수정 | RED는 실패 테스트만 |
| Logic Track Domain Mock (`@patch` entity/control) | Dual-Track 규칙 |
| assert 완화·더미 통과 | Loop 우회 |
| `pytest.skip` · `xfail` | RED 증거 훼손 |
| entity E001~E005 emit (테스트·코드) | ECB 계약 |
| `34`/`16`/`4` 리터럴 (테스트·conftest) | MagicConstant SSOT — `entity.constants` import |
