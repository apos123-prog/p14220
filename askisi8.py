# p14220
p14220 ergasia eisagwgi stin epistimi twn upologistwn



counter = 0
file_name = input('Enter file name:')
with open(file_name) as f:
    data = f.read()
    for i in range(0,len(data)-1, 2):
        if data[i] in ascii_string and data[i+1] in ascii_string:
            counter+=1
print("Total number of 2 ASCII characters: ", str(counter))
