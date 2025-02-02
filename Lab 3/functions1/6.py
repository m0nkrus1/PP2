# 6 
# function that revers the sentence
def reverse_sentence(sentence): 
    words = sentence.split() 
    reversed_words = words[::-1] 
    return " ".join(reversed_words) 
 
 
k = input("Enter a sentence: ") 
print(reverse_sentence(k)) 