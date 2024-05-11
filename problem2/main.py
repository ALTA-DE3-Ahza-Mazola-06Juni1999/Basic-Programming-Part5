def pow(x, n):
    if x == 0:
        return 0
    
    if n == 0:
        return 1

    result = 1
    if n > 0:
        for i in range(n):
            result *= x
    else:  # n < 0
        for i in range(-n):
            result *= 1 / x

    return result


if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125