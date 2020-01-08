a = [[1, 2, 3],  
        [8, 4, 6],  
        [4, 5, 7]];  
b = [[1, 2, 3],  
        [8, 4, 6],  
        [4, 5, 7]];  
flag = True;  
 
row1 = len(a);  
col1 = len(a[0]);  
 
row2 = len(b);  
col2 = len(b[0]);  
 
if(row1 != row2 or col1 != col2):  
    print("Matrices are not equal"); 
else:
	print ("Matrices are equal")
