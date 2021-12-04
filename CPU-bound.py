import time
from hashlib import md5
from random import choice
import concurrent
import concurrent.futures

ZEROS = [
    "0",
    "00",
    "000",
    "0000",
    "00000",
    "000000"]


def getMon(zeros):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith(zeros):
            print(s, h)
            break


if __name__ == '__main__':
    result = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=61) as executor:
        result = executor.map(getMon, ZEROS)

    for r in result:
        print(r)
