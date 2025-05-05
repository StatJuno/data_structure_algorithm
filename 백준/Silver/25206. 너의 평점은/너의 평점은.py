grade_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
point_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0
    
for i in range(20):
    name, unit, grade = input().split()
    unit = float(unit)
    if grade != 'P':
        total += unit
        result += unit * point_list[grade_list.index(grade)]

print('%.6f'%(result/total))

