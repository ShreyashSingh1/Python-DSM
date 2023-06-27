"""Logging is the process of keeping a record of important events
or messages that happen when a program or system runs. It helps
developers understand what's going on inside the code and allows
them to find and fix issues more easily.

In software development, logging is similar. It involves writing
down information about what the program is doing, any errors or
problems encountered, and other important details. These "logs"
serve as a history of the program's activities and can be reviewed
later to figure out what went wrong or to understand how the
program is behaving.

Overall, logging is like taking notes or keeping a diary for a
program or system. It's a way to keep a record of what happened,
which helps in understanding and improving the software."""

import logging
print("This is my print")
"""
Its alternative of print
we don't use print generally

-> Levels of logging
1. NOTSET
2. DEBUG
3. INFO
4. WARNING
5. ERROR
6. CRITICAL
"""

"""Setting basis config"""
logging.basicConfig(filename="test.log", level=logging.INFO)

logging.info("Log this line of execution")

logging.info("This is my print")

# It won't update/log as it is present at a higher level
logging.debug("This is my message")

logging.warning("This is my warning message")

logging.error("This is my error")

logging.critical("This is my critical message")

logging.shutdown()

logging.basicConfig(filename="test1.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
# "%(acstime)s %(message)s" -> % click time % message s = string

logging.info("This is my info logging")

logging.error("This is my error")

logging.critical("This is my critical message")

logging.shutdown()

logging.basicConfig(filename="test2.log", level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")

logging.info("This is my info logging")

logging.error("This is my error")

logging.critical("This is my critical message")

logging.shutdown()


logging.basicConfig(filename="implement.log", level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s")

l = [1, 2, 3, 34, 4, [2, 3, 4, "shreyash"], "Shreyash", "Singh"]
l1_num = []
l1_str = []
for i in l:
    logging.info(f"We are iterating through our list {l} and our local variable is i")
    if type(i) == list:
        logging.info("I am inside if statement and i am trying ro check list type ")
        for j in i:
            logging.info("I am in side another for loop list inside list element")
            if type(j) == int:
                l1_num.append(j)
            if type(j) == str:
                l1_str.append(j)

    if type(i) == str:
        logging.info("I am inside another if check for str data type")
        l1_str.append(i)

    if type(i) == int:
        l1_num.append(i)

print(l1_num)
print(l1_str)
logging.info(f"This is int list: {l1_num}")
logging.info(f"This is str list: {l1_str}")

logging.shutdown()
