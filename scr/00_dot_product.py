import numpy as np


def init_2_vectors(length):
    a = np.random.rand(length)
    b = np.random.rand(length)
    return a, b


def for_loop_dot_product(a, b):
    dot_product = 0
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    return dot_product


def comprehension_list_dot_product(a, b):
    return sum(a_i*b_i for a_i, b_i in zip(a, b))


def BLAS_dot_product(a, b):
    return np.dot(a, b)


if __name__ == '__main__':
    from time import time

    length = 10**7

    a, b = init_2_vectors(length)

    t0 = time()
    print(
        '\n\tdot =', for_loop_dot_product(a, b),
        f'\n\tFor loop runtime: {round(time()-t0, 3)}'
    )

    t0 = time()
    print(
        '\n\tdot =', comprehension_list_dot_product(a, b),
        f'\n\tComprehension list loop runtime: {round(time()-t0, 3)}'
    )

    t0 = time()
    print(
        '\n\tdot =', BLAS_dot_product(a, b),
        f'\n\tNumPy (BLAS): {round(time()-t0, 3)}\n'
    )
