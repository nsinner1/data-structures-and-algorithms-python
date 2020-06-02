# Write a function called reverseArray which takes an array as an argument. 
# Without utilizing any of the built-in methods available to your language, 
# return an array with elements in reversed order.

def reverse_array():
  x = input("would you like to enter your array type yes: ")
  my_arr = []
  while x == "yes":
    arr_val = input("enter values into your array (type quit when done): ")
    my_arr.append(arr_val)
    print(my_arr[::-1])
    if arr_val == "quit":
        break
reverse_array()
