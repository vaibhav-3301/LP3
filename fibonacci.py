def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
nterms = int(input("How many terms? "))  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))

first_num = int(input("Enter the first number of the fibonacci series... "))
second_num = int(input("Enter the second number of the fibonacci series... "))
num_of_terms = int(input("Enter the number of terms... "))
print(first_num,second_num)
print("The numbers in fibonacci series are : ")
while(num_of_terms-2):
   third_num = first_num + second_num
   first_num=second_num
   second_num=third_num
   print(third_num)
   num_of_terms=num_of_terms-1