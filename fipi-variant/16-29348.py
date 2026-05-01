def f(n):
    if n<247_500:return 1
    return (n+3) * f(n-3)
print((f(247563)/519 -477*f(247560)) / f(247557))