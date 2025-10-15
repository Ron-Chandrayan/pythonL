# import pickle
# #reading and writing in text file
# filename='text.txt'

# with open(filename,'w') as file:
#     file.write("hello this is chandrayan paul")
#     file.write("meow meow")

# print("file written and created")

# with open(filename,'r') as file:
#     content=file.read()

# print(content)

# data="hatt lode"

# filename='data.pkl'

# with open(filename,'wb') as file:
#     pickle.dump(data,file)

# print("data saved to binary file")

# with open(filename,'rb') as file:
#     loaded = pickle.load(file)

# print(loaded)

import pickle

filename='text.txt'

with open(filename,'w') as file:
    file.write("hello bro")
    file.write("hi")

print("file created successfully")

with open(filename,'r') as file:
    content=file.read()

print(content)



filenam='data.pkl'

with open(filenam,'wb') as file:
    pickle.dump("Hello this is from binary",file)

print("data written in binary file")

with open(filenam,'rb') as file:
    loaded=pickle.load(file)

print(loaded)


import os
current_dir=os.getcwd()

print(current_dir)

files=os.listdir(current_dir)

print(files)
