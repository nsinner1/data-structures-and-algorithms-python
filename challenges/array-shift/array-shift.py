

my_arr = [1, 2, 4, 5] 
def insert_Shift_Array():
  user_arr_input = input("please type anything that you would like to insert into the array: ")
  middle_number = len(my_arr)//2
  my_array =  my_arr[0:middle_number] + [user_arr_input] + my_arr[middle_number:]
  print (my_array)
insert_Shift_Array()

