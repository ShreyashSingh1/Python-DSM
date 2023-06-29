"""
Multi-Processing
Multiprocessing refers to the simultaneous execution of multiple
processes or tasks on a computer system with multiple processors
or processor cores. It is a technique used to improve the performance
and efficiency of a system by dividing the workload among multiple
processing units.
"""

import multiprocessing

"""PROCESS"""
def test():
    print("This my multiprocessing program")

test()

"""
The if __name__ == "__main__": condition is used in Python to
differentiate between a script being run directly and a script being
imported as a module.


main program will invoke all the resources/interpreter/compiler
"""

"""This is my main process"""
if __name__ == "__main__":
    """This is my child process"""
    m = multiprocessing.Process(target=test)
    """
    The multiprocessing.Process() class allows you to create
    and manage separate processes in Python.

    It will create a child process that executes the test
    function concurrently with the main process.
    The child process will print "This is my
    multiprocessing program," while the main process will
    print "This is main." The main process will wait for
    the child process to complete using m.join() before
    exiting.
    """
    print("This is main")

    # To start a child process
    m.start()

    # Wait until child process terminates
    m.join()


"""POOL"""
def square(n):
    return n**2

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        """
        The multiprocessing.Pool(processes=4) line creates a pool of
        worker processes with the specified number of processes set to 4.
        This means that the Pool object will manage a pool of four worker
        processes to execute the tasks.

        The pool.map(square, [1, 2, 3, 4, 4, 5, 5, 6, 7]) line is where
        the parallelization happens. The map function applies the square
        function to each item in the iterable [1, 2, 3, 4, 4, 5, 5, 6, 7]
        using the worker processes in the pool. It divides the input into
        chunks and distributes them across the available processes.

        By using multiprocessing.Pool and the map function, you can take
        advantage of multiple processes to compute the squares of the
        numbers simultaneously, potentially improving performance compared
        to a sequential execution.
        """
        out = pool.map(square, [1, 2, 3, 4, 4, 5, 5, 6, 7])
        print(out)


"""QUEUE"""
def producer(q):
    for i in range(10):
        q.put(i)

def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    """Ek function() nikal raha hai to dusra daal raha hai in this way
    multiprocessing is been done

    A Queue in multiprocessing is a synchronized data structure used
    for interprocess communication. It allows multiple processes to
    safely exchange data by putting items into the queue and retrieving
    them later.
    """
    m1 = multiprocessing.Process(target=producer, args=(queue,))
    m2 = multiprocessing.Process(target=consume, args=(queue,))
    queue.put("Shreyash")
    m1.start()
    m2.start()
    m1.join()
    m2.join()


"""ARRAY"""
def square(index, value):
    value[index] = value[index] ** 2

if __name__ == "__main__":
    """
    The type code 'i' indicates that the array will contain signed integers.
    The initial values provided in the iterable [1, 2, 3, 4, 5, 6, 7, 8, 9] will
    be used to initialize the shared array.

    created a shared array that can be accessed and modified by multiple processes
    simultaneously.
    """
    arr = multiprocessing.Array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
    # The array created is shared between all the processors
    process = []
    for i in range(9):
        m = multiprocessing.Process(target=square, args=(i, arr))
        process.append(m)
        m.start()
    for m in process:
        # print(m)
        m.join()
    print(list(arr))



"""PIPE"""

"""
A pipe is a mechanism for inter-process communication (IPC) that
allows processes to exchange data. It consists of a read end and
a write end. Data written to the write end can be read from the
read end by another process. Pipes are typically unidirectional
but can be used bidirectionally by using two pipes.

But here duplex is true you and send and receive together from both sides

The multiprocessing.Pipe() function in Python's multiprocessing module is
used to create a duplex (two-way) connection between two processes.
It returns a pair of connection objects that represent the two ends of the pipe.

In a duplex pipe, both ends can send and receive data, allowing for bidirectional
communication between the processes. Each connection object returned by
Pipe() has its own send() and recv() methods to facilitate sending and
receiving data.

In Python, the multiprocessing module provides the Pipe class for creating pipes.
The send method is used to write data to the pipe, and the recv method
is used to read data from the pipe. Pipes are commonly used when multiple
processes need to communicate and share data.
"""

def sender(conn, msg):
    for i in msg:
        conn.send(i)
    conn.close()

def receive(conn):
    while True:
        try:
            msg = conn.recv()
            # conn.send(msg)
        except Exception as e:
            print(e)
            break
        print(msg)

if __name__ == "__main__":
    msg = ["Shreyash", "Manoj", "Singh"]
    """Returns two connection object connected by pipe eg. Whatsapp message"""
    parent_conn, child_conn = multiprocessing.Pipe(duplex=True)
    m1 = multiprocessing.Process(target=sender, args=(child_conn, msg))
    m2 = multiprocessing.Process(target=receive, args=(parent_conn,))
    m1.start()
    m2.start()
    m1.join()
    child_conn.close()
    m2.join()
    parent_conn.close()
