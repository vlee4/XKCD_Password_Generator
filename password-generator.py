# XKCD inspired Password Generator
# Author: Alina Momin

from xkcdpass import xkcd_password as xp
import random


wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile, min_length=4, max_length=6)

delimiters = ['!', '@', '#', '%', '^', '_', ')', '  ']
new_password = ''
array_of_inputs = []
word_len = int(random.randrange(4, 6))
proper_input_yes = ['yes', 'y', 'Yes', 'Y']
proper_input_done = ['d', 'done', 'DONE']

user_input_prompt = "Choose the parameters you would like to set, enter 'd' to complete:\n [1] Choose a password length \n [2] Say hi \n \n "


if __name__ == '__main__':
    print('Welcome to the Password Generator inspired by XKCD\'s comic! \n')

    customize = input(
        "Would you like to customize parameters for your password? \n Type 'yes' or ENTER to continue. \n")

    if customize in proper_input_yes:
        print('input is yes to customize \n')

        print(user_input_prompt)
        user_input = input()

        while user_input not in proper_input_done:

            if int(user_input) == 1:
                word_len = int(input("Enter word length: "))
                print(f"Your password length is now set to: {word_len} \n \n")
                user_input = 0
                # continue

            elif int(user_input) == 2:
                name = input('Type your name: ')
                print(f'Hi, {name} \n \n')
                user_input = 0
                # continue
            else:
                user_input = input(user_input_prompt)

    # automatic password
    word_v1 = (xp.generate_xkcdpassword(mywords, numwords=word_len))
    # print(word_v1)

    # word currently has num of words and is seperated by spaces
    word_v1 = str.split(word_v1)

    # randomize the delimiter that is chosen and add a random delimiter between each word
    for i in range(len(word_v1)):
        index = random.randrange(len(delimiters))

        rand_delim = delimiters[index - 1]

        joining_words = str(word_v1[i]) + str(rand_delim)

        new_password = new_password + joining_words
        # print(new_password)

    # join the strings together for a single stringed password
    new_password = new_password.strip()
    print("Your password is:", new_password)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
