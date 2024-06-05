# Write a python program to find the longest words.

def find_longest_words(file_path):
    longest_words = []
    max_length = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?";:')
                if len(word) > max_length:
                    longest_words = [word]
                    max_length = len(word)
                elif len(word) == max_length:
                    longest_words.append(word)
    
    return longest_words

file_path = 'example.txt'

longest_words = find_longest_words(file_path)

print("The longest words are:", longest_words)
