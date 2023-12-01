import sys
from thread import multi_thread
from process import multi_process
from utils import DEFAULT_NUMBERS, is_prime


def run_normally():
    for num in DEFAULT_NUMBERS:
        is_prime(num)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        run_normally()
    else:
        try:
            if sys.argv[1] == '-t':
                multi_thread()  
            elif sys.argv[1] == '-p':
                multi_process()
        except IndexError:
            print("please select one argument at least(-t or -p) \n")
        