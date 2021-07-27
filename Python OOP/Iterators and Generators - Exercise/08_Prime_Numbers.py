def get_primes(integers_list):
    for i in integers_list:
        if is_prime(i):
            yield i


def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
