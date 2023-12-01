# Code Descriptions

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
