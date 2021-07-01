# https://www.geeksforgeeks.org/how-to-make-a-python-program-wait/

# First import time module.
import time

def wait():
    # immediately prints the following.
    print("Printed immediately.")
    time.sleep(5.5)

    # delays the execution
    # for 5.5 secs.
    print("Printed after 5.5 secs.")

if __name__ == '__main__':
    wait()