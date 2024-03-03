num = input('Enter a number (decimal only): ')
# type your code here
temp_num = num
dot = temp_num.find(".")
temp_list = list(temp_num)
i = 0
while i <= dot:
  temp_list.pop(i)
  i = i + 1

temp_num = "".join(temp_list)
dp = len(temp_num)

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')


