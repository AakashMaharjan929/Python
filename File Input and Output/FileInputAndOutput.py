# File Input and Output Example

f = open("demo.txt", "r")
content = f.read()
print(content)
# line=f.readline()
# print(line)
print(type(content))
f.close()

f = open("demo.txt", "a")
f.write("\nThis is new line added to the file.")    
f.close()

f = open("demo.txt", "r")
content = f.read()
print(content)
f.close()

f=open("demo.txt","r+")
content=f.read()
print(content)
f.write("\nAdding another line using r+ mode.")
f.close()

with open("demo.txt","r") as f:
    content=f.read()
    print(content)

with open("demo.txt","r") as f:
    data = f.read()

new_data = data.replace("line", "sentence")

with open("demo.txt","w") as f:
    f.write(new_data)

with open("demo.txt","r") as f:
    data=f.read()
    if(data.find("line")==-1):
        print("The word 'line' is no longer present in the file.")