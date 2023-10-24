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
        string += f"{factor}^{factor_dict[factor]} * "
    string += "\b\b\b"
    return string


def lcm(num1, num2):
    return (num1 * num2) / gcd(num1, num2)


def direct_proof(num, expr):
    result = ""
    if expr == "If a number is even, then it is divisible by 2.":
        if parity_check(num) == "Even":
            result = f"{num} is indeed an even number since it can be written as 2k where k={num // 2}. As such, by definition, it is divisible by 2, validating the given statement."
        else:
            result = f"Here, {num} is an odd number, which goes against our hypothesis, as well as the conclusion"
    elif expr == "If a number is even, then it is not divisible by 2.":
        if parity_check(num) == "Even":
            result = f"{num} is indeed an even number since it can be written as 2k where k={num // 2}. As such, by definition, it is divisible by 2, which goes against our hypothesis, as well as the conclusion."
        else:
            result = f"Here, {num} is an odd number, which goes against our hypothesis. It does apply to our conclusion though, since our number {num} is not, in fact, divisible by 2."

    return result


def main():
    print(parity_check(25))
    print(prime_checker(17))
    print(gcd(48, 18))
    print(prime_factors(56))
    print(lcm(15, 20))


if __name__ == '__main__':
    main()
