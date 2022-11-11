x = None
y = None

def init(a,b):
    global x
    global y
    x = int(a)
    y = int(b)


def summa():
    result = x + y
    return result


def diff():
    result = x - y
    return result


def mult():
    result = x * y
    return result


def div():
    result = x / y
    return result