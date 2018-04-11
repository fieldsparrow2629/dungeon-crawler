import time
class Dungeon:
    def __init__(self):
        self.one_clear = False
        self.two_clear = False
        self.three_clear = False
        self.four_clear = False
        self.five_clear = False

    def room_one(self,char):
        print("You enter the first room, it is dark and damp.")
        time.sleep(1)
        print("You see a fire in the center of the room...")
        time.sleep(1)
        print("Take a torch with you?...")
        ans = ""
        while ans != 'y' and ans != 'n':
            ans = input()
            if ans == 'y':
                print("You pick up the torch")
                char.inv.append('Torch')
            elif ans == 'n':
                print("You leave the torch, and procede to the next room.")
            else:
                print("Please choose 'y/n'.")

    def room_two(self,char):
        print("You enter the second room, which is covered floor to ceiling in webs.")
        if char.inv[0] == 'Torch':
            print("You clear the webs with your torch.")
        else:
            print("You you cannot make your way through the room.")
        
