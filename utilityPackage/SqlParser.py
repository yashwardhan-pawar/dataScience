



# print(f.read())
from builtins import list


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
	i:int = 0
	level:int=0
	retunDict: dict = {}
	strtList: list = []
	endList: list = []
	levelstrtList: list = []
	levelendList: list = []
	while len(listInput) != 0:
		if len(listInput) > 1:
			nthPosDict:dict = listInput[i]
			nthPlusOnePosDict:dict = listInput[i+1]
		else:
			nthPosDict:dict = listInput[0]
			nthPlusOnePosDict:dict = listInput[0]



		if ('START' in nthPosDict) and ('START' in nthPlusOnePosDict):
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('*START [' + str(level) + ']: line' + str(nthPosDict))
			levelstrtList.append(nthPosDict.get('START'))
			listInput.pop(i)
			strtparser(listInput)
			level+=1
		elif ('START' in nthPosDict) and level > 0:
			level+=1
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('#START [' + str(level) + ']: line' + str(nthPosDict))
			levelstrtList.append(nthPosDict.get('START'))
			listInput.pop(i)
		elif 'START' in nthPosDict:
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('~START [' + str(level) + ']: line' + str(nthPosDict))
			strtList.append(nthPosDict.get('START'))
			listInput.pop(i)
		# else:
		# 	listInput.pop(i)

		if ('END' in nthPosDict) and ('END' in nthPlusOnePosDict):
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('*END [' + str(level) + ']: line' + str(nthPosDict))
			levelendList.append(nthPosDict.get('END'))
			listInput.pop(i)
			# strtparser(listInput)
			level -= 1
		elif ('END' in nthPlusOnePosDict) and level > 0:
			level-=1
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('#END [' + str(level) + ']: line' + str(nthPosDict))
			levelendList.append(nthPosDict.get('END'))
			listInput.pop(i)
		elif 'END' in nthPosDict:
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('~END [' + str(level) + ']: line' + str(nthPosDict))
			endList.append(nthPlusOnePosDict.get('END'))
			listInput.pop(i)
		# else:
		# 	listInput.pop(i)
		# if level > 0:
			# strtparser(listInput)


	strtList.extend(levelstrtList)
	print(strtList)


	if len(levelendList) > 0:
		print(levelendList)
	# endList.extend(levelendList)
	if len(endList) > 0:
		print(endList)


def endparser(listInput: list):
	i:int = 0
	level:int=0
	endList: list = []
	levelendList: list = []
	while len(listInput) != 0:
		if len(listInput) > 1:
			nthPosDict:dict = listInput[i]
			nthPlusOnePosDict:dict = listInput[i+1]
		else:
			nthPosDict:dict = listInput[0]
			nthPlusOnePosDict:dict = listInput[0]

		if ('END' in nthPosDict) and ('END' in nthPlusOnePosDict):
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('*END [' + str(level) + ']: line' + str(nthPosDict))
			levelendList.append(nthPosDict.get('END'))
			listInput.pop(i)
			# endparser(listInput)
			level+=1
		elif ('END' in nthPosDict) and level > 0:
			# level+=1
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('#END [' + str(level) + ']: line' + str(nthPosDict))
			levelendList.append(nthPosDict.get('END'))
			listInput.pop(i)
		elif 'END' in nthPosDict:
			# print('START ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
			print('~END [' + str(level) + ']: line' + str(nthPosDict))
			endList.append(nthPosDict.get('END'))
			listInput.pop(i)
		else:
			listInput.pop(i)
	if len(levelendList) > 0:
		print(levelendList)
	# endList.extend(levelendList)
	if len(endList) > 0:
		print(endList)

	
	
	
	
	
	
	
	
	
	
	
	
	# 
	# listInput:list = listInput
	# i: int = 0
	# level: int = 0
	# endList: list = []
	# levelendList: list = []
	# while len(listInput) != 0:
	# 	listInput.remov(i)
	# 	if len(listInput) > 1:
	# 		nthPosDict: dict = listInput[i]
	# 		nthPlusOnePosDict: dict = listInput[i+1]
	# 	else:
	# 		nthPosDict: dict = listInput[0]
	# 		nthPlusOnePosDict: dict = listInput[0]
	# 
	# 	if ('END' in nthPosDict) and ('END' in nthPlusOnePosDict):
	# 		# print('END['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
	# 		print('*END[' + str(level) + ']: line' + str(nthPosDict))
	# 		levelendList.append(nthPosDict.get('END'))
	# 		endparser(listInput)
	# 		level += 1
	# 	elif ('END' in nthPosDict) and level > 0:
	# 		# level-=1
	# 		# print('END['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
	# 		print('#END[' + str(level) + ']: line' + str(nthPosDict))
	# 		levelendList.append(nthPosDict.get('END'))
	# 	elif 'END' in nthPosDict:
	# 		# print('END ['+str(level)+']: line'+str(nthPosDict)+ ' & '+str(nthPlusOnePosDict))
	# 		print('~END [' + str(level) + ']: line' + str(nthPosDict))
	# 		endList.append(nthPosDict.get('END'))
	# 	# i+=1
	# 	# retunDict[strtList]=endList
	# 	# print(retunDict)
	# 
	# # endList.extend(levelendList)
	# print(levelendList)
	# 
	# # levelendList.reverse()
	# # endList.extend(levelendList)
	# print(endList)





def mainParser(file, strtLoop:str, endLoop:str):
	file = open("inputTest.sql")
	strtReturnList:list = listAllLoops(file,strtLoop,endLoop)
	strtparser(strtReturnList)
	# fileTemp = open("inputTest.sql")
	# endReturnList = listAllLoops(fileTemp,strtLoop,endLoop)
	# endReturnList.reverse()
	# print(endReturnList)
	# endparser(endReturnList)



print(__name__)
if __name__ == '__main__':
	print('Run Executed from File')
	f = open("inputTest.sql")
	mainParser(f, 'begin', 'end;')
	# testList = ['a','b','c','d','e']
	# testList.remov(0)
	# print(testList)
	# testList.remov(0)
	# print(testList)
	# testList.remov(0)
	# print(testList)
	# testList.remov(0)
	# print(testList)
	# testList.remov(0)
	# print(testList)