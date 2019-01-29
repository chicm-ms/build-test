import sys
import time

def my_func():
    print('hello!!!!!!!!')

if __name__ == "__main__":
    print('hello')
    for _ in range(5):
        sys.stdout.write('_')
        sys.stdout.flush()
        #time.sleep(1)