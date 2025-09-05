def fact(a):
    if a < 0:
        return -1
    elif a == 0:
        return 1
    else:
        t = 1
        for i in range(2, a):
            t *= i
        return t

def multi(a, b):
    c = a ** b
    return c

def floating(a, b):
    if a or b == 0:
        return 0
    else:
        c = a // b
        return c

def test1_fact():
    expect = 24
    got = fact(5)
    assert expect == got

def test2_fact():
    expect = 120
    got = fact(5)
    assert expect == got

def test3_fact():
    expect = 24
    got = fact(-4)
    assert expect == got

def test4_fact():
    expect = 0
    got = fact(0)
    assert expect == got

def test5_fact():
    expect = -1
    got = fact(-5)
    assert expect == got

def test1_multi():
    expect = 32
    got = multi(2, 5)
    assert expect == got

def test2_multi():
    expect = 12
    got = multi(3, 2)
    assert expect == got

def test3_multi():
    expect = 12
    got = multi(-2, 5)
    assert expect == got

def test4_multi():
    expect = 0
    got = multi(0, 0)
    assert expect == got

def test5_multi():
    expect = 9
    got = multi(-3, 2)

def test1_floating():
    expect = 4
    got = floating(12, 3)
    assert expect == got

def test2_floating():
    expect = 5
    got = floating(15, 3)
    
def test3_floating():
    expect = 4
    got = floating(-5, 2)

def test4_floating():
    expect = 0
    got = floating(0, 0)

def test5_floating():
    expect = -5
    got = floating(-15, 3)
