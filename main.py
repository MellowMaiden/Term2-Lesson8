#Term2-Lesson8:work with files
import csv # this is needed to read CSV files
with open("database.csv.csv",encoding='utf-8-sig') as f:#the code here is for the csv file only
    #this reads f and puts the result in csvRead
    csvRead=csv.reader(f)
    for row in csvRead:
        print(row)#print every line
#now that we are outside "with" the file automatically closes
#let us print the rows

#if we just want to print age
import csv # this is needed to read CSV files
with open("database.csv.csv") as f:#the code here is for the csv file only
    #this reads f and puts the result in csvRead
    csvRead=csv.reader(f)
    for row in csvRead:
        print(row[1])#print every line

import csv
try:
    f=open("books.csv","r")
    f.close()
    print("Book database found")
except FileNotFoundError:
    f=open("books.csv","w")
    f.write("name,price")
    f.close()
    print("Creating database file")

choice=input("Do you want to add to the database or search it? Type ADD or SEARCH.")
if choice.upper()=="ADD":
    while True:
        name = input("name:")
        price=input("price:")
        if name =="":
            break
        else:
            f=open("books.csv","a")
            f.write("\n"+name+","+price)
            f.close()
else:
    name=input("name:")
    found=False
    with open("books.csv",encoding='utf-8-sig') as f:
        readCSV=csv.reader(f)
        for row in readCSV:
            if row[0].lower()==name.lower():
                found=True
                print("Book Found, its price is", row[1])
    if found == False:
        print("Book Not Found")