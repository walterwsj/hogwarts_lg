def func1(func):
    def func2():
        func()
        print("This is func2()")
    return func2

@func1
def de_decorateion():
    print("This is de_decoration and func2 will be auto called later")

de_decorateion()