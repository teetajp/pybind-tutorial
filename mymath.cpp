#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

double sum_squares(int n) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i) {
        sum += i * i;
    }
    return sum;
}

PYBIND11_MODULE(mymath, m) {
    m.doc() = "A simple math module"; // Optional module docstring
    m.def("add", &add, "A function that adds two numbers");
    m.def("sum_squares", &sum_squares, "A function that calculates the sum of squares of the first n natural numbers");
}