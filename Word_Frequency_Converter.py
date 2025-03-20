"""
Create a Python program that allows the user to input a
sentence, then counts the frequency of each word in the
sentence. 
"""
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}

for word in words:
    word = word.lower().strip(".,!?;")  
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
