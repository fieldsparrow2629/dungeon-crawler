class Dungeon:
    def __init__(self):
        self.one_clear = False
        self.two_clear = False
        self.three_clear = False
        self.four_clear = False
        self.five_clear = False

    def room_one(self,char):
        print("You enter the first room, it is dark and damp.")
        print("You see a fire in the center of the room...")
        print("Take a torch with you?...")
        while True:
            ans = input()
            if ans == 'y':
                print("You pick up the torch")
                char.inv.append('Torch')
                char.pos = 2
                break
            elif ans == 'n':
                print("You leave the torch, and procede to the next room.")
                char.pos = 2
                break
            else:
                print("Please choose 'y/n'.")

    def room_two(self,char):
        print("You enter the second room, which is covered floor to ceiling in webs.")
        
