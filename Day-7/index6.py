#WAF that replacesall occurrences of "Java" with "python" in above file.
with open("Day-7/demo.tex","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("Day-7/demo.tex","w") as f:
    f.write(new_data)