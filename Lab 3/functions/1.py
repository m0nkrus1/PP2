# 1 
def grams_to_ounces(grams): 
  ounces = grams / 28.3495231 
  return ounces 
 
grams = float(input("Enter weight in grams: ")) 
ounces = grams_to_ounces(grams) 
print("Weight in ounces:", ounces) 
