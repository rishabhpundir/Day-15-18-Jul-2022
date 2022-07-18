# ages = [15, 34, 56, 12, 7, 18, 20]

# def funct(age):
#     if age >= 18:
#         return True
#     else:
#         return False

# adults = filter(funct, ages)

# for i in adults:
    # print(i)


# -------------------------------------------------------------------


# A VOWEL FILTER

# def funct(char):
#     vowels = 'aeiou'
#     if char not in vowels:
#         return True
#     else:
#         return False

# sequence = ['v', 'e', 's', 'p', 'e', 'r']

# filtered_list = list(filter(funct, sequence))

# print(filtered_list)


# -------------------------------------------------------------------


# FILTERING WORDS BASED ON CHAR LENGTH

# def checker(word):
#     if len(word) >= 5:
#         return True
#     else:
#         False

# sentence = str(input("Enter the sentence : "))
# words = sentence.split()

# filtered_words_list = list(filter(checker, words))
# print(filtered_words_list)


# -------------------------------------------------------------------


# USING FILTER WITH LAMBDA

# num_list = [10, 32, 2, 5, 11, 55, 38, 51]

# # for odd numbers
# result = filter(lambda x:x % 2 != 0, num_list)
# print(list(result))

# # for even numbers
# result = filter(lambda x:x % 2 == 0, num_list)
# print(list(result))


# -------------------------------------------------------------------


