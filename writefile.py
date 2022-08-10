f = open("f:\\RahulKR\\Class XII\\Computer Studies\\mydemofile.txt","a")
#Note the arguement vale - a is for append
# if you put w - it will overwrite
f.write("adding more lines to it")
f.close()

f = open("f:\\RahulKR\\Class XII\\Computer Studies\\mydemofile.txt","r")
#print(f.readline())
#read next line
#keep doing print(f.readline())

#Note - if we want a new file, you can use open with a new file name and parameter x
#myFile = open("e:\\my docs\python proj\newfile.txt","x")
#note newfile should not exist. If it exists - will give error


#you can also use the for statement to read each linee
lineNum = 1
for myLine in f:
	print("reading ", lineNum , " with in for ", myLine)
	lineNum = lineNum + 1

f.close()
