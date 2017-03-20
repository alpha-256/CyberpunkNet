from time import sleep as wait
with open("story.txt","r") as f:
    for line in f:
        if '\n' == line[-1]:
            line = line[:-1]
            wait(0.5)
            print(line)
