
def f(start,hod=0):
    if hod==13:
        if start <0:
            return {start}
        return set()
    if hod>13:return 0
    return f(start -3,hod+1) | f(start*(-3),hod+1)

f=f(333)
print(len(f))

# dots={333}
# for i in range(13):
#     dots={x-3 for x in dots} | {x*(-3) for x in dots}
# ans=set()
# for i in dots:
#     if i<0:
#         ans|={i}
# print(len(ans))