# main.py
import mymath
import timeit


def py_sum_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


def main():
    n = 10_000_000

    py_time = timeit.timeit(lambda: py_sum_squares(n), number=5)
    cpp_time = timeit.timeit(lambda: mymath.sum_squares(n), number=5)

    print(f"Python: {py_time:.4f}s")
    print(f"C++:    {cpp_time:.4f}s")

    print(f"Speedup: {py_time / cpp_time:.1f}x")


if __name__ == "__main__":
    main()