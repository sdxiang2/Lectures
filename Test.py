message = "Now this string is something different."
print(message)

def factorial(x):
    f = x
    for i in reversed(range(x)[1:]):
        f = f*i
    return f