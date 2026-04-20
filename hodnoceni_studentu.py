from itertools import count


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.get_by_index(index)
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"
    def find(self, score_count):
        indexes = []
        count = 0
        for i, j in enumerate(self.scores):
            if j == score_count:
                indexes.append(i)
        return indexes
    def get_sorted(self):
        scoress = self.scores.copy()
        for _ in range(len(scoress)):
            for i in range(len(scoress)):
                try:
                    if scoress[i] > scoress[i + 1]:
                        scoress[i], scoress[i + 1] = scoress[i + 1], scoress[i]
                except:
                    continue
        return scoress
    def average(self):
        return sum(self.scores)/len(self.scores)
    def best(self):
        return max(self.scores)
    def worst(self):
        return min(self.scores)
    def pass_rate(self):
        count = 0
        for i in self.scores:
            if i  >= 50:
                count += 1
        return count / self.count()

    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"
results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())  # 9
print(results.get_by_index(2))  # 91
print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
print(results.get_grade(4))
print(results.find(67))
print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
print(results.average())
print(results.pass_rate())
print(results)