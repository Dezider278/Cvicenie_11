from sorting import selection_sort
from sorting import random_numbers
from sorting import bubble_sort
from hodnoceni_studentu import StudentsGrades
# print(selection_sort([5, 1, 4, 2, 8]))
# print(selection_sort(random_numbers(20)))
# print(bubble_sort([5, 1, 4, 2, 8]))
# print(bubble_sort(random_numbers(20)))
results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
N = results.count()
print(results)
print(f"Pocet studentov {results.count()}")
for i in range(N):
    print(f"Student {i} : {results.get_by_index(i)} points - {results.get_grade(i)}")
print(f"Index studenta(ov) s plnym poctom: {results.find(100)}")
print(f"Zoradene znamky: {results.get_sorted()}")
from sorting import random_numbers

results = StudentsGrades(random_numbers(30, 0, 100))
print(results.count())

for i in range(N):
    print(f"Student {i} : {results.get_by_index(i)} points - {results.get_grade(i)}")
print(f"Index studenta(ov) s plnym poctom: {results.find(100)}")
print(f"Zoradene znamky: {results.get_sorted()}")
