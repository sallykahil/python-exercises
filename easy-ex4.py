#Write a function that takes an ordered list of numbers
#  (a list where the elements are in order from smallest to largest) and another number.
#  The function decides whether or not the given number is inside the list and returns (then prints)
#  an appropriate boolean.
def listfunction() :
    numbers = input("Enter numbers separated by spaces to create a list : ").split()
    numbers = [int(num) for num in numbers] 
    sorted_list = sorted(numbers)

    print ("the ordered list is :",sorted_list)
    number=int(input("enter a number to check if found in list "))
     
    if(number in sorted_list):
        print(f"{number} is found in list ")
    else:
        print(f"{number} is not found in list ")
    return sorted_list

print("solution 1 ")
listfunction() 
 #boolean way 
print("solution 2 ")
def find(ordered_list, element_to_find):
  for element in ordered_list:
    if element == element_to_find:
      return True
  return False
n= input("Enter numbers separated by spaces to create a list : ").split()

n = [int(num) for num in n] 
sorted_list = sorted(n)
number=int(input("enter a number to check if found in list "))
   
if find(n,number) is True:
   print("it is found")
else :
   print("it is not found")
