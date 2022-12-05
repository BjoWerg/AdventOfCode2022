# open the file and read its contents
with open('input3.txt', 'r') as f:
    contents = f.readlines()

# initialize a sum for the values of the common letters
sum = 0

# loop through each row in the file
for row in contents:
    # split the row into two halves
    first_half = row[:len(row)//2]
    second_half = row[len(row)//2:]

    # check if any letters are common between the two halves
    for letter in first_half:
        if letter in second_half:
            # calculate the value of the common letter and add it to the sum
            if 'a' <= letter <= 'z':
                sum += ord(letter) - ord('a') + 1
            elif 'A' <= letter <= 'Z':
                sum += ord(letter) - ord('A') + 27

            # only consider the first common letter in the row
            break

# print the sum of the values of the common letters
print(f'Sum of values of common letters: {sum}')