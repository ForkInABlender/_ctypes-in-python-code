# _ctypes-in-python-code
This repo is made public in case any of the examples are valuable. 

This is for python developers looking to transition their c++ code to python.

Most of the code will be example code for how to transition by hand. This repo will be updated as well as have new bits added on a semi-regular basis.

# the goal?
The goal is to provide things that represent c++ like objects, types, and so on to use any binary regardless of architecture or operating system or execution environment. (that includes the browser using brython.js & not pyodide where all the logic is hidden away or compiled down)

The point for this type of compatibility is that the code then no longer needs to be compiled. But if the code is compiled, we should be able to meet the needs of that compiled library. 
