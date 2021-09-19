# importing the threading module
import threading,time


def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    time.sleep(5)
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating thread


    t1 = threading.Thread(target=print_square, args=(10,))
    #t2 = threading.Thread(target=print_cube, args=(10,))
    print_cube(10)
    # starting thread 1
    t1.start()
    # starting thread 2

    # wait until thread 1 is completely executed


    # both threads completely executed
    print("Done!")