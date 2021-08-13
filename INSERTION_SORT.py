#INSERTION-SORT(A)
A = [ 9 , 10 , -1, 3, 6, 2, 1, -3, 1, 0, -2, 15, 8, -7, 0] 

for j in range(1,len(A)):
    
    chave = A[j]
    i = j-1
    print(A)
    while (i >= 0) and (A[i] > chave):
          
          A[i + 1] = A[i]
          
          
          i = i - 1
    
    A[i + 1] = chave
    
print(A) 


    
