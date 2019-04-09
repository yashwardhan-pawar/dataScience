

f = open("inputTest.sql")


def fileMeta(inputFile,strtString:str, endString:str):
	fileContent:str = inputFile.read()
	fileContent = fileContent.upper()
	lineCount:int = 0
	listInfo:list=[]
	for lines in fileContent.splitlines():
		lineCount += 1
		if lines.__contains__(strtString.upper()):
			listInfo.append({'START': lineCount})
		if lines.__contains__(endString.upper()):
			listInfo.append({'END': lineCount})
	print(listInfo)
	return listInfo

def parse(inputList:list):
	i:int = 0
	stratEleList:list = []
	stratEleLevelList:list = []
	endEleList:list = []
	level:int=0
	# while len(inputList) != 0:
	while i < len(inputList):
		# if len(inputList) > 1:
		# if i != 0:
		# 	ele:dict = inputList[i-1]
		# 	eleNext:dict = inputList[i]
		# else:
		# 	ele:dict = inputList[i]
		# 	eleNext:dict = inputList[i]
		ele: dict = inputList[i]
		if i > 0:
			ele:dict = inputList[i]
			eleLast:dict = inputList[i-1]
			if ('START' in ele) and ('START' in eleLast):
				level+=1
				# print('Drilling down a level[' + str(level) + ']: ' + str(ele.get('START')))
				print((' ---****--- ' * (level+1)) + ' Starts: ' +  str(ele.get('START')))
				# stratEleList.append(ele.get('START'))
				# inputList.pop(i)
				# parse(inputList)
			elif ('START' in ele) and ('END' in eleLast):
				# print('Open at same level[' + str(level) + ']: ' + str(ele.get('START')))
				print((' ---****--- ' * (level+1)) + ' Starts: ' + str(ele.get('START')))
				# stratEleList.append(ele.get('START'))
				# print('Inserting at same level: '+str(ele.get('START')))
				# inputList.pop(i)
			elif ('END' in ele) and ('END' in eleLast):
				level-=1
				# print('Going up a level[' + str(level) + ']: ' + str(ele.get('END')))
				print((' ---****--- ' * (level+1)) + ' Ends: ' + str(ele.get('END')))
				# print('*****')
				# inputList.pop(i)
			elif ('END' in ele) and ('START' in eleLast):
				# print('Closing at same level[' + str(level) + ']: ' + str(ele.get('END')))
				print((' ---****--- ' * (level+1)) + ' Ends: ' + str(ele.get('END')))
		else:
			# print('At same level[' + str(level) + ']: ' + str(ele.get('START')))
			print((' ---****--- ' * (level + 1)) + ' Starts: ' + str(ele.get('START')))
		i+=1
	# print(stratEleList)







metaList:list = fileMeta(f, 'begin', 'end;')
parse(metaList)