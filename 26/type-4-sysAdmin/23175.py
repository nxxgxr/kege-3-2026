with open(r'../files/26_2_23175.txt') as file:
    n, m = map(int, file.readline().split())
    gruz = [int(file.readline()) for i in range(n)]
    containers = [int(file.readline()) for i in range(m)]
containers = sorted(containers)
loads = sorted(gruz)
loaded = []
last_containers = 0
for load in loads:
    for container in containers:
        if container - load >= 0:
            loaded += [load]
            last_containers = container
            containers.remove(container)
            break
loaded=loaded[:-1]
for load in loads[::-1]:
    if last_containers - load>=0:
        loaded+=[load]
        break
print(len(loaded),loaded[-1]- loaded[-2])

