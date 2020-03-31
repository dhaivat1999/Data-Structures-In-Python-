numbers = [100,25412,2563,4684064,654645]

# # print(numbers[2])
# numbers[2]= 'heyy'
# # print(numbers[2])

# for num in numbers :
#     print (num)

# print(numbers[1:-1]) if we want any specific indexes from the array then we can use this method

maximum = numbers[0]
  
# Searching complexitiy O(N) complexity
# Searching in array for max element
for num in numbers:
    if num > maximum:
        maximum=num

print(maximum)

minimum=numbers[0]

for num in numbers:
    if num < minimum:
        minimum=num

print(minimum)
