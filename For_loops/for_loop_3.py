# adding all the numbers in the list and also prinintg the sum ouside the for loop
# Observe that all the addition is done inside the for loop and result is printed outside the for loop

my_list = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in my_list:
    list_sum = list_sum + num

print(list_sum)