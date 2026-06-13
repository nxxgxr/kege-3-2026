with open(r'../files/26_15_23259.txt') as file:
    n, m = map(int, file.readline().split())
    m_child = [int(file.readline()) for i in range(n)]
    m_sanok = [int(file.readline()) for i in range(m)]
m_child = sorted(m_child)
m_sanok = sorted(m_sanok)
massa = []
last_maxx = 0

for i in range(0,len(m_child)-1,2):
    ves=m_child[i] + m_child[i+1]
    for maxx in m_sanok:
        if ves <= maxx:
            massa += [ves]
            m_sanok.remove(maxx)
            last_maxx = maxx
            break
massa = massa[:-1]
ans=[]
for child1, child2 in zip(m_child[::-1], m_child[::-1][1:]):
    if last_maxx - child2 - child1 >= 0:
        massa += [child1 + child2]
        break
print(len(massa), max(massa))
