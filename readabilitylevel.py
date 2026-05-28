para = input("Enter the paragraph: ")

# Better word splitting (handles multiple spaces, tabs, newlines)
paragraph = para.split()
no_of_words = len(paragraph)

no_of_letters = 0
no_of_sentences = 0

# Count letters and sentences
for word in paragraph:
    # Count only alphabetic characters as letters
    for char in word:
        if char.isalpha():
            no_of_letters += 1
    
    # Count sentences only when punctuation is at END of word
    if word.endswith('.') or word.endswith('?') or word.endswith('!'):
        no_of_sentences += 1
    # Special case: Handle abbreviations like "Mr.", "Mrs.", "Dr."
    elif word.lower() in ['mr.', 'mrs.', 'ms.', 'dr.', 'jr.', 'sr.']:
        # These don't end sentences
        pass

# Calculate Coleman-Liau index
L = (no_of_letters / no_of_words) * 100
S = (no_of_sentences / no_of_words) * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

# Output grade level
if index > 16:
    print("Grade 16+")
elif index >= 1:
    print(f"Grade {index}")
else:
    print("Before Grade 1")