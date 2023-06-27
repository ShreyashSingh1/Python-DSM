"""
-> Multi-Threading <-
Multithreading is a programming concept that involves executing
multiple threads concurrently within a single process. A thread
is a lightweight unit of execution that represents a sequence
of instructions. By utilizing multiple threads, a program can
perform multiple tasks simultaneously, improving performance
and responsiveness.
"""

import threading
import urllib.request
import time


# When we have to run a multiple process in one core

def test(id):
    print("Program start %d" % id)


# test(45)

# Ek core hai aur usk under hum multiple thread/program bana rahe hai

thread = [threading.Thread(target=test, args=(i,)) for i in range(1, 11)]
"""Thread, you need to pass them as a tuple. In your code, (i) is not
a tuple, but simply the integer i surrounded by parentheses. To
create a tuple with a single element, you need to include a
trailing comma after the element."""

for t in thread:
    t.start()

print(thread)

print(id(thread))

"""Storing multiple files into files multiple file"""


def file_download(url, filename):
    urllib.request.urlretrieve(url, filename)


file_download('https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt', "test.txt")

url_list = ['https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt',
            'https://raw.githubusercontent.com/itsfoss/text-files/master/sherlock.txt',
            'https://raw.githubusercontent.com/itsfoss/text-files/master/sample_log_file.txt']

file_name_list = ["data1.txt", "data2.txt", "data3.txt"]

"""Eder vo thread bana k  ready  kar diya hai for execution"""
thread1 = [threading.Thread(target=file_download, args=(url_list[i], file_name_list[i])) for i in range(3)]
print(thread1)
"""
[<Thread(Thread-11 (file_download), initial)>, 
<Thread(Thread-12 (file_download), initial)>, 
<Thread(Thread-13 (file_download), initial)>]
"""
# for i in thread1:
#     i.start()

"""
Multithreading in Python refers to the ability of a program to execute multiple 
threads concurrently. A thread is a sequence of instructions that can run 
independently of other threads, allowing for parallel execution and improved 
performance in certain scenarios. Python provides a built-in threading 
module that allows you to work with threads.
"""
def test1(id):
    for i in range(10):
        print(f"test1 {id} printing {i} {time.ctime()}")
        time.sleep(1)

# test1(1)
thread2 = [threading.Thread(target=test1, args=(i,)) for i in range(3)]
# for t in thread2:
#     # t.start()

"""
>> Just because of sleep nhi toh ek shat me pura program run ho jata
Context switching
Resource utilization accha ho jata hai
test1 0 printing 0
test1 1 printing 0
test1 2 printing 0
test1 0 printing 1
test1 2 printing 1
test1 1 printing 1
test1 0 printing 2
test1 1 printing 2
test1 2 printing 2
test1 0 printing 3
test1 1 printing 3
test1 2 printing 3
test1 0 printing 4
test1 1 printing 4
test1 2 printing 4
test1 0 printing 5
test1 1 printing 5
test1 2 printing 5
test1 0 printing 6
test1 1 printing 6
test1 2 printing 6
test1 0 printing 7
test1 1 printing 7
test1 2 printing 7
test1 0 printing 8
test1 1 printing 8
test1 2 printing 8
test1 0 printing 9
test1 1 printing 9
test1 2 printing 9
"""


shared_variable = 0
lock_var = threading.Lock()

def test2(id):
    global shared_variable
    with lock_var:
        """
         The with lock_var statement, also known as a "with statement" or a "context manager," 
         is used to acquire and release a lock in a safe and convenient manner. In this case, 
         it is being used to ensure that only one thread can access the shared_variable at a time.
        """
        shared_variable += 1
        print(f"Test2 id is {id} has increased the shared variable by {shared_variable}")
        time.sleep(1)


thread3 = [threading.Thread(target=test2, args=(i,)) for i in range(3)]
print(thread3)

for i in thread3:
    i.start()
"""
Test2 id is 0 has increased the shared variable by 1
Test2 id is 1 has increased the shared variable by 2
Test2 id is 2 has increased the shared variable by 3
"""
