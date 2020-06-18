

import sys

if __name__ == '__main__':
    number = int(sys.argv[1])
    for i in range(number):
        print("%s %s" %(i, i**2))

