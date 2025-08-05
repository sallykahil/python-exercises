#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list.
#  For practice, write this code inside a function.
def listfunction() :
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    return numbers
def newlist(numbers) :
    first=numbers[0]
    last=numbers[-1]
    newlist1=[first,last]
    return newlist1
list1=listfunction()
print("Your list:" , list1)

print("new list: " , newlist(list1))

