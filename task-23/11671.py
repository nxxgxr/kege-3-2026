dots={1}
for i in range(15):
    dots={x+10 for x in dots} | {x-5 for x in dots}
print(len(dots))