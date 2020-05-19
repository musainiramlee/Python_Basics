# Nested Loops (Loop in a loop)
## Can be useful to generate related data like coordinates
### Example

# for x in range(4):
    # for y in range(5):
        # print(f'({x}, {y})')

numbers = (5, 2, 5, 2, 2)
for i in numbers:
    print('x' * i)

# Or if we used a nested loops we can run the following

for i in numbers:
    output = ''
    for count in range(i):
            output += 'C'
    print(output)

no = (2, 2, 2, 2, 8)
for char in no:
    output = ''
    for count in range(char):
            output += 'O'
    print(output)








