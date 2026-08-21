'''
=================================
           HIT137 
Group Assignment 1: Text Analyser
=================================
     Group Name: DAN/EXT 15
=================================

Group Members:
--------------
 Ashok Tamang   -  S406128
 Rajesh Basnet  -  S404205
 Aryan Karki    -  S407507
 Ayun Neupane   -  S406923
'''

#================================
# Solution Start: 
#================================

# Taking multi-line input from users:
print("=" * 20)
print("TEXT ANALYSER")
print("=" * 20)
text = ""
print('Enter your text (Press Enter on an empty line when you are finished):')
while True:
        line = input()
        if line == "":
            break
        # Adding a newline characters to separate lines, avoiding it for the very first line
        if text != "":
            text += "\n"
        text += line 

'''
-------------------------
Task 1: Character census
-------------------------
Scan the input text one character at a time and count:
    1.	the total number of characters,
    2.	the number of letters (a-z, A-Z),
    3.	the number of digits (0-9),
    4.	the number of whitespace characters (spaces, tabs, newlines),
    5.	the number of other characters (everything else — punctuation and so on).
Print a short, clearly labelled report of these five numbers. As a self-check, the four category counts should add up to the total.
'''

# ----------------------------
# Task 1: Solution:
# ---------------------------- 

# Initialising Task 1 Counters
total = 0
letters = 0
digits = 0
whitespace = 0
other = 0

# Checking each character
for ch in text:
    total += 1            
    if ch.isalpha():      # alphabet check
        letters += 1
    elif ch.isdigit():    # digit check
        digits += 1
    elif ch.isspace():    # whitespace check
        whitespace += 1
    else:                 # other check
        other += 1

# Displaying output of Task 1
print()
print("=" * 40)
print("Task 1: Character Census")
print("=" * 40)
print(f"Total number of characters     : {total}")
print(f"Number of letters(a-z, A-Z)    : {letters}")
print(f"Number of digits(0-9)          : {digits}")
print(f"Number of whitesape characters : {whitespace}")
print(f"Number of other characters     : {other}")

# Self check
check = letters + digits + whitespace + other
if check == total:
    print("self check success: counts the total.")
else:
    print("Self-check failed: count does not equal total.")

'''
---------------------------------
Task 2: Case and vowel breakdown
---------------------------------
Extend your program so that you also count:
    1.	uppercase letters and lowercase letters separately,
    2.	vowels and consonants separately (treat	a e i o u as vowels, in either case),
    3.	how many times each individual vowel appears. 
Add these to your report.
'''

# ----------------------------
# Task 2: Solution:
# ----------------------------

# Initialising Task 2 Counters
UC = 0
LC = 0
V = 0
CS = 0
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Checking each character
for ch in text:
    if ch.isalpha():                # checking alphabets

        if ch.isupper():            # checking uppercase letters
            UC += 1
        elif ch.islower():          # checking lowercase letters
            LC += 1

        if ch.lower() in "aeiou":   # checking vowels
            V += 1
            if ch.lower() == "a":
                a_count += 1
            elif ch.lower() == "e":
                e_count += 1
            elif ch.lower() == "i":
                i_count += 1
            elif ch.lower() == "o":
                o_count += 1
            elif ch.lower() == "u":
                u_count += 1
        else:                       # checking consonants
            CS += 1

# Displaying output of Task 2
print()
print("=" * 40)
print("Task 2: Case and Vowel Breakdown")
print("=" * 40)
print(f"Uppercase letters              : {UC}")
print(f"Lowercase letters              : {LC}")
print(f"Vowels                         : {V}")
print(f"Consonants                     : {CS}")
print(f"'a' count                      : {a_count}")
print(f"'e' count                      : {e_count}")
print(f"'i' count                      : {i_count}")
print(f"'o' count                      : {o_count}")
print(f"'u' count                      : {u_count}")

'''
------------------------
Task 3: Word statistics
------------------------
Treat a word as a run of one or more letters (you may also allow an apostrophe inside a word, so that we're and isn't count as single words). 
Anything that is not part of a word (spaces, punctuation, digits, newlines) separates one word from the next.
Using this rule, report:
    1.	the total number of words,
    2.	the longest word and its length (if several words tie for longest, report the first one),
    3.	the average word length, rounded to one decimal place.
'''

# -----------------------------------------
# Task 3: Solution:
# -----------------------------------------

# Initialising Task 3 Variables and Counter
words = []
current_word = ""
length = len(text)
index = 0

# Finding total number of words 
while index < length:
    char = text[index]

    if char.isalpha():
        current_word += char
        index += 1
    elif (
        char == "'"
        and current_word != ""
        and index + 1 < length
        and text[index + 1].isalpha()
    ):
        current_word += char
        index += 1
    else:
        if current_word != "":
            words.append(current_word)
            current_word = ""
        index += 1

if current_word != "":
    words.append(current_word)

total_words = len(words)

# Finding longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Determining average word length
if total_words > 0:
    total_letters_in_words = 0
    for word in words:
        total_letters_in_words += len(word)
    average_length = round(total_letters_in_words / total_words, 1)
else:
    average_length = 0.0

# Displaying output of Task 3  
print()
print("=" * 40)
print("Task 3: Word Statistics")
print("=" * 40)
print(f"Total number of words          : {total_words}")
print(f"Longest Word                   : {longest_word}")
print(f"Length of Longest Word         : {len(longest_word)}")
print(f"Average Word Length            : {average_length}")

'''
-----------------------------------
Task 4: Line and sentence analysis
-----------------------------------
Add three more measurements:
    1.	the number of lines in the text (a line is separated by the newline character '\n'),
    2.	the number of sentences, where a sentence ends with: .,!, or ?,
    3.	the length of the longest line (in characters).
'''

# ----------------------------
# Task 4: Solution:
# ----------------------------

#Initialising Task 4 Variables
lines = []
line = ""

# Finding number of lines in the text
for ch in text:
    if ch == "\n":
        lines.append(line)
        line = ""
    else:
        line += ch
lines.append(line)  
line_count = len(lines)

# Finding number of sentences, where a sentence ends with: .,!, or ?
sentence_count = 0
for ch in text:
    if ch == "." or ch == "!" or ch == "?":
        sentence_count += 1

# Finding length of longest line (in characters)
longest_line = 0
for ln in lines:
    if len(ln) > longest_line:
        longest_line = len(ln)

# Displaying output of Task 4
print()
print("=" * 40)
print("Task 4: Line and Sentence Analysis")
print("=" * 40)
print(f"Number of lines                : {line_count}")
print(f"Number of sentences            : {sentence_count}")
print(f"Longest line length            : {longest_line}")
print("=" * 40)
