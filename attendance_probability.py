from typing import Dict, Tuple

class AttendanceProblem:
    def __init__(self, n: int):
        self.n = n
        self.memo: Dict[Tuple[int, int], int] = {}

    def count_ways(self) -> Tuple[int, int]:
        total_ways = self.valid_seq(0, 0)
        self.memo.clear() 
        miss_graduation = self._count_miss_graduation(0, 0)
        return total_ways, miss_graduation

    def valid_seq(self, day: int, misses: int) -> int:
        if (day, misses) in self.memo:
            return self.memo[(day, misses)]

        if misses >= 4:
            return 0

        if day == self.n:
            return 1

        attend = self.valid_seq(day + 1, 0)
        miss = self.valid_seq(day + 1, misses + 1)

        self.memo[(day, misses)] = attend + miss
        return self.memo[(day, misses)]

    def _count_miss_graduation(self, day: int, misses: int) -> int:
        if (day, misses) in self.memo:
            return self.memo[(day, misses)]

        if misses >= 4:
            return 0

        if day == self.n - 1:
            return 1 if misses < 3 else 0

        attend = self._count_miss_graduation(day + 1, 0)
        miss = self._count_miss_graduation(day + 1, misses + 1)

        self.memo[(day, misses)] = attend + miss
        return self.memo[(day, misses)]

def attendance_probability(n: int) -> str:
    problem = AttendanceProblem(n)
    total_ways, miss_graduation = problem.count_ways()
    return f"{miss_graduation}/{total_ways}"

# Example Usage
if __name__ == "__main__":
    print(attendance_probability(5))  # Expected Output: "14/29"
    print(attendance_probability(10))  # Expected Output: "372/773"
