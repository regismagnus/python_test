with open("camelot.txt") as song:
    for i in range(0, 1000):
        try:
            print(song.read(i))
        except Exception:
            break
        
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)        
    
    