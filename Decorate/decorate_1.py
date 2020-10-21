import time


def func1(func):
    def func2(m_time):
        print("func2 is called")
        func(m_time)

    return func2


@func1
def decorate(m_time):
    time.sleep(m_time)
    print("Hello")


decorate(5)
