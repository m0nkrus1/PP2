def from_n_to_0(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number: "))
for num in from_n_to_0(n):
    print(num)