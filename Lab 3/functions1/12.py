# 12
def histogram(lst):
    for num in lst:
        print('*' * num)
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
histogram(numbers)
