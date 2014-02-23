##XZY Spacer - checks for difference in x, y or z then puts a space in the file.
##This is usefull for opening up point clouds in Mastercam.
##Selecting options-> open as splines, creates a spline per block of XYZ points separated by that space. 
##Alvaro Gil 2014-02-22

import csv
import os
import sys
import string

infile="xyzin.txt"
outfile="xyzout.txt"
rownum = 0
colnum = 0
header = "XYZ"
X = float(0)
Y = float(0)
Z = float(0)
lastX = float(0)
lastY = float(0)
lastZ = float(0)
watchvar = str("NONE")
watchcol = -1
tolerance = float(.001) 
verbose = str("N")
spacenum = int(0)

if os.path.isfile(outfile):  #removes the old file if it exists
        os.remove(outfile)

watchvar = input("Enter variable to watch - X, Y, or Z: ").upper()
tolerance = float(input("Enter Tolerance: "))
verbose = input("Verbose? - Y or N: ").upper()


if watchvar == 'X':
                watchcol = 0
if watchvar == 'Y':
                watchcol = 1
if watchvar == 'Z':
                watchcol = 2
if watchcol < 0:
        print("Only X, Y or Z values are allowed. Program terminated.")
        sys.exit("only X, Y or Z values allowed")

csvfile = open(infile)

dialect = csv.Sniffer().sniff(csvfile.read(1024))
csvfile.seek(0)

print(" ") 
#print("The Delimiter is [", dialect.delimiter, "]") #can't get this to work
print("Watching for change in[", watchvar, "Column",watchcol,"Tolerance",tolerance,"]")
print(" ") 

reader = csv.reader(csvfile, dialect)
# ... process CSV file contents here ...
reader = csv.reader(open(infile), delimiter=dialect.delimiter, quoting=csv.QUOTE_NONE)

csvfile2 = open(outfile, 'a', newline='') #this opens the file
with csvfile2 as csvfile2: 
 for row in reader:
    colnum = 0

    for col in row:

            #print("Column Number:", colnum, "Row Number:", rownum)
            #print(header[colnum], col)
            if colnum==0:
                X=float(col)
            if colnum==1:
                Y=float(col)
            if colnum==2:
                Z=float(col)
            if rownum == 0: #removes extra space on first line.
                lastX=float(X)     #removes extra space on first line.
                lastY=float(Y)     #removes extra space on first line.
                lastZ=float(Z)     #removes extra space on first line.
                
            colnum += 1

    if tolerance < (abs(abs(lastX)-abs(X))) and watchcol == 0:
      #if lastX != X and watchcol == 0: #X variable and Colum 0
        if verbose == 'Y':
           print("---------- NEW X PASS ----------")
        xyzspacer = csv.writer(csvfile2, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        #xyzspacer.writerow("---------- NEW X PASS ----------") 
        xyzspacer.writerow(" ")
        spacenum += 1  
    if tolerance < (abs(abs(lastY)-abs(Y))) and watchcol == 1:            
     #if lastY != Y and watchcol == 1:  #Y variable and Colum 1
        if verbose == 'Y':
           print("---------- NEW Y PASS ----------")
        xyzspacer = csv.writer(csvfile2, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        #xyzspacer.writerow("---------- NEW Y PASS ----------") 
        xyzspacer.writerow(" ")
        spacenum += 1  
    if tolerance < (abs(abs(lastZ)-abs(Z))) and watchcol == 2:
     #if lastZ != Z and watchcol == 2: #Z variable and Colum 2
        if verbose == 'Y':    
           print("---------- NEW Z PASS ----------")
        xyzspacer = csv.writer(csvfile2, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        #xyzspacer.writerow("---------- NEW Z PASS ----------") 
        xyzspacer.writerow(" ")
        spacenum += 1    
    if verbose == 'Y':        
       print("XYZ FROM VARIABLES: ", X, Y, Z) #writes to terminal
    xyzspacer = csv.writer(csvfile2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    xyzspacer.writerow([X, Y, Z]) #writes to file #<------ ? error
    	
    lastX=float(X) #Saves the last x value
    lastY=float(Y) #Saves the last y value
    lastZ=float(Z) #Saves the last z value

    
    rownum += 1
print("Analyzed ", rownum, "coordinates.")
print("Added", spacenum, "spaces to ", outfile)




