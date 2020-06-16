g = open("parsedTxt.csv", "w+")

with open("strikeMap.kml") as file_in:
    check = False
    for line in file_in:
    	if check:
    		newline = line.split(",")
    		g.write(", " + newline[1] + ", " + newline[0].split()[0] + "\n")
    		check = False
    	if "<coordinates>" in line:
    		check = True

g.close()