# task 3 coding questions

#Question1
def hello_name(user_name):
    print("hello_" + user_name)
hello_name("USERNAME")
hello_name("Scott")

#Question2
def odd_num(num):
    numList = []
    for n in range(1,num):
        if n % 2 == 0:
            numList.append(n)
            
    print(numList)
odd_num(100)

#Question3
def max_num_in_list(a_list):
    maxNum = 0
    for n in a_list:
        if n > maxNum:
            maxNum = n
    return maxNum

aList = [2,1,45,4,7,24]
print(max_num_in_list(aList))     

#Question4
def is_leap_year(a_year):
    if a_year%100 == 0 and a_year%400 == 0:
        return True
    elif a_year%4 == 0:
        return True
    else:
        return False
if is_leap_year(2024) == True:
    print("It's a leap year!")
else:
    print("It's not a leap year.")

#Question5
def is_consecutive(a_list):
    currentNum = a_list[0]
    for n in a_list[1:]:
        if n != currentNum+1:
            return False
        else:
            currentNum += 1
    return True

a_list = [2,3,4,5,6]
if is_consecutive(a_list):
    print("It's Consecutive!")
else:
    print("It's not Consecutive.")