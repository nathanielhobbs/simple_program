import random

# this function takes a string and returns a string with all the words reversed
# e.g. reverse("one two three") returns "three two one"
def reverseWords(s):
    # you may find these useful: 
    # 'a b c'.split() will return ['a','b','c']
    # ' '.join(['a','b','c']) will return 'a b c'
    # new_list = [] # create place holder list
    # split_list = s.split() # break single string into a list of word strings.
    # for word_idx in range(len(split_list)-1,-1,-1): # starting from the last position, going to the first position, in (reverse) step size 1
    #     new_list.append(split_list[word_idx]) # append (to the end) of new_list the word from split_list at position word_idx.

    # return ' '.join(new_list) # convert list of word strings to single string with space

    return ' '.join([word for word in s.split()[::-1]])

def getWordCount(my_string):
    # iterate through each word in the string
    my_dict={}
    list_of_words = my_string.split()
    for word in list_of_words:
        if word not in my_dict:
            my_dict[word]=1
        else:
            my_dict[word] += 1

    return my_dict

def getWordFrequencies(my_string):
    # iterate through each word in the string
    my_dict={}
    list_of_words = my_string.split() # this creates a list of strings, each string is one word
    count = len(list_of_words) # we want to know the total number of words in the string
    for word in list_of_words:
        if word not in my_dict:
            my_dict[word]=1/count
        else:
            my_dict[word]+=1/count # this is the same as my_dict[word]=my_dict[word]+1/count

    return my_dict

def generateSentence(word_freq_dict):
    vocabulary_list = list(word_freq_dict.keys())
    vocabulary_weights = list(word_freq_dict.values())
    random_string=''
    while True:
        random_word = random.choices(vocabulary_list, weights=vocabulary_weights,k=1)
        random_string += random_word[0] + ' '
        if random_word[0] == '.':
            break

    # random_word = random.choices(vocabulary_list, weights=vocabulary_weights,k=1)
    # while not random_word[0] == '.':
    #     random_string += random_word[0] + ' '
    #     random_word = random.choices(vocabulary_list, weights=vocabulary_weights,k=1)
    # random_string += '.'


    return random_string

if __name__=='__main__':
    print(reverseWords('one two three'))
    print(getWordCount('cat dog dog penguin .'))
    print(getWordFrequencies('cat dog dog penguin .'))
    vocabulary_dict = getWordFrequencies('cat dog dog penguin .')
    print(generateSentence(vocabulary_dict))
    # this function takes a string and returns a string with all
    # the characters reversed
    # e.g. reverseChars("one two three") would return "eerht owt eno"
    # def reverseChars(s):





















    # Your long string of words
# long_string = "This is a long string with repeated words. This is a test string."

# # Split the string into words
# words = long_string.split()

# # Create an empty dictionary to store word counts
# word_count = {}

# # Iterate through the words and update the dictionary
# for word in words:
#     # Remove punctuation and convert to lowercase to ensure case-insensitive counts
#     cleaned_word = word.strip(".,!?:;").lower()
    
#     if cleaned_word not in word_count:
#         word_count[cleaned_word] = 1
#     else:
#         word_count[cleaned_word] += 1

# # Print the word counts
# for word, count in word_count.items():
#     print(f"'{word}': {count}")
















# this function counts the number of words in a string
# for example, countWords('every day I go to school')
# would return 6
