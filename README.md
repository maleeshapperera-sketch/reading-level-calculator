# reading-level-calculator
A text readability analyzer that computes U.S. grade levels using the Coleman-Liau index formula.

📚 The Problem
Given any text, determine what grade level is required to read it comfortably, just like Flesch-Kincaid readability tests.

📊 Coleman-Liau Index Formula
text
index = 0.0588 * L - 0.296 * S - 15.8

Where:
L = average number of letters per 100 words
S = average number of sentences per 100 words
Grade Level Output
Grade 1 or lower → "Before Grade 1"

Grade 16 or higher → "Grade 16+"

Grades 2-15 → "Grade X" (where X is the number)

🔤 What Counts As...
Letters - Uppercase and lowercase A-Z (no punctuation, numbers, spaces)

Words - Any sequence of characters separated by spaces

Sentences - Ends with ., !, or ?

🛠️ Implementation Approach
Step 1: Count Letters
c
// Check each character, count A-Z or a-z
if (isalpha(c)) letters++;
Step 2: Count Words
c
// Count spaces + 1, OR check word boundaries
if (c == ' ') words++;
Step 3: Count Sentences
c
// Count punctuation marks
if (c == '.' || c == '!' || c == '?') sentences++;
Step 4: Calculate Averages
c
float L = (float)letters / words * 100;
float S = (float)sentences / words * 100;
Step 5: Compute Index & Round
c
int index = round(0.0588 * L - 0.296 * S - 15.8);
📁 Files
readability.c - Main program (C version)

readability.py - Python version (if applicable)

🚀 Usage
bash
# C version
make readability
./readability

# Python version
python readability.py
📝 Example Inputs & Outputs
Input:

text
Congratulations! Today is your day. You're off to Great Places! You're off and away!
Output:

text
Grade 3
Input:

text
Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of night. And he also happened to be a wizard.
Output:

text
Grade 5
Input:

text
One fish. Two fish. Red fish. Blue fish.
Output:

text
Before Grade 1
