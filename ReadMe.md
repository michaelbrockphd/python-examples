# Python Practice

Small repo holding my Python port-folio.  The repo basically has two root folders:
* **modules** - where the Python code exists, and
* **modules_test** - where all unit tests (helped along with [parameterized](https://github.com/wolever/parameterized) is held.

## Modules

Each module is described below - but at the time is mostly just a port of my [matrix Golang module](https://github.com/michaelbrockphd/golang-example/tree/master/matrix).

* **matrix**
    * Holds all interfaces and custom exception class used by the other modules.
    * Home to Matrix, MatrixSegment, and ArgumentException

* **matrix_computed**
    * Holds the computed version of MatrixSegment as well as ComputedIdentityMatrix.
    * In short, these implementations try to reduce memory usage by computing the bounds of an identity matrix and returning either zero or the identity value when queried.

* **matrix_concrete**
    * (Still to be developed and tested)
    * Holds the concret implementations, RowAlignedMatrix and ColumnAlignedMatrix.
    * Both are adapters to LinearMatrix as underneath all elements are kept in a single demensional array.

* **matrix_opeartions**
    * (Still to be developed and tested)
    * Holds all other operations that can be carried out on a matrix.
    * Currently holds methods for matrix initialization and matrix multiplication.
