# Python Practice

Small repo holding my Python port-folio.  The repo basically has three root folders:
* **modules** - where the Python code exists, and
* **modules_test** - where all unit tests (helped along with [parameterized](https://github.com/wolever/parameterized) is held.
* **moudles_demos** - simple demonstration module(s) to see the classes in action (and not just yay or nay from unit tests).

## Modules

Each module is described below - but at the time is mostly just a port of my [matrix Golang module](https://github.com/michaelbrockphd/golang-example/tree/master/matrix).

* **matrix**
    * Holds all interfaces and custom exception class used by the other modules.
    * Home to Matrix, MatrixSegment, and ArgumentException

* **matrix_computed**
    * Holds the computed version of MatrixSegment as well as ComputedIdentityMatrix.
    * In short, these implementations try to reduce memory usage by computing the bounds of an identity matrix and returning either zero or the identity value when queried.

* **matrix_concrete**
    * Holds the concret implementations, RowAlignedMatrix and ColumnAlignedMatrix.
    * Both are adapters to LinearMatrix as underneath all elements are kept in a single demensional array.

* **matrix_operations**
    * Currently holds methods for matrix matrix multiplication.

* **matrix_initializers**
    * As the name implies, it holds initializer classes to put newly created matrixes into a required state.

## Testing

All unit tests can be found in **modules_test** and there is one file for each module.  Invocation is the same as any other Python module, an example is below for testing the computed module.

```
$ cd path/to/modules_test
$ python3 -m unittest -v matrix_computed_test
```

It was planned to be as extensive as possible but I found myself stuck on learning the various Python unit test frameworks.  In the end, I adopted to get as many tests as I could and then made a demo module instead.  I wanted to avoid a repeat of what happened with AWS and Cognito.

## Demonstration Modules

This project has a modules_demos folder where it holds (currently) a single module to demonstrate the classes in action.

In short, it simply creates and prints to the screen various types of matrix and prints two demonstrations at the end where matrix multiplication is carried oout.

```
$ cd path/to/modules_demos
$ python3 matrix_concrete_demo.py
```
