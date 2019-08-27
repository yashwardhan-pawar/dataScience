"""
Created on Feb 15, 2019

@author: code
"""


def listTypeValidator(array, Object):
    if isinstance(array,list):
        for item in array:
            if isinstance(item, Object):
                pass
            else:
                return False
        return True
    else:
        print('Input type is not a list')
        return False


def isNotEmptyArray(array):
    if isinstance(array,list):
        if len(array) > 0:
            return True
        else:
            print('Empty Array')
            return False
    else:
        print('Not an Array')
        return False

def isIntList(array):
    if isNotEmptyArray(array):
        for item in array:
            if isinstance(item, int):
                pass
            else:
                print('Not a valid Integer Array')
                return False
        return True
    else:
        return False

def add_number(array, addNumber):
    if isIntList(array):
        result = arrayAdditionIterator(array,addNumber)
        print(result)
        return result
    else:
        print('Invalid Request')
        return None
        #     if add_num
        #     array_len[i] =
        # for item in array:
        #     array[len(array)]

def arrayAdditionIterator(array, addNumber):
    if isIntList(array):
        array_len = len(array)
        return_array = []
        i = array_len
        carry_over = 0
        itr = -1
        while itr != 0 : #and i != 0:  #i != 0:
            # print(str(i) + '. At pos '+str(i-1))
            if i == array_len:
                add_num = array[i - 1] + addNumber + carry_over
            elif i <= 0:
                add_num = carry_over
            else:
                add_num = array[i - 1] + carry_over
            # print('For (' + str(array_len - i) + '), At begning: Addition: ' + str(add_num) + '. To be added: ' + str((add_num % 10)) + '. CarryOver: ' + str(carry_over) + ', +num: ' + str(addNumber))
            if add_num > 9:
                carry_over = int(add_num / 10)
            else:
                # itr=0
                carry_over = 0
            if carry_over == 0 and i <= 0:
                itr = 0
            # print('For ('+str(array_len-i)+'), At End: Addition: ' + str(add_num) + '. To be added: '+ str((add_num%10)) + '. CarryOver: '+ str(carry_over)+ ', +num: ' + str(addNumber))
            return_array.append(add_num % 10)
            add_num = 0
            i -= 1
        return_array.reverse()
        return return_array
    else:
        return []

def call_func():
    test_array = [3,4,5,2,9]
    test_array = [9,9,9]
    print(listTypeValidator([['a'], [1,2]], list))
    add_number([9,9], 1098860)


if __name__ == '__main__':
    call_func()