word = "Python"

print("0th word", word[0])
print("5th word", word[5])
print(word[-1]) #last character (from right)
print(word[-2]) #second-last character (from right)
print(word[-6]) #6th character (from right)

# Slicing the string
# [start:end]

print(word[:2]) # Character from the beginning to position two (excluded)
print(word[4:]) # Character from position 4 (included) to the end
print(word[-2:]) # Character from the second-last (included) to the end

print(word[:2] + word[2:]) # 'py' + 'thon'
print(word[:4] + word[4:])  # 'pyth' + 'on'

print(word[4:42])
print(word[42:])
print('J'+ word[1:])
print(word[:2]+'py')