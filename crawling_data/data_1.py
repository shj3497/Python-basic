filename = "./file/a.bin"
filename1 = "./file/a.txt"
data = 100

with open(filename, "wb") as f:
    f.write(bytearray([data]))

with open(filename1, "wb") as f1:
    f1.write(bytearray([data]))