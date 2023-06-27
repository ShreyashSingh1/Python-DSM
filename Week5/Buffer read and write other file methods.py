"""buffer use kar k koi bada file read ya Write karte ho
tab usko chunk me read/write karta hai used in binary data"""
import io
with open("test1.txt", "wb") as f:
    file = io.BufferedWriter(f)
    file.write(b"This is my first line\n")
    file.write(b"This is my second line")
    file.flush()

with open("test1.txt", "rb") as f:
    file = io.BufferedReader(f)
    # 100 bits ka data chayie toh
    print(file.read(100))

"""
The io.BufferedWriter() is like a helper tool that makes writing data more efficient.
When you write data, instead of sending it directly to its destination 
(like a file or network), the BufferedWriter holds onto the data temporarily in a buffer.

Think of it like a container where you can store a bunch of things before actually 
delivering them. Instead of delivering one thing at a time, you can wait until the 
container is full or a certain condition is met, and then deliver everything at once.
This is faster and more efficient.

-> The benefits of using io.BufferedWriter() are: <-
Faster Writing: By collecting data in the buffer and writing it in bigger chunks,
it saves time and makes writing faster overall.

Less Work: Instead of doing many small deliveries, you do fewer large deliveries, 
which reduces the amount of work needed.

Control: You can decide when to send the data from the buffer to its destination. 
You can do it manually or set conditions to automatically send it when it reaches a certain size or condition.

Easy to Use: It's a built-in tool in Python, so you don't have to create it yourself. 
You can use it to write data to files, network connections, or other writable things easily.

In simple terms, io.BufferedWriter() helps make writing data quicker and more efficient by 
collecting it in a temporary container (buffer) and delivering it in larger batches.
"""