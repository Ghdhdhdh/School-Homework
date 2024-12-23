def factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def is_prime(num):
    if len(factors(num)) == 2:
        return True
    else:
        return False
    
def lowest_common_multiple(num1:int,num:int):
    iters = 200
    num1_mul = []
    num2_mul = []
    # Get iters amount of multiples
    for i in range(num1, (num1*iters)+1, num1):
        num1_mul.append(i)
    for i in range(num, (num*iters)+1, num):
        num2_mul.append(i)

    for num in num1_mul:
        if num in num2_mul:
            return num

    

