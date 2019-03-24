secretNumber = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Write code that prompts the user to enter an integer number
userInput = int(input("Enter a numer to guess: "))
# Write your while loop here and the rest of your code
while(secretNumber!=userInput):
     print("No, that's not the number I've picked for you. Try again!")
     userInput = int(input("Enter a different number to guess: "))
     if (secretNumber==userInput):
         print("Well done! That's the number I've chosen for you! You are free now.")
