import filecmp
import os


print("\nINPUT NUMBER OF FILES WHOSE DUPLICATES YOU WANT TO REMOVE: ")
n=int(input())

for i in range(0,n):

    print("\nGIVE FILE NAME WHOSE DUPLICATES YOU WANT TO REMOVE: \n")

    folder=os.listdir()

    f = input()

    Duplicates=0

    for file in folder:
        if file!= f:
            if filecmp.cmp(f,file):
                os.remove(file)
                Duplicates+=1
            else:
                continue
    
    print("\nDuplicates Removed: ",Duplicates,"\n")

