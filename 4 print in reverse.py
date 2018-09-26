##author: ricky
##date: 26 sep 2018
##decription: wrod length and word in reverse
##Hello olleh
##date modified: 26 sep 2018


user_input = input("please enter a word: ")

word_length = len(user_input)

print(user_input,"has the length of:",word_length)
reverse_word = ""

for i in range(word_length):
    reverse_word = user_input[i] + reverse_word
print(reverse_word)
