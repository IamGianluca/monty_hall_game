import random
import copy


class Door(object):

    """
    A door in the Monty Hall game show Let's Make A Deal
    """

    # Use class variable to keep track of which door hides the prize
    right_door = None

    def __init__(self, name, has_prize=False):
        self.hasPrize = has_prize
        self.name = name

    def hide_prize(self):
        self.hasPrize = True


class Contender(object):

    """
    The contender in the Monty Hall game
    """

    def __init__(self):
        self.guess = None

    def second_stage_decision(self, remaining_contender_doors):
        if random.choice('yn') == 'y':
            print("GR: Well Monty, I know that switching door I would increase my chances to win, so YES I'll change "
                  "my initial pick")
            Contender.switch_door(self, remaining_contender_doors)
        else:
            print("GR: Monty, I want to go ahead with my initial choice. So, I'll stick with door", self.guess.name)

    def choose_door(self, doors):
        self.guess = random.choice(doors)

    def switch_door(self, remaining_contender_doors):
        assert len(remaining_contender_doors) == 2
        remaining_contender_doors.remove(self.guess)
        self.guess = remaining_contender_doors[0]
        print("GR: Monty, my new pick is door", self.guess.name)


class MontyHall(object):

    """
    Monty Hall himself!!
    """

    @staticmethod
    def open_door(door_without_prize):
        print("MH: I can tell you behind door", door_without_prize.name, "there isn't any prize. Would you like to "
                                                                         "maintain your first pick or change it?")

    @staticmethod
    def reveal_final_result(contender_final_guess, right_door):
        if contender_final_guess.hasPrize:
            print("MH: Congratulation, you just won a brand new car!!")
        else:
            print("MH: What a pity! The final prize was behind door", right_door.name)

    @staticmethod
    def decide_door_with_prize(doors):
        right_door = random.choice(doors)
        right_door.hide_prize()
        Door.right_door = right_door


def main():

    """
    "Let's Make A Deal" game
    """

    a = Door("A")
    b = Door("B")
    c = Door("C")

    # Hide the prize behind one of the doors and let the contender make his first pick
    doors = [a, b, c]

    MontyHall.decide_door_with_prize(doors)

    contender = Contender()
    contender.choose_door(doors)

    # Print the name of the door which hides the final prize and the contender (GR) first choice
    print("The prize is behind door:", Door.right_door.name)
    print("The contender chooses door:", contender.guess.name)
    print()

    """
    Here is where things start getting interesting. There are two scenarios:
    1) The contender got it right on his first pick, so MH will have the choice of open one of the
         two remaining doors
    2) The contender got it wrong on his first pick, so MH will have to open the only remaining door
         which doesn't hide the final prize

    @TODO: Find better way to remove class instances from array. numpy.delete is not an option because it doesn't
      handle class instances as arguments
    """
    first_stage_remaining_doors = copy.copy(doors)
    first_stage_remaining_doors.remove(contender.guess)

    remaining_doors_without_prize = copy.copy(first_stage_remaining_doors)
    if Door.right_door in remaining_doors_without_prize:
        remaining_doors_without_prize.remove(Door.right_door)

    door_to_open = random.choice(remaining_doors_without_prize)
    remaining_contender_door = copy.copy(doors)
    remaining_contender_door.remove(door_to_open)

    """
    Second stage of the game. MH will open one of the two remaining doors and the contender will have to
      decide if maintaining his/her first pick or switching door
    """
    MontyHall.open_door(door_to_open)
    contender.second_stage_decision(remaining_contender_door)

    # Lot of suspense before MH will tell the audience the final result. Will the contended win the car??
    MontyHall.reveal_final_result(contender.guess, Door.right_door)


if __name__ == "__main__":
    main()
