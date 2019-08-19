import json
import re

# def fetchJsonKeysAsList(lines, primaryColumnList:list, secondaryColumnList:list, attributeKey:str=None, breakAfterLines:int=None):
# 	# primaryColumnList:list = []
# 	# secondaryColumnList: list = []
# 	i:int=0
# 	for line in lines:
# 	# for line in fileToread.readlines(breakAfterLines):
# 		i += 1
# 		# print('Line [' + str(i) + ']: ' + line)
# 		toJson:json = json.loads(line)
#
# 		if breakAfterLines is not None:
# 			if i >= breakAfterLines:
# 				break
#
# 		if attributeKey is not None:
# 			if toJson[attributeKey] is not None:
# 				# print(toJson[attributeKey])
# 				for key in toJson[attributeKey]:
# 					if isinstance(toJson[attributeKey][key], str):
# 						if toJson[attributeKey][key].startswith('{'):
# 							if key not in secondaryColumnList:
# 								secondaryColumnList.append(key)
# 						elif convertCamelToUnderScoreUpper(key) not in primaryColumnList:
# 							primaryColumnList.append(convertCamelToUnderScoreUpper(key))
# 					elif isinstance(toJson[attributeKey][key], dict):
# 						if key not in secondaryColumnList:
# 							secondaryColumnList.append(key)
# 					elif convertCamelToUnderScoreUpper(key) not in primaryColumnList:
# 						primaryColumnList.append(convertCamelToUnderScoreUpper(key))
#
# 					# if isinstance(toJson[attributeKey][key], str):
# 					# 	if toJson[attributeKey][key].startswith('{') :
# 					# 		if key not in secondaryColumnList:
# 					# 			secondaryColumnList.append(key)
# 					# elif convertCamelToUnderScoreUpper(key) not in primaryColumnList:
# 					# 	primaryColumnList.append(convertCamelToUnderScoreUpper(key))
# 		else:
# 			for key in toJson:
# 				# print('Key['+key+'] is instance of '+str(type(toJson[key])))
# 				if isinstance(toJson[key], str):
# 					if toJson[key].startswith('{') :
# 						if key not in secondaryColumnList:
# 							secondaryColumnList.append(key)
# 					elif key.upper() not in primaryColumnList:
# 						primaryColumnList.append(key.upper())
# 				elif isinstance(toJson[key], dict):
# 					if key not in secondaryColumnList:
# 						secondaryColumnList.append(key)
# 				elif key.upper() not in primaryColumnList:
# 					primaryColumnList.append(key.upper())
#
# 	primList:list = []
# 	secList: list = []
# 	primList = primaryColumnList
# 	secList = secondaryColumnList
# 	#itrList:list = secondaryColumnList
# 	print(primList)
# 	print(secList)
# 	print(secList.__len__())
#
# 	if secList.__len__() > 0:
# 		j = 0
# 		while j < secList.__len__():
# 			print('For '+secList[j]+':')
# 			fetchJsonKeysAsList(lines, primList, secList, secList[j])
# 			j+=1
# 	return i

def fetchJsonKeysAsList(lines, attributeKey:str=None, breakAfterLines:int=None, level:int=None):
	if level is None:
		level = 1
	else:
		level += 1

	primaryColumnList:list = []
	secondaryColumnList: list = []
	i:int=0
	for line in lines:
	# for line in fileToread.readlines(breakAfterLines):
		i += 1
		# print('Line [' + str(i) + ']: ' + line)
		toJson:json = json.loads(line)

		if breakAfterLines is not None:
			if i >= breakAfterLines:
				break

		if attributeKey is not None:
			if toJson[attributeKey] is not None:
				# print(toJson[attributeKey])
				for key in toJson[attributeKey]:
					if isinstance(toJson[attributeKey][key], str):
						if toJson[attributeKey][key].startswith('{'):
							if key not in secondaryColumnList:
								secondaryColumnList.append(key)
						elif convertCamelToUnderScoreUpper(key) not in primaryColumnList:
							primaryColumnList.append(convertCamelToUnderScoreUpper(key))
					elif isinstance(toJson[attributeKey][key], dict):
						if key not in secondaryColumnList:
							secondaryColumnList.append(key)
					elif convertCamelToUnderScoreUpper(key) not in primaryColumnList:
						primaryColumnList.append(convertCamelToUnderScoreUpper(key))

					# if isinstance(toJson[attributeKey][key], str):
					# 	if toJson[attributeKey][key].startswith('{') :
					# 		if key not in secondaryColumnList:
					# 			secondaryColumnList.append(key)
					# elif convertCamelToUnderScoreUpper(key) not in primaryColumnList:
					# 	primaryColumnList.append(convertCamelToUnderScoreUpper(key))
		else:
			for key in toJson:
				# print('Key['+key+'] is instance of '+str(type(toJson[key])))
				if isinstance(toJson[key], str):
					if toJson[key].startswith('{') :
						if key not in secondaryColumnList:
							secondaryColumnList.append(key)
					elif key.upper() not in primaryColumnList:
						primaryColumnList.append(key.upper())
				elif isinstance(toJson[key], dict):
					if key not in secondaryColumnList:
						secondaryColumnList.append(key)
				elif key.upper() not in primaryColumnList:
					primaryColumnList.append(key.upper())


	if level > 1:
		secList = []
		primList = []
	else:
		primList = primaryColumnList
		secList = secondaryColumnList

	#itrList:list = secondaryColumnList
	# print(primList)
	# print(secList)
	# print(secList.__len__())
	returnDict: dict = {'PRIMARY': primaryColumnList, 'SECONDARY' : secondaryColumnList, 'LEVEL' : level}
	print(returnDict)

	if secList.__len__() > 0:
		j = 0
		while j < secList.__len__():
			print('For '+secList[j]+':')
			fetchJsonKeysAsList(lines, secList[j], None, level)
			j+=1


	return 	returnDict



def convertCamelToUnderScoreUpper(value):
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).upper()

def convertCamelToUnderScoreLower(value):
	s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
