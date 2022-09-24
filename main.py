import string
from itertools import product


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def check_if_valid(chak_word):
    for i in range(len(chak_word) - 2):
        if chak_word[i] == chak_word[i + 1] and chak_word[i] == chak_word[i + 2]:
            return False
    return True

def check_uppercase(str):
    count_uppercase = 0
    for i in str:
        if i ==string.ascii_uppercase:
            count_uppercase += 1
            if count_uppercase>2:
                return False
    return True



min_lan = int(input("enter min lan: "))
max_lan = int(input("enter max lan: "))
counter = 0
#string.digits  string.ascii_uppercase  string.ascii_lowercase  string.punctuation
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
chars.list
counter_of_lists = 0
word_list = open(f"word_list{counter_of_lists}.txt", "w")

if min_lan <= 5:
    print("The password must be at least 6 chars")

else:
    for i in range(min_lan, max_lan + 1):
        for j in product(chars, repeat=i):

            word = "".join(j)
            print(word)
            if not has_numbers(word):
                continue

            if not check_if_valid(list(word)):
                continue

            if not check_uppercase(word):
                continue

            if counter == 20000000:
                word_list.close()
                counter_of_lists += 1
                word_list = open(f"word_list_num{counter_of_lists}.txt", "w")
                counter = 0
                continue
            else:
                word_list.write(word + "\n")
                print(word)
                counter += 1