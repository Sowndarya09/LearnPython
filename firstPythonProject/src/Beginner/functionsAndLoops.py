#FUNCTION
# def cube(text, age): #lowecase underscore parameters
#     print("HI "+text+str(age))
# print("TOP")
# sampl_e("SOWND ", 34)
# print("BOTTOM")
# sampl_e("BALA ", 38)

#RETURN STATEMENT
# def cube(num):
#     return num*num*num
# number = input("Number you want to cube: ")
# result = cube(int(number))
# print(result)

#IF STATEMENT
# is_female = True
# is_tall = False
# if is_female and is_tall: # replace or with and
#     print("You are a female")
# elif is_female and not(is_tall):
#     print("You are female not tall")
# else:
#     print("You are a male")

#COMPARISON OPERATOR
# def max_num(num1, num2, num3):
#     if num1>= num2 and num1>num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3
# print(max_num(2,7,4))

#WHILE LOOP
# i=1
# while i<=10:
#     print(i)
#     i+=1

#For Loop
# friends = ["arjun","achu","bala"]
# # for letter in "Sownd":
# #     print(letter)
# # for friend in friends:
# #     print(friend)
# print(len(friends)) # Gives lenght of an array
# for index in range(len(friends)):
#     print(friends[index])


#Exponential
# print(2*2*2*2)
# def raise_to_power(base_num, power_num):
#     #print(base_num**power_num)
#     result=1
#     for index in range(power_num):
#         result = result*base_num
#     return result
#
# print(raise_to_power(2,3))


# 2-D List and Nested loops
# number_grid =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]] #4 rows and 3 colmuns
# print(number_grid[1][2])
#
# for row in number_grid:
#     for column in row:
#         print(column)

#try except
try:
    value =10/0
    number = int(input("Enter number: "))
    print(number)
except ZeroDivisionError as err:
    print("Zero division ")
    print(err)
except ValueError:
    print("Invalid input")
