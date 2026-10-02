num = int(input("Enter the Fibonacci sequence length to be generated:"))
first_term = 0
second_term = 1
print("The Fibonacci deries with",num,"term is:")
print(first_term, second_term, end=" ")
for i in range(2,num):
    cur_term = first_term+second_term
    print(cur_term, end=" ")
    first_term = second_term
    second_term = cur_term
