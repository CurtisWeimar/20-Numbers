import random

# array to hold variables and their positions
totalNums = 20
nums = [0] * totalNums


# method for receiving and parsing input from player
def prompt(text):
    print(text)
    # TODO: Verify input is a single int
    return input()


def checkForWin():
    count = 0
    for i in nums:
        if count < (totalNums - 1):
            if i > nums[count + 1]:
                return False
    return True


def gameLoop():
    # bool to hold if we are currently playing
    playing = True
    turns = 1
    while playing:
        # Display the current list
        count = 1
        for i in nums:
            print(f'{count}: {i}')
            count += 1

        numToPlace = random.randint(1, 1000)
        # TODO: Check if you can place number anywhere
        index = prompt(f'Place {numToPlace}')
        nums[int(index) - 1] = numToPlace
        turns += 1
        if turns > totalNums:
            win = checkForWin()
            if win:
                print(f'You win! Congrats!')
            if not win:
                print(f'Sorry! You lost!')

            again = prompt("Play again? (Y/N)")
            if again.lower() != "y":
                playing = False
            else:
                turns = 1
                count = 0
                for x in nums:
                    nums[count] = 0
                    count += 1


# TODO: Add a game menu
# TODO: Store statistics

gameLoop()

