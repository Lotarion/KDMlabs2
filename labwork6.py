def is_reflexive(input_set: set, input_relation: set) -> bool:
    for i in input_set:
        if (i, i) not in input_relation:
            return False
    return True


def is_symmetric(input_relation: set) -> bool:
    for i, j in input_relation:
        if (j, i) not in input_relation:
            return False
    return True


def is_transitive(input_relation: set) -> bool:
    for i, j in input_relation:
        for m, n in input_relation:
            if j == m:
                if (i, n) not in input_relation:
                    return False
    return True


def is_equivalence_relation(input_set: set, input_relation: set) -> bool:
    refl = is_reflexive(input_set, input_relation)
    symm = is_symmetric(input_relation)
    tran = is_transitive(input_relation)
    return all([refl, symm, tran])


def reverse_relation(input_relation: set) -> set:
    result_relation = set()
    for i, j in input_relation:
        result_relation.add((j, i))
    return result_relation


def main():
    print(is_reflexive({1, 2, 3}, {(1, 1), (2, 2), (3, 3)}))
    print(is_symmetric({(1, 2), (2, 1), (3, 3)}))
    print(is_transitive({(1, 2), (2, 3), (1, 3)}))
    print(is_equivalence_relation({1, 2, 3}, {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)}))
    print(reverse_relation({(1, 2), (3, 4), (5, 6)}))


if __name__ == "__main__":
    main()
