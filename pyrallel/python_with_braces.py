with open("./input.py") as file, open("./output.py", "+a") as output:
    
    for line in file:
        if ('{' in line):
            line = line.replace('{', ':')
        elif ('}' in line):
            line = line.replace('}', '')
            
        output.write(line)


print("✨ Pythonized ✨")
