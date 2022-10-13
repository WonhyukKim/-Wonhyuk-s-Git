# 셀프넘버

def d(n) :
    numlist = list(map(int, str(n)))
    num = sum(numlist) + n
    return num

def selfnum() :
    result = [x for x in range(1, 10000)]
    for i in range(1, 10000) :
        num = d(i)
        if num in result :
            result.remove(num)
    for n in result :
        print(n)

selfnum()


