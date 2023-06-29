"""Types of error"""
import logging
logging.basicConfig(filename="Exception.log", level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s "
 
                                                                          "%(message)s")
try:
    a = 10/0

except ZeroDivisionError as e:
    logging.error(e)

try:
    a = int("Shreyash")

except (ValueError, TypeError) as e:
    logging.error(e)

try:
    int("Shreyash")

except:
    print("This catch an error")


try:
    import shreyash

except ImportError as e:
    logging.error(e)


try:
    d = {
        "Key": "WWE",
        "key1": "WWF"
    }
    print(d["k"])

except KeyError as e:
    logging.error(e)


try:
    "string".test()

except AttributeError as e:
    logging.error(e)

try:
    l = [1, 2, 4, 3]
    print(l[7])

except IndexError as e:
    logging.error(e)

try:
    123 + "we"

except TypeError as e:
    logging.error(e)


try:
    with open(file="Shreyash.txt", mode="r") as file:
        print(file.read())

except FileNotFoundError as e:
    logging.error(e)
    print("test")

# Super class ko niche rakh
except Exception as e:
    print(e)

def test():
    try:
        with open(file="Shreyash.txt", mode="r") as file:
            print(file.read())

    except FileNotFoundError as e:
        logging.error(e)
        print("test")

    # Super class ko niche rakh
    except Exception as e:
        print(e)

test()