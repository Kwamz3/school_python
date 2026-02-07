# while loop works by evaluating a condition at the start of a condition.

# they're also useful for for loops in which the number of iterations are unknown.

# a while True loop creates an infinte loop that continues to execute until the a break statement is introduced-
# or an external interuption occurs.

# loops are control flow statements that excute a set of code a number of times 

# a for loop is used for a known number of times 
# a while loop is used for a unknown number of times


# # an example of a using a while loop to iterate over decreasing numbers
# number = 5

# while number > 0:
#     print(number)
#     number -= 1


# # because it decreses by -1 it reaches the 0 where it's checked and it when number = 0 the conditional becomes false
# # and comes out of the loop
# number = 5
# while number != 0:
#     print(number)
#     number -= 1

# because it decreses by -2 it reaches the -1 where it's when the checking takes place number = -1 and the conditional still checks true
# and continues to run negative numbers
# number = 5
# while number != 0:
#     print(number)
#     number -= 2


# # the use of the break enables the user to terminate the current loop and continue with the first block of code after the loop
# number = 6

# while number > 0:
#     number -= 1
#     if number == 2:
#         break
#     print(number)


# the continue keyword is almost identical to the break except that it skips the conditional that will be satisfied 
number = 6

while number > 0:
    number -= 1
    if number == 2: #here 2 is skipped because the condition set has been matched successfully 
        continue
    print(number)