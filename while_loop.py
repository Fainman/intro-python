'''
Learn conditional repetition
Two loops: for-loop and while-loops
'''

counter = 5
while counter != 0:
    print(counter)
    counter -= 1

counter = 5
while counter:
    print(counter)
    counter -= 1

# Run forever
while True:
    print("Enter a number")
    response = input()          # take user input
    if int(response) % 7 == 0:  # number divisible by 7
        break                   # exit loop

print("Outside while loop")