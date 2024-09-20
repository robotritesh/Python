#WAF to find in which line of the file does the word "learning"occur first. Print -1 if word not found. 

def read_word():
    word = "programming"
    data = True
    line_no = 1
    with open("Day-7/demo.tex","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(read_word())


#From a file containing numbers separated by comma, print the count of even numbers.