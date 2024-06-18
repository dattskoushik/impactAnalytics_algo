from typing import List

class AttendanceProblem:
    def __init__(self, n: int):
        self.n = n

    def generate_sequences(self) -> List[str]:
        sequences = []
        self.backtrack_seq("", sequences)
        return sequences

    def backtrack_seq(self, current: str, sequences: List[str]):
        if len(current) == self.n:
            sequences.append(current)
            return None
        self.backtrack_seq(current + "A", sequences)
        self.backtrack_seq(current + "M", sequences)

    def is_valid(self, sequence: str) -> bool:
        return 'MMMM' not in sequence

    def count_valid_sequences(self) -> int:
        sequences = self.generate_sequences()
        valid_sequences = [seq for seq in sequences if self.is_valid(seq)]
        return len(valid_sequences)

    def count_miss_graduation(self) -> int:
        sequences = self.generate_sequences()
        valid_sequences = [seq for seq in sequences if self.is_valid(seq)]
        miss_graduation_sequences = [seq for seq in valid_sequences if seq[-1] == 'M']
        return len(miss_graduation_sequences)

def attendance_probability(n: int) -> str:
    problem = AttendanceProblem(n)
    total_ways = problem.count_valid_sequences()
    miss_graduation = problem.count_miss_graduation()
    return f"{miss_graduation}/{total_ways}"

# Example Usage
if __name__ == "__main__":
    print(attendance_probability(5))  # Expected Output: "14/29"
    print(attendance_probability(10))  # Expected Output: "372/773"
