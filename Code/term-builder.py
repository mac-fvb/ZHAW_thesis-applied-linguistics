letters = ['a', 'b', 'c', 'd', 'e', 'ae', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'oe', 'ue']

output = '('

for letter in letters:
    output += '/' + letter + '_terms[]|'

output += ')'

# Save the output to a text file
with open('output.txt', 'w') as file:
    file.write(output)

print("Output saved to 'output.txt' file.")
