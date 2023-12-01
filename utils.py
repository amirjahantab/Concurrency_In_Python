def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            return False
    print(f"{n} is prime")
    return True

DEFAULT_NUMBERS = [10000019, 10000079, 10000103, 13422108, 10,\
    7, 91, 10000259] * 10