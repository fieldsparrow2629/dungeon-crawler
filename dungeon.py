class Dungeon:
    def __init__(self):
        self.one_clear = False
        self.two_clear = False
        self.three_clear = False
        self.four_clear = False
        self.five_clear = False

    def room_one(self):
        print("You enter the first room, it is dark and damp.")
        print("You see a fire in the center of the room...")
        print("Take a torch with you?...")
        while True:
            ans = input()
            if ans == 'y':
                print("You pick up the torch")
            if ans == 'n':
                print("You leave the torch")

            break
