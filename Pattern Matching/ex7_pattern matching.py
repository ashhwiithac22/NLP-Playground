import nltk
import re
from nltk.corpus import gutenberg
nltk.download('gutenberg')
nltk.download('punkt') #helps to split text into words
words = gutenberg.words('melville-moby_dick.txt')
words = [word.lower() for word in words if word.isalpha()]
unique_words = sorted(set(words))
# 1. Words ending with a specific pattern (eg:ing)
print("\n Words ending with ing:") #loads all lines from moby dick book
ending_ing = [word for word in unique_words if word.endswith('ing')]
print(ending_ing[:20])

# 2. Words matching a pattern with wildcards (* and ?) #? - means one letter and * means any number of letters
def wildcard_match(pattern, word_list):
    regex = '^' + pattern.replace('?', '.').replace('*', '.*') + '$'
    return [word for word in word_list if re.match(regex, word)]

print("\n Words matching wildcard pattern 'b?ll':")
wildcard_words = wildcard_match('b?ll', unique_words)
print(wildcard_words)

print("\n Words matching wildcard pattern 'judicia*':")
wildcard_words2 = wildcard_match('judicia*', unique_words)
print(wildcard_words2)

# 3. Words that do not contain any vowels
print("\n Words without vowels:")
no_vowel_words = [word for word in unique_words if not re.search(r'[aeiou]', word)]
print(no_vowel_words)

# 4. Words with specific length constraints (e.g.length =    5 to 6)
print("\n Words with length 5 to 6:")
length_filtered = [word for word in unique_words if 5 <= len(word) <= 6]
print(length_filtered[:20])

# 5. Words using quantifiers (e.g., double letters like 'ss', 'oo')
print("\n Words with repeated characters using quantifier (e.g., double letters):")
repeated_letter_words = [word for word in unique_words if re.search(r'(.)\1', word)]
print(repeated_letter_words[:20])
#. means any character and \1 means the same character
