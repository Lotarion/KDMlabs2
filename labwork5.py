def linear_func_calc(x: int, k: int = 1, b: int = 0):
    return (k * x) + b


def dot_list_to_dot_dict(dot_list):
    dot_dict = dict()
    for pair in dot_list:
        dot_dict[pair[0]] = pair[1]
    return dot_dict


def domain_range_identifier(dot_list):
    dot_dict = dot_list_to_dot_dict(dot_list)
    return [set(dot_dict.keys()), set(dot_dict.values())]


def parity_checker(dot_list):
    dot_dict = dot_list_to_dot_dict(dot_list)
    count = 0
    count_even = 0
    count_odd = 0
    for x in dot_dict.keys():
        if -x in dot_dict.keys():
            count += 1
            if dot_dict[x] == dot_dict[-x]:
                count_even += 1
            if dot_dict[x] == -dot_dict[-x]:
                count_odd += 1
    if count == 0:
        return "Neither odd nor even"
    elif count_even == count:
        return "Even"
    elif count_odd == count:
        return "Odd"
    else:
        return "Neither odd nor even"


def is_injective(dot_list):
    dot_dict = dot_list_to_dot_dict(dot_list)
    if len(set(dot_dict.keys())) > len(set(dot_dict.values())):
        return False
    else:
        return True


def is_surjective(dot_list: list, codomain: set):
    dot_dict = dot_list_to_dot_dict(dot_list)
    for y in codomain:
        if not (y in dot_dict.values()):
            return False
    return True


def main():
    print(linear_func_calc(4, 2, 3))
    raw_out = domain_range_identifier({(1, 2), (3, 6), (4, 8)})
    print("Domain: {}\nRange: {}".format(raw_out[0], raw_out[1]))
    print("Function type: " + parity_checker([(-1, 1), (0, 0), (1, 1)]))
    print(is_injective([(2, 4), (3, 6), (4, 8)]))
    print(is_surjective([(1, 2), (2, 3), (3, 4)], {2, 3, 4}))


if __name__ == "__main__":
    main()
