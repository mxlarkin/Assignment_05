#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Larkin, 2021-Aug-8, Edited File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
dicTbl = []  # list of dictionaries to hold data
dicRow = {}  # data stored in a dictionary row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 1. Exit the program if the user chooses so
        break
    
    if strChoice == 'l': # No elif necessary, as is only reached if strChoice is not 'x'
        # 2. Load existing CD inventory data froim CD text file
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': lstRow[0], 'title': lstRow[1], 'artist': lstRow[2]}
            dicTbl.append(dicRow)
        objFile.close()
        
    elif strChoice == 'a': 
        # 3. Add data to the table (2d-list) each time the user wants to add data
        strID = len(dicTbl) + 1 # automatically assigns a CD Id so no duplicates occur
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        dicTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 4. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        
        for row in dicTbl:
            lststr = ''
            for item in row.values():
                lststr += str(item) + ', '
            print(lststr[:-2])
        print('\n')
            
    elif strChoice == 'd':
        # 5. Delete CD of User's Choice
        delCD = str(input('Enter ID number of CD to Delete: '))
        for i in range(len(dicTbl)):
            if str(dicTbl[i]['id']) == delCD:
                del (dicTbl[i])
                break
        for i in range(len(dicTbl)): # renumbers IDs to prevent duplicates after del row
            j = i + 1
            dicTbl[i]['id'] = j
        
    elif strChoice == 's':
        # 6. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w+')
        for row in dicTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
    else:
        print('Please choose either l, a, i, d, s or x!')


