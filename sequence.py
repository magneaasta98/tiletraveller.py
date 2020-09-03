n = int(input("Enter the length of the sequence: "))
first_int=1
second_int=2
third_int=3

print(first_int)
print(second_int)
print(third_int)

for num in range(3,n):
    next_int=first_int+second_int+third_int
    print(next_int)
    first_int=second_int
    second_int=third_int
    third_int=next_int
    








