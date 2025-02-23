import re

strings = ["ab", "acb", "a123b", "aXYZb", "a_b", "b", "ba", "abc", "aabb"]

pattern = r'^a.*b$'

matches = [s for s in strings if re.fullmatch(pattern, s)]

if matches:
    print("Matching strings:", matches)
else:
    print("No match found.")
