#Error Hndling
try:
    with open('testfile.csv', 'r+') as f:
        print('This execution does not happen here')
        for line in f:
            print(line)
except FileNotFoundError:
    print("File doesnot exist in this folder")
    
