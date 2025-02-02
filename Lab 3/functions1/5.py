# 5 
# function for permutating of a word
def permute(s, answer=""): 
    if len(s) == 0: 
        print(answer) 
        return 
 
    for i in range(len(s)): 
        char = s[i] 
        remaining = s[:i] + s[i+1:] 
        permute(remaining, answer + char) 
 
k = input("Enter a string: ") 
print("All permutations:") 
permute(k)