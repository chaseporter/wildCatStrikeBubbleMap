g = open("parsedTxt2.csv", "w+")

catDict = {"h": "", "wf": "", "t":"", "o":"", "f":""}

with open("copy.csv") as file_in:
    for line in file_in:
    	newline = line.split(",")
    	if newline[4].split('\n')[0] in catDict:
    		catDict[newline[4].split('\n')[0]] += line

    for cat in catDict:
    	for line in catDict[cat]:
    		g.write(line)
    	print(cat)
    	print(len(catDict[cat].split('\n')) - 1)
g.close()