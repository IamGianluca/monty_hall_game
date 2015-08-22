import numpy as np
import random

class Door(object):
    def __init__(self, name):
        self.name = name

def main():
    a = Door("A")
    b = Door("B")
    c = Door("C")

    doors = [a, b, c]
    doors.remove(a)
    print(doors.__contains__(a))
    to_exclude = random.choice(doors)
    print(to_exclude.name)
    # to_exclude
    # # remaining_doors = np.delete(doors, to_exclude)
    # print(remaining_doors)

if __name__ == "__main__":
    main()