from itertools import count


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
        self._sorted_scores = None

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

    def find_sorted(self, score):
        if self._sorted_scores is None:
            self._sorted_scores = self.get_sorted()
        k = self._sorted_scores
        start = 0
        end = len(k) - 1
        print("Sorting...")
        while start <= end:
            stred = (start + end) / 2
            if k[round(stred)] == score:
                print("Sorted")
                return round(stred), score
            elif k[round(stred)] < score:
                start = stred + 1
            elif k[round(stred)] > score:
                end = stred - 1
        print("None")
        return None

