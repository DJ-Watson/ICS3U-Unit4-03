#!/usr/bin/env python3

# Created by DJ Watson
# Created on October 2019
# this program loops a number and sends the square for each number


def main():
    loopn = 0
    answer = 0

    # input
    intc = input("enter number: ")
    print("")

    # process and output
    try:
        numinput = int(intc)
        if numinput > 0:
            for loopn in range(numinput + 1):
                answer = loopn**2
                print("{}² = {}" .format(loopn, answer))
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
