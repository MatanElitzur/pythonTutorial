# pythonTutorial

## Create a Python Enviornment
1. which python3 --> in the command line will display your current python env, a result example: /usr/local/bin/python3
This is not good I would like to work on a virtual enviornment
    1. in visual studio code  Shift + Command + P, choose "Python: Create Enviornment..." Choose .venv option and then choose the python Version.
    On the explorer in the left side you will see a .venv folder.
    At the visual studio at the upper pane, Choose Terminal --> New Terminal
    If you will type again which python3 the result will be the new path to our env enviornment /Users/I044184/matans_playground/pythonTutorial/.venv/bin/python3
2. python3 -m venv <'virtual environment name'> --> create a virtual environment
       For example:
       1. python3 -m venv test-env

## Modules
1. install a Python package via terminal, Example: pip3 install pytest-benchmark

## Tests
1. Execute tests in terminal: pytest, will execute all function that start with test_
2. python3 -m unittest tests.unit.unit_test_runner  --> run the unittest module as a script and the module path where the unit tests are defined. Execute where tests folder exists.

## Profilers
1. Profile module execute: python3 -m profile sum_loop.py --> To test performance, but the module profile has a slow performance
2. cProfile module execute: python3 -m cProfile sum_loop.py --> To test performance
3. Line_profiler --> **pip install line_profiler** --> display specific lines and their time
   1. https://kernprof.readthedocs.io/en/latest/
   2.  decorate the function with @profile
   3.  Execute in the terminal 'kernprof -lvr "NameOfPythonFile.py"'
   4.  Or Execute in terminal "python3 -m kernprof -lvr large_function.py"
   5.  The result is displayed and a file is created by the name "NameOfPythonFile.py.lprof" 
   6.  To vire details run: python3 -m line_profiler -rtmz "NameOfPythonFile.py.lprof"
4. Py-spy - Can profile multithreading applications.
5. Scalene
6. Yappi
7. Memory_profiler --> pip install memory_profiler --> display the memory usgae
   1. Execute "python3 -m memory_profiler memory_intensive.py"
   2. Generate plots to show memory consumption
      1. Requires matplotlib (We get it with Memory_profiler module)
      2. Usage:
         1. Run: mprof run file.py
         2. Run: mprof plot --output file.jpg
         3. 
## Plots   
1. Display the performence output:
    1. pip3 install matplot
      1. Usage: "mprof run "fileName.py"  Example: "mprof run memory_intensive.py" (Saving profiling data into a new file)
         1. Output: mprofile_20240417171129.dat
      2. mprof plot --output memory_intensive.jpg --> a file is created memory_intensive.jpg
   1. Snakeviz "pip install snakeviz" --> Visualize cProfile output, it is interactive Browser-based
   2. Usgae: "python3 -m cProfile -o file.prof file.py" -o for output file
      1. Example: "python3 -m cProfile -o file.prof sum_loop.py"
      2. Execute snakeviz file.prof --> it will display the result in the browser

## Packages
1. pip install numpy --> for arrays of numbers, the performance is better then a regular array
2. pip install -r requirements.txt  --> Install packages mentioned in file.

## Packaging
1. https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#distributing-packages
   
## Interpreters
1. CPython --> is the official interpreter it is written in C
   1. Execute a python file example: python3 file_name.py
2. PyPy --> Execute Python code faster hten CPython, it is using Just-In-Time compiler
   1. Execute a python file example: pypy3 file_name.py
3. Cython --> Compiles Python code into C code, Will get extra performance and you can't run this code with CPython
4. Jython --> Implemented in Java and it integrates with other Java code
5. Pyson --> aims to be fast and highly compatible Python

## Time
1. time python3 threads.py --> Adding time will give us the following example output
   1. real    0m1.953s  --> The execution time, so we can check it we improved with multi threding or not
      user    0m0.055s
      sys     0m0.057s
## Sample Python Project
1. https://github.com/pypa/sampleproject
