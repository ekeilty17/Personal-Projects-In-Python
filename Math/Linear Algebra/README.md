# Linear Algebra Code
This code preforms common operations one would do in a first year linear algebra course such as Gaussian Elimination, checking if a set of vectors are linearly independent, and Change of Basis.

## Matrix
In essense a matrix is just a 2D list. Here are the list of methods associated with the matrix object.

* `.get()`
* `.setRow(r)`
* `.setCol(c)`
* `.deleteRow(r)`
* `.deleteCol(c)`
* `.set(L)`
* `.copy()`
* `.dim()`
* `.isSquare()`
* `.scale(k)`
* `.transpose()`
* `.submatrix()`
* `.Det()`
* `.minor()`
* `.cof()`
* `.cofactor_matrix()`
* `.adj()`
* `.inverse()`

Moreover I can preform operations between matrices such as add, subtract, multiply, and augment.

### Matrix Properties
There are many important types of matrices. The file `matrix_prop.py` contains functions to check or produce special types of matrices.  

## Vector
In essense a vector is just a 1D list. Here are the list of methods associated with the vector object.

* `.get()`
* `.set(L)`
* `.copy()`
* `.dim()`
* `.scale(k)`
* `.magnitude()`
* `.normalize()`

Moreover I can preform operations between vectors such as add, substract, dot product, cross product, angle between, and projection onto.

## Operations between vectors are matrices
The relationship between vectors and matrices are the core of linear algebra. I have a series of functions that convert one object to another and make preforming operations between them much easier.

* `vector_list_to_matrix(L)`
* `matrix_to_list_vectors(A)`
* `vector_to_matrix(v)`
* `matrix_to_vector(A)`
* `matrix_vector_multiply(A, v)`

## Linear Algebra Concepts
Now that I have created the basics, I can implement core concepts in Linear Algebra such as

* Gaussian Elimination
* Checking if vectors are Linearly Independent
* Generating a Change of Basis Matrix and preforming Change of Basis on a Linear Transformation
