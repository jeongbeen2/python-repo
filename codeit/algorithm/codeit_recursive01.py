def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)  # recursive


countdown(4)