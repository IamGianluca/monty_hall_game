import random
import re


class Door(object):

    """
    A door in the Monty Hall game show Let's Make A Deal
    """

    def __init__(self, name, has_prize=False):
        self.hasPrize = has_prize
        self.name = name


class Contender(object):

    """
    The contender in the Monty Hall game
    """

    def __init__(self, initial_guess):
        self.guess = initial_guess

    def second_stage_decision(self, remaining_contender_door):
        if random.choice('yn') == 'y':
            print("GR: Well Monty, I know that switching door I would increase my chances to win, so YES I'll change "
                  "my initial pick")
            Contender.switch_door(self, remaining_contender_door)
        else:
            print("GR: Monty, I want to go ahead with my initial choice. So, I'll stick with door", self.guess)

    def switch_door(self, remaining_contender_door):
        self.guess = remaining_contender_door
        print("GR: Monty, my new pick is door", self.guess)


class MontyHall(object):

    """
    Monty Hall himself!!
    """

    @staticmethod
    def open_door(door_without_prize):
        print("MH: I can tell you behind door", door_without_prize, "there isn't any prize")
        print("MH: Would you like to maintain your first pick or change it?")

    @staticmethod
    def reveal_final_result(contender_final_guess, right_door):
        if contender_final_guess == right_door:
            print("MH: Congratulation, you just won a brand new car!!")
        else:
            print("MH: What a pity! The final prize was behind door", right_door)


def main():

    """
    "Let's Make A Deal" game
    """

    a = Door("A")
    b = Door("B")
    c = Door("C")

    """Hide the prize behind one of the doors and let the contender make his first pick"""
    doors = ''.join([a.name, b.name, c.name])
    right_door = random.choice(doors)
    contender = Contender(random.choice(doors))
    monty = MontyHall()

    """Print right door and contender first choice"""
    print("The prize is behind door:", right_door)
    print("The contender chooses door:", contender.guess)

    """
    Here is where things start getting interesting. There are two scenarios:
    1) The contender got it right on his first pick, so MH will have the choice of open one of the
         two remaining doors
    2) The contender got it wrong on his first pick, so MH will have to open the only remaining door
         which doesn't hide the final prize
    """
    first_stage_remaining_doors = re.sub(contender.guess, '', doors)
    doors_to_exclude = ''.join(['[', right_door, contender.guess, ']'])
    remaining_doors_without_prize = re.sub(doors_to_exclude, "", doors)
    door_to_open = random.choice(remaining_doors_without_prize)
    remaining_contender_door = re.sub(door_to_open, "", first_stage_remaining_doors)

    """
    Second stage of the game. MH will open one of the two remaining doors and the contender will have to
      decide if maintaining his/her first pick or switching door
    """
    monty.open_door(door_to_open)
    contender.second_stage_decision(remaining_contender_door)

    """A lot of suspense before MH will tell the audience the final result. Will the contended win the car??"""
    monty.reveal_final_result(contender.guess, right_door)


if __name__ == "__main__":
    main()
