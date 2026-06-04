# D-* Test ID (Logic Track)

| Test ID | PRD | 대상 (예정) |
|---------|-----|-------------|
| D-LOC-01 | FR-LOC-01 | 빈칸 2곳 좌표 (1-index) |
| D-VAL-01 | FR-VAL-01 | 행 4개 합 = 34 |
| D-VAL-02 | FR-VAL-02 | 열 4개 합 = 34 |
| D-VAL-03 | FR-VAL-03 | 주대각 `\` 합 = 34 |
| D-VAL-04 | FR-VAL-04 | 반대 `/` 합 = 34 (Mom Test) |
| D-VAL-05 | FR-VAL-05 | 10선 전체 = 34 |
| D-SOL-01 | FR-SOL-01 | 빈칸 2개 풀이 → `int[6]` |

**권장 RED 순서:** D-VAL-04 → D-VAL-05 → D-LOC-01 → D-SOL-01

**파일명:** `tests/entity/test_d_{loc|val|sol}_{nn}.py`
