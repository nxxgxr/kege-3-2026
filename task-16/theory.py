ans = [0] * 2030
ans[2026] = 2026
ans[2025] = 2025
for i in range(2024, 0, -1):
    ans[i] = ans[i + 1] - ans[i + 2] + 7

print(ans[15] - ans[24])

