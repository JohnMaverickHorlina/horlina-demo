# Ask the user to enter the number of rows for the triangle
rows = int(input("Enter the number of rows for the triangle: "))

#Initialize the starting number and row for the triangle
number = 1  
row = 1  

#Outer loop
while row <= rows:
    col = 1  
    
    #Inner loop   
    while col <= row:
        print(number, end=" ")  
        number += 1  
        col += 1  
    
    print()  
    row += 1  