mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
row_ind = 0
col_ind = 0;
m = 3
n = 3
row_arr = []
z = 0
print(“Sum of rows is “, end = “”)
for row in range(0, m):
sum = 0
for col in range(0, n):
sum = sum + mat[row][col]
print(sum, end = ” “)
z = z + 1
row_arr.append(sum)

temp_row = row_arr[0]
for i in range(1, m):
if(temp_row < row_arr[i]):
temp_row = row_arr[i]
row_ind = i
print(“Row”, row_ind+1,”has maximum sum”) 
print(“Sum of columns is “, end = “”)

sum = 0
y = 0
col_arr = []
for i in range(0, n):
sum = 0
for j in range(0, m):
sum = sum + mat[j][i]
print(sum, end = ” “)
y = y + 1
col_arr.append(sum)

temp_col = col_arr[0]
for i in range(1, n):
if(temp_col < col_arr[i]):
temp_col = col_arr[i]
col_ind = i
print(“Column”, col_ind+1,”has maximum sum”)
