word_list = input("Please inserst paragraph to be crunched (no punctuation please): ").split()
#The list of words to be crunched.
number_of_words = len(word_list)
#The number of words to be crunched.
word_number = 0
#The word we are on (starts at 0)
first_longest = "a"
second_longest = "a"
third_longest = "a"
old_first_longest = first_longest
old_second_longest = second_longest

while word_number < number_of_words:
    current_word = word_list[word_number]
    if len(current_word) > len(first_longest):
        first_longest = old_first_longest
        first_longest = current_word
        second_longest = old_second_longest
        second_longest = old_first_longest
        third_longest = old_second_longest
    elif len(current_word) > len(second_longest):
        second_longest = old_second_longest
        second_longest = current_word
        third_longest = old_second_longest
    elif len(current_word) > len(third_longest):
        third_longest = current_word
    word_number = word_number + 1
print("The first place word is " + str(first_longest) + " with " + str(len(first_longest)) + " letters!")
print("The second place word is " + str(second_longest) + " with " + str(len(second_longest)) + " letters!")
print("The third place word is " + str(third_longest) + " with " + str(len(third_longest)) + " letters!")
