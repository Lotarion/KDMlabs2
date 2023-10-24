from math import sqrt


def parity_check(number: int) -> str:
    if number % 2:
        return "Odd"
    else:
        return "Even"


def prime_checker(number: int) -> str:
    if number <= 1:
        return "Not prime"
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return "Not prime"
    return "Prime"


def gcd(a: int, b: int) -> int:
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def prime_factors(num: int) -> str:
    def factorize(number, factors_, factor_):
        while number % factor_ == 0:
            number /= factor_
            factors_.append(factor_)
        return number

    factors = []
    num = factorize(num, factors, 2)
    num = factorize(num, factors, 3)

    k = 1
    while num > 1 and k < num:
        p1 = 6 * k - 1
        p2 = 6 * k + 1

        num = factorize(num, factors, p1)
        num = factorize(num, factors, p2)

        k += 1

    factor_dict = {}
    for factor in factors:
        if factor not in factor_dict.keys():
            factor_dict.update({factor: 1})
        else:
            factor_dict[factor] += 1

    string = ""
    for factor in factor_dict.keys():
        string += f"{factor} ^ {factor_dict[factor]} * "
    string += "\b\b\b"
    return string


def main():
    # print(parity_check(25))
    print(prime_factors(54000))


if __name__ == '__main__':
    main()
