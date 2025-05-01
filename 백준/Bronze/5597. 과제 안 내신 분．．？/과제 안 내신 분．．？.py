student = list(range(1,31))

for i in range(28):
    submission = int(input())
    student.remove(submission)

for j in student:
    print(j)