from utilityPackage import FileUtility as fu

file = fu.Files('C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/user.json')
# file = fu.Files('C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/data_twitter.csv')

# print(file.readFile(10))
lines = file.readFile(10)

print(lines)
# for line in lines:
#     print(line)

# i = 0
# for lines in file.readFile(10):
#     if i is 15:
#         break
#     print(lines)
#     i += 1
