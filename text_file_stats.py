import sys, os.path, re, collections, json
from collections import  Counter

def calculate_lines(file_name):
    return len(open(file_name).readlines())

def calculate_words(file_name):
    num_words = 0
    for line in open(file_name):
        words = line.split()
        num_words += len(words)
    return num_words

def calculate_characters(file_name):
    num_characters = 0;
    for line in open(file_name):
        num_characters += len(line)
    return num_characters

def find_most_common_word(file_name):
    list_words = Counter(re.findall('\w+', open(file_name).read()))
    most_common_word = ''
    most_common_word_frequence = 0
    for word in list_words:
        if list_words[word] > most_common_word_frequence:
            most_common_word_frequence = list_words[word]
            most_common_word = word
    return most_common_word

def count_letters(file_text):
    letters = {}
    for char in file_text:
        if char != ' ': 
            if char in letters: 
                letters[char] += 1
            else: 
                letters[char] = 1
    return letters

def find_most_common_letter(file_name):
    file_text = open(file_name).read()
    list_characters = count_letters(file_text)
    most_common_letter = ''
    most_common_letter_frequence = 0
    for character in list_characters:
        if list_characters[character] > most_common_letter_frequence:
            most_common_letter_frequence = list_characters[character]
            most_common_letter = character
    return most_common_letter

def find_word_count(file_name):
    list_words = Counter(re.findall('\w+', open(file_name).read()))
    return list_words

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    if os.path.isfile(file_name):
        data = {}
        data['lines'] = calculate_lines(file_name)
        data['words'] = calculate_words(file_name)
        data['characters'] = calculate_characters(file_name)
        data['most_common_word'] = find_most_common_word(file_name)
        data['most_common_letter'] = find_most_common_letter(file_name)
        data['word_count'] = find_word_count(file_name)
        print json.dumps(data, indent=4, sort_keys=True)
    else:
        print "input doesn't exist"
else:
    print "invalid number of arguments"

