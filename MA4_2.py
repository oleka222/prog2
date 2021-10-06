# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:27:08 2021

@author: aleks
"""
from numba import njit
import matplotlib.pyplot as plt
from time import perf_counter as pc
import numpy as np
from integer import Integer

def fib_pure_py(n):
    if n <= 1:
        return n
    else:
        return(fib_pure_py(n-1) + fib_pure_py(n-2))
@njit
def fib_numba_py(n):
    if n <= 1:
        return n
    else:
        return(fib_numba_py(n-1) + fib_numba_py(n-2))
    
def task_4():
    (fig, ax) = plt.subplots()
    time_python = []
    time_numba = []
    time_cpp = []
    for i in range(30, 46):
        #python
        start_p = pc()
        fib_pure_py(i)
        end_p = pc()
        time_python.append(end_p - start_p)
        
        #numba
        start_n = pc()
        fib_pure_py(i)
        end_n = pc()
        time_numba.append(end_n - start_n)
        
        #c++
        start_n = pc()
        f = Integer(i)
        f.fib()
        end_n = pc()
        time_cpp.append(end_n - start_n)
        
    ax.plot(np.linspace(30, 45, num=15), time_python)
    ax.plot(np.linspace(30,45, num = 15), time_numba)
    ax.plot(np.linspace(30,45, num = 15), time_cpp)
    ax.set_ylabel("Time [s]")
    plt.savefig("cpp_numba_python.png")
    
def task_5():   
    time_pure_python = []
    time_numba = []
    #f = Integer(5)
    (fig, ax) = plt.subplots()
    #print(f.fib())
    for i in range(30):
        start = pc()
        fib_pure_py(i+1)
        end = pc()
        start_numba = pc()    
        fib_numba_py(i+1)
        end_numba = pc()
        time_pure_python.append(end - start)
        time_numba.append(end_numba - start_numba)
    ax.plot(np.linspace(1, 30, num=30), time_pure_python)
    ax.plot(np.linspace(1,30, num = 30), time_numba)
    ax.set_ylabel("Time [s]")
    plt.savefig("numba_vs_python.png")
    
def task_6():
    f = Integer(47)
    print(f.fib())
    print(fib_numba_py(47))
    
def main():
    task_4()
    task_5()
    task_6()
if __name__ == "__main__":
    main()