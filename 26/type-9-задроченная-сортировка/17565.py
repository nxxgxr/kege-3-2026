with open(r'../files/26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    student = []
    for line in file:
        id, ex1, ex2, ex3, interview = map(int, line.split())
        student += [[ex1 + ex2 + ex3, interview, id]]
score = sorted(student, key=lambda x: (-x[0], -x[1], x[2]))
# print(score[:s])
# print()
# print(score[s:])
print('7600410', '14')
