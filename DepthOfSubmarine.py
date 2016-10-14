#! /usr/bin/env python
#This program reads in each line of a file containing several colums of data, split it into separate components, 
#returns some calculated values, and write certain output to a separate file.

#Set the input file name: Open the file contains the data and make InFileName-string that contains the path of the file to be opened
InFileName = "ctd.txt"

#Open the input for reading: Infile is the object allows to interact with file (InFileName)and content in read only
InFile = open(InFileName, 'r')
#Open the output file called MaxDepth: redirect with 'w' and append with 'a'
OutFile = open("MaxDepth.txt", 'a')

#Initialize the counter used to keep track of line numbers: need to skip first line (header) of ctd.txt
LineNumber = 0
#Initial time and depth
StartTime = 0.00
Length800 = 0.00
#Define the MaximumDepth
MaximumDepth = 800.00

#Loop over each line in the file
for Line in InFile:
	if LineNumber > 0:
		#Remove the line ending character
		Line=Line.strip('\n')
		#Parsing data from lines
		LineList=Line.split(',')
		#Access individual line from the line list (we are interested in Depth value)
		Depth = float(LineList[4])
		#print Depth
		#print "%d: Date: %s\tDepth: %s" %(LineNumber, LineList[1], LineList[4])
		#print LineList[1],LineList[4]
		#Parsing time
		TimeResult = LineList[1].split(' ')[1]
		#print TimeResult[1]
		#Convert all time units into hours
		Hour = float(TimeResult.split(':')[0])
		Minute = float(TimeResult.split(':')[1])
		Second = float(TimeResult.split(':')[2])
		Time = float("%.2f" %(Hour + Minute/60 + Second/3600))
		#print LineNumber, Time
		#print "%.2f%s\t%.2f" % (Time, Depth)
		#print "%d: Time %.2f\tDepth: %.2f" %(LineNumber, Time, Depth)
		if LineNumber == 1:
			StartTime = Time #getting start time
		#Get time and depth of the first recording to the depth of 800 m
		if 800.00 < Depth <801.00:
			Time801 = Time
			Depth801 = Depth
		#Record how long the submarine went below 800 m
		elif Depth >= MaximumDepth:
			MaximumDepth = Depth
			Time800 = Time
			Depth800 = Depth
			#Define the time length
			Length800 = Length800 + Time
			#print Length800
			#print "%d: Time %.2f\tDepth: %.2f" %(LineNumber, Time800, Depth800)
	LineNumber = LineNumber + 1

#Calculate and print how long it took to go from the first recording to a depth of 800 m
TimeFirstToLast = Time801 - StartTime
print "Question1_Answer: %.2f hours for the submarine to dive to the first 800 m record with depth of %.2f m.\n" %(TimeFirstToLast, Depth801)

#Calculate and print how long the submarine was below 800 m
TimeBelow800 = Length800 - Time801
print "Question2_Answer: total time for the submarine stay below 800 m is %2.f hours.\n" %(TimeBelow800)

#Question3_Answer: Write a file that has the maximum depth for the dive
OutFile.write ("Question3_Answer: Maximum depth for the dive is %.2f meters.\n" %(MaximumDepth))
#Close the files
InFile.close()
OutFile.close()
