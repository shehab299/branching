def pow(x,y)
{
    return x**y
}


def add(x,y)
{
    return x+y
}


def mul(x,y)
{
    return x*y
}


def calculator(x,y,fun)
{
    return fun(x,y)
}

def calc(x,y ,ch)
{
    if(ch == 'a')
        return add(x,y)
    elif(ch == 'm')
        return mul(x,y)
    elif(ch == 'p')
        return pow(x,y)
}