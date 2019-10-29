"""
Maayan Eliya
-method that make a dictionary contains 2 objects, the values are lists of numbers
-doing NORMALIZE to list 'stap' (num/255)
and check if the first digit after '.' in a number
located in an index in list 'stap' is suitable to the number in that index in 'test' list
"""

import random
def make_dic(dict):
    """
    make dictionary that contains 2 objects: key=str, value=list of nums, by using random 
    :return: the dictionary
    """
    dic= {'stap':[],'test':[]}
    for mun in range(1000):
        dic['stap'].append(random.randint(0,255))
        dic['test'].append(random.randint(0,9))
    return dic


def normlize(dic):
    """
    doing NORMALIZE to list 'stap' (num/255)
    """
    for i in range(1000):
        dic['stap'][i]=dic['stap'][i]/255
    return dic


def check_if_suitable(dic):
    """
    check if the first digit after '.' in a number
    located in an index in list 'stap' is suitable to the number in that index in 'test' list
"""
    mone=0
    for i in range(1000):
        if dic['stap'][i]==1 and dic['test'][i]==1:
            mone=mone+1
        elif int((str(dic['stap'][i]).split('.')[1])[0])==dic['test'][i]:
            mone=mone+1
    return mone/10 #mone/1000*100 = mone/10 = mone in %


def main():
    dic=make_dic(dict)
    dic=normlize(dic)
    print("the precent of suitablaness is ",check_if_suitable(dic),"%")
    
if __name__=="__main__":

    main()

    