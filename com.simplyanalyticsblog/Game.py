import random
import re


class Door(object):

    """
    A door in the Monty Hall game show Let's Make A Deal
    """

    def __init__(self, name, hasprize=False):
        self.hasPrize = hasprize
        self.name = name


class Contender(object):

    """
    The contender in the Monty Hall game
    """

    def __init__(self, initialGuess):
        self.guess = initialGuess

    def second_stage_decision(self, remainingContenderDoor):
        if random.choice('yn') == 'y':
            print("GR: Well Monty, I know that switching door I would increase my chances to win, so YES I'll change my initial pick")
            Contender.switch_door(self, remainingContenderDoor)

    def switch_door(self, remainingContenderDoor):
        self.guess = remainingContenderDoor
        print("GR: Monty, my new pick is door", self.guess)


class MontyHall(object):

    """
    Monty Hall himself!!
    """

    def open_door(self, doorWithoutPrize):
        print("MH: I can tell you behind door", doorWithoutPrize, "there isn't any prize")
        print("MH: Would you like to maintain your first pick or change it?")

    def tell_final_result(self, contenderFinalGuess, rightDoor):
        if contenderFinalGuess == rightDoor:
            print("MH: Congratulation, you just won a brand new car!!")
        else:
            print("MH: What a pity! The final prize was behind door", rightDoor)


def main():

    """
    Let's Make A Deal show
    """

    a = Door("A", False)
    b = Door("B", False)
    c = Door("C", True)

    """Hide the prize behind one of the doors and let the contender make his first pick"""
    doors = "ABC"
    rightDoor = random.choice(doors)
    contender = Contender(random.choice(doors))
    monty = MontyHall()

    """Print right door and contender first choice"""
    print("The prize is behind door:", rightDoor)
    print("The contender chose door:", contender.guess)

    """
    Here is where things start getting interesting. There are two scenarios:
    1) The contender got it right on his first pick, so MH will have the choice of open one of the
         two remaining doors
    2) The contender got it wrong on his first pick, so MH will have to open the only remaining door
         which doesn't hide the final prize
    """
    firstStageRemainingDoors = re.sub(contender.guess, '', doors)
    filter = ''.join(['[', rightDoor, contender.guess, ']'])
    remainingDoorsWithoutPrize = re.sub(filter, "", doors)
    doorToOpen = random.choice(remainingDoorsWithoutPrize)
    remainingContenderDoor = re.sub(doorToOpen, "", firstStageRemainingDoors)

    """
    Second stage of the game. MH will open one of the two remaining doors and the contender will have to
      decide if maintaining his/her first pick or switching door
    """
    monty.open_door(doorToOpen)
    contender.second_stage_decision(remainingContenderDoor)

    """A lot of suspense before MH will tell the audience the final result. Will the contended win the car??"""
    monty.tell_final_result(contender.guess, rightDoor)


if __name__ == "__main__":
    main()
