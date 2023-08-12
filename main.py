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

    for i in range(1, totalNums, 1):
        if nums[i - 1] > nums[i]:
            return False
    return True


# TODO: Fix bug where it won't cause a lose condition if the first index is larger
def checkOpenPlace(genNum):
    for i in range(0, totalNums, 1):  # For every possible index
        listedNum = nums[i]
        if listedNum == 0:  # If there is a number
            if checkValidPlace(i, genNum):  # Check if found open space can be used
                return True
    return False


def checkValidPlace(userNum, genNum):
    if userNum - 1 >= 0:
        userNum -= 1
    # Check if the index is in range
    if totalNums >= userNum >= 0:
        if nums[userNum] != 0:  # Check if index value is 0 check for invalid placement
            return False
        elif 2 <= userNum < totalNums - 1:  # If the index isn't at the beginning or end of the list
            for i in range(userNum + 1, totalNums, 1):  # Check if nearest number below is larger
                if nums[i] != 0:
                    if nums[i] < genNum:
                        return False
            for i in range(userNum - 1, 0, -1):  # Check if nearest number above is smaller
                if nums[i] != 0:
                    if nums[i] > genNum:
                        return False
        elif userNum == 0:  # If the index is 0 check for invalid placement
            for i in range(userNum + 1, totalNums, 1):
                if nums[i] != 0:
                    if nums[i] < genNum:
                        return False
        elif userNum == totalNums:  # If the index is the max check for invalid placement
            for i in range(userNum - 1, 0, -1):
                if nums[i] != 0:
                    if nums[i] > genNum:
                        return False
        return True  # No invalid placement found
    else:  # If index is not in range return false
        return False




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

        numToPlace = random.randint(1, 1000)  # Generate a random number
        if not checkOpenPlace(numToPlace):  # Call checkOpenPlace to check if the number doesn't fit
            turns = totalNums + 1
        else:  # If it does fit then allow the player to place it
            placing = True
            while placing:
                index = prompt(f'Place {numToPlace}')
                if checkValidPlace(int(index), numToPlace):  # Call checkValidPlace to ensure it doesn't lose
                    nums[int(index) - 1] = numToPlace
                    placing = False
                else:
                    print("Invalid placement! Try again.")

        turns += 1
        if turns > totalNums:
            if checkForWin():
                print(f'You win! Congrats!')
            else:
                print(f'Sorry! You lost! --------- Next number: {numToPlace}')

            # win = checkForWin()
            # if win:
            #     print(f'You win! Congrats!')
            # if not win:
            #     print(f'Sorry! You lost!')

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

