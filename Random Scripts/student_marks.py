if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

for i in student_marks:
    print(i)
#prints each key on new line


for i in student_marks.items():
    print(i)
#prints a tuple (key, value) on each line

print(sum(student_marks[query_name])/len(student_marks[query_name]))
