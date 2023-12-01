# Concurrency in Python

### Introduction to Concurrency in Python

Concurrency is the ability of a program to handle multiple tasks simultaneously. In Python, there are two primary ways to achieve concurrency: multi-threading and multi-processing.

#### Multi-Threading

Multi-threading is a concurrent execution model where multiple threads share the same resources, such as memory space. Threads are lightweight, and they can run concurrently, allowing for better responsiveness and resource utilization. However, Python's Global Interpreter Lock (GIL) limits the execution of multiple threads in a single process, making it challenging to achieve true parallelism.

##### Global Interpreter Lock (GIL)

The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This means that, even in a multi-threaded environment, only one thread can execute Python bytecode at a time.

As a result, the GIL can become a bottleneck in CPU-bound tasks, limiting the performance gain from using multiple threads. However, for I/O-bound tasks, where threads spend a significant amount of time waiting for external resources, the GIL is less of an issue, and multi-threading can still provide benefits.

#### Multi-Processing

Multi-processing, on the other hand, involves running multiple processes concurrently. Each process has its own Python interpreter and memory space, allowing for true parallelism and efficient utilization of multiple CPU cores. Unlike threads, processes do not share memory by default, which can help avoid many concurrency-related issues.


#### Understanding GIL

The Global Interpreter Lock (GIL) can impact the performance of multi-threaded Python programs. When dealing with CPU-bound tasks, consider using multi-processing for better parallelism. For I/O-bound tasks, multi-threading can still provide advantages.

### Conclusion

Concurrency in Python involves managing multiple tasks simultaneously. Understanding the GIL and choosing the appropriate concurrency model based on the nature of the tasks is crucial for optimizing performance. This repository provides examples of both multi-threading and multi-processing in Python, allowing you to explore and compare these concurrency approaches.




## process.py
The `process.py` file contains code related to multiprocessing. It imports the necessary modules and functions such as `Pool`, `time`, `multi_thread` from `thread.py`, and `is_prime` and `DEFAULT_NUMBERS` from `utils.py`. 

The main function in this file is `multi_process()`. It creates a process pool with 4 workers using the `Pool` class. It then uses the `map()` function to parallelize the execution of the `is_prime()` function on the `DEFAULT_NUMBERS` list. Finally, it prints "All processes finished" when all the processes are completed.

## utils.py
The `utils.py` file contains utility functions and variables used by other code files. It imports the necessary modules such as `Pool` from `multiprocessing`, `time`, `multi_thread` from `thread.py`, and `is_prime` and `DEFAULT_NUMBERS` from itself.

The main function in this file is `multi_process()`, which is identical to the one in `process.py`. This function creates a process pool, maps the `is_prime()` function to the `DEFAULT_NUMBERS` list, and prints "All processes finished" when the execution is completed.

## thread.py
The `thread.py` file contains code related to multithreading. It imports necessary modules such as `time`, `threading`, and `queue`, as well as the `is_prime` and `DEFAULT_NUMBERS` from `utils.py`. It also initializes a `Queue` object named `q` for storing numbers.

The file includes two functions: `get_page(number)` and `show_is_prime(worker_id)`. The `get_page(number)` function is responsible for fetching a web page specified by a URL retrieved from the `q` queue.  It handles exceptions that may occur during the request and prints information about completed requests.

The `show_is_prime(worker_id)` function checks if a number from the `q` queue is prime using the `is_prime()` function. It prints information about completed checks.

The `multi_thread()` function is the entry point for multithreading. It populates the `q` queue with numbers from the `DEFAULT_NUMBERS` list. It creates 6 worker threads that execute the `show_is_prime()` function. Once all the tasks in the `q` queue are completed, it prints "threads joined".

## main.py
The `main.py` file serves as the main entry point for the program. It imports necessary modules and functions such as `sys`, `multi_thread` from `thread.py`, `multi_process` from `process.py`, and `is_prime` and `DEFAULT_NUMBERS` from `utils.py`.

The file includes a function called `run_normally()`, which performs a normal execution of the `is_prime()` function on the `DEFAULT_NUMBERS` list.

The program checks if any command-line arguments are provided. If no arguments are provided, it executes the `run_normally()` function. If an argument is provided, it checks if it is `-t` or `-p`. If it is `-t`, it calls the `multi_thread()` function. If it is `-p`, it calls the `multi_process()` function. If no valid argument is provided, it prints "please select one argument at least (-t or -p)".

## Run the Program
To run the program without any command-line arguments, simply execute `main.py`. This will execute the `run_normally()` function on the `DEFAULT_NUMBERS` list.

To run the program with multithreading, execute `main.py -t`.

To run the program with multiprocessing, execute `main.py -p`.

Please ensure that the necessary dependencies are installed before running the program.

Please let me know if you have any further questions! 😊
