str1 = ["flower", "flow", "flight"]
# str1 = ["pow", "power", "powers"]

if not str1:
    print("")  # Empty list

result = ""
first_word = str1[0]

for i in range(len(first_word)):
    current_char = first_word[i]
    
    # Check if this character exists in all other words
    for word in str1[1:]:
        if i >= len(word) or word[i] != current_char:
            print(result)  # Print longest common prefix found so far
            exit()
    
    # Character matches in all words
    result += current_char

print(result)  # Print final result