#Question 1
def hello_name(user_name):
    print("hello_" + user_name)

hello_name("USERNAME")
hello_name("Scott")

#Question 2
for n in range(1,101):
    if n%2 == 1:
        print(n)

#Question 3
def max_num_in_list(a_list):
    maxNum = 0
    for n in a_list:
        if maxNum < n:
            maxNum = n
    return maxNum
alist = [1,4,2,3,5,8,6]
print("Max number in this list is",max_num_in_list(alist))

#Question 4
def is_leap_year(a_year):
    if a_year % 100 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 100 == 0 and a_year % 400 != 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
year = 1900
if is_leap_year(year) == True:
    print(year, "is a leap year!")
else:
    print(year, "is not a leap year.")

#Question 5
def is_consecutive(a_list):
    isCons = True
    for i in range(len(a_list)-1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return isCons

aList = [1,2,3,4,7,5]
if is_consecutive(aList):
    print("It is Consecutive!")
else:
    print("It is not Consecutive.")
    
