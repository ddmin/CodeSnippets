import os
import time

master = os.getcwd()

directories = int(input("Number of directories: "))
subdirectories = int(input("Number of subdirectories: "))
text_files = int(input("Number of text files: "))

for x in range(directories):                               
    directory = str(x)
    print(f'Created directory {x}')
    for y in range(subdirectories):                           
        subdirectory = str(y)
        directory = os.path.join(master, '{}'.format(x))
        directory = os.path.join(directory, '{}'.format(y))
        
        os.makedirs(directory)
        for z in range(text_files):
            os.chdir(directory)
            file = str(z)+'.txt'
            with open(file, 'w') as f:
                f.write('67657472656b74736b727562')
