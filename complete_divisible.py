def  proper_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    print(divisors)

proper_divisors(10)