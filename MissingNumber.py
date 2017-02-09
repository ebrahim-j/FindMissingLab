def find_missing(list1, list2):

    inputList = [] #list with extra number
    checkList = [] #template list
    if len(list1) > len(list2): #determines the variable (input and check)lists will be assigned to
        inputList = list1
        checkList = list2
    else:
        inputList = list2
        checkList = list1

    missing_num = [] #missing number to be stored in array
    for i in inputList:
       if i not in checkList: #if current number not in template list, that is added to missing list array
        missing_num.append(i)
    if len(missing_num) == 0: #if no outstanding number/value found
      return 0
    return missing_num.pop()
    
