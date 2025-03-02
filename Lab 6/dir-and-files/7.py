with open("source.txt", "r", encoding="utf-8") as src, open("destination.txt", "w", encoding="utf-8") as dest:
    dest.write(src.read()) 