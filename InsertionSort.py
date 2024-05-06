#Question  
#a) Write a program to read a set of numbers (between 10  to 20) from the keyboard and store 
#them in an array.  
#b) Sort the numbers in ascending order with the Insertion sorting algorithm. 


#a
A = []
for v in range(10):
    A.append(int(input("Enter a number: ")))
print(A)

#b
def insertsort(A):
    for j in range (1, len(A)):
        key = A[j]
        i = j-1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i=i-1
        A[i+1] = key
    return while_count

print("Sorted Array ")
for item in A:
    print(item)
        
        


