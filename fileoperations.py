import os
modes=('r','w','a','r+')
#read
def read(filepath,option = "all" ):
    print(filepath)
    if(os.path.exists(filepath)):
        file=open(filepath,modes[0])
        if option == 'all':
            content = file.read()
        elif isinstance(option,int):
            content = file.read(option)
        elif option == 'line':
            content = file.readline()
        elif option == 'lines':
            content = file.readlines()
        else:
            content='invaid option'
        file.close()
        return content
    else:
        return  'file does not exsist'


def write(filepath, content):
    file = open(filepath, modes[1])
    file.write(content)
    file.close
    return "Write operation successful"

def append(filepath, content):
    file = open(filepath, modes[1])
    file.write(content)
    file.close()
    return "appead operation successful"