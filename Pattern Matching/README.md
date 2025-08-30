# 📖 Regex & Pattern Matching with NLTK (Moby Dick Dataset)

- This project demonstrates **text pattern matching** and **regular expression (regex) filtering** using the **NLTK Gutenberg corpus**.
- We use the book *Moby Dick by Herman Melville* to explore different word patterns.  

---

## 🔹 Features Implemented

### 1. Words Ending with a Specific Pattern
Filters words that end with `"ing"`.

```python
ending_ing = [word for word in unique_words if word.endswith('ing')]
print(ending_ing[:20])
```
### 2. Words Matching a Wildcard Pattern

Supports:
- ? → matches any single character
- * → matches zero or more characters
```
def wildcard_match(pattern, word_list):
    regex = '^' + pattern.replace('?', '.').replace('*', '.*') + '$'
    return [word for word in word_list if re.match(regex, word)]
# Examples
print(wildcard_match('b?ll', unique_words))     # ball, bell, bill
print(wildcard_match('judicia*', unique_words)) # judicial, judiciary
```

### 3. Words Without Vowels

Finds words that do not contain vowels (a, e, i, o, u).
```
no_vowel_words = [word for word in unique_words if not re.search(r'[aeiou]', word)]
print(no_vowel_words)

```

### 4. Words with Specific Length Constraints

Filters words with length between 5 and 6 characters.
```
length_filtered = [word for word in unique_words if 5 <= len(word) <= 6]
print(length_filtered[:20])

```

### 5. Words with Repeated Characters (Quantifiers)

Finds words with double letters (e.g., ss, oo, ll).
```
repeated_letter_words = [word for word in unique_words if re.search(r'(.)\1', word)]
print(repeated_letter_words[:20])

```

### ⚡ Summary

- Used NLTK Gutenberg corpus (moby_dick.txt)
- Applied regex filtering for:
- Word endings
- Wildcards
- No-vowel words
- Word length
- Double letters

This project helps in understanding text preprocessing, regex patterns, and linguistic exploration using real text data.
