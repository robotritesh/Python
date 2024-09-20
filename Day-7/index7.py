#Search if the word "learning" exists in the file or not.
# word = "learning"

# with open("Day-7/demo.tex","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")

def for_word():
    word = "learning"
    with open("Day-7/demo.tex","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")


for_word()