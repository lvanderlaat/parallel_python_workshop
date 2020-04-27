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
