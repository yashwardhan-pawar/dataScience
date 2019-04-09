


f = open("inputTest.sql")
# print(f.read())


def listAllLoops(file, strtLoop:str, endLoop:str):
	fileContent:str = file.read()
	fileContent = fileContent.upper()
	# print(fileContent)
	lineCount:int = 0
	listInfo:list=[]
	for lines in fileContent.splitlines():
		lineCount += 1
		# print(lines)
		if lines.__contains__(strtLoop.upper()):
			listInfo.append({'START': lineCount})
			# print("Start of loop at line number: " + str(lineCount))
		if lines.__contains__(endLoop.upper()):
			listInfo.append({'END': lineCount})
			# print("End of loop at line number: " + str(lineCount))
	print(listInfo)
	return listInfo


def strtparser(listInput:list):
	tempList:list = listInput
	i:int = 0
	level:int=0
	retunDict: dict = {}
	strtList: list = []
	endList: list = []
	levelstrtList: list = []
	levelendList: list = []
	while len(tempList) != 0:
		if len(tempList) > 1:
			nthPosDict:dict = tempList[i]
			nthPlusOnePosDict:dict = tempList[i+1]
		else:
			nthPosDict:dict = tempList[0]
			nthPlusOnePosDict:dict = tempList[0]

		if ('START' in nthPosDict) and ('START' in nthPlusOnePosDict):
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('*START [' + str(level) + ']: line' + str(nthPosDict))
			levelstrtList.append(nthPosDict.get('START'))
			tempList.pop(i)
			strtparser(tempList)
			level+=1
		elif ('START' in nthPosDict) and level > 0:
			# level+=1
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('#START [' + str(level) + ']: line' + str(nthPosDict))
			levelstrtList.append(nthPosDict.get('START'))
			tempList.pop(i)
		elif 'START' in nthPosDict:
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('~START [' + str(level) + ']: line' + str(nthPosDict))
			strtList.append(nthPosDict.get('START'))
			tempList.pop(i)
		else:
			tempList.pop(i)
	strtList.extend(levelstrtList)
	print(strtList)

def endparser(listInput: list):
	tempList:list = listInput
	i: int = 0
	level: int = 0
	endList: list = []
	levelendList: list = []
	while len(tempList) != 0:
		if len(tempList) > 1:
			nthPosDict: dict = tempList[i]
			nthPlusOnePosDict: dict = tempList[i + 1]
		else:
			nthPosDict: dict = tempList[0]
			nthPlusOnePosDict: dict = tempList[0]

		if ('END' in nthPosDict) and ('END' in nthPlusOnePosDict):
			# print('END['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('*END[' + str(level) + ']: line' + str(nthPosDict))
			levelendList.append(nthPosDict.get('END'))
			tempList.pop(i)
			endparser(tempList)
			level -= 1
		elif ('END' in nthPosDict) and level > 0:
			# level-=1
			# print('END['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('#END[' + str(level) + ']: line' + str(nthPosDict))
			levelendList.append(nthPosDict.get('END'))
			tempList.pop(i)
		elif 'END' in nthPosDict:
			# print('END ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('~END [' + str(level) + ']: line' + str(nthPosDict))
			tempList.pop(i)
			endList.append(nthPosDict.get('END'))
		else:
			tempList.pop(i)
		# i+=1
		# retunDict[strtList]=endList
		# print(retunDict)

	levelendList.reverse()
	endList.extend(levelendList)
	print(endList)





def mainParser(file, strtLoop:str, endLoop:str):
	fileTemp = file
	strtReturnList:list = listAllLoops(file,strtLoop,endLoop)
	# int_init:int = 0
	# while int_init < len
	# print(strtReturnList)
	strtparser(strtReturnList)
	print(fileTemp)
	print(fileTemp.read())

	endReturnList = listAllLoops(fileTemp,strtLoop,endLoop)
	print(endReturnList)
	endparser(endReturnList)



print(__name__)
if __name__ == '__main__':
	print('Run Executed from File')
	mainParser(f, 'begin', 'end;')
	# testList = ['a','b','c','d','e']
	# testList.pop(0)
	# print(testList)
	# testList.pop(0)
	# print(testList)
	# testList.pop(0)
	# print(testList)
	# testList.pop(0)
	# print(testList)
	# testList.pop(0)
	# print(testList)