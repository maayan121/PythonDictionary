"""
Maayan Eliya
-method that make a dictionary contains 3 objects
-method that chacks if str is a key in dictionary
"""

def make_dictionary ():
    """
    make dictionary that contains 3 objects: key=str, value=int 
    :return: the dictionary
    """
    dict={}
    for x in range (3):
        key=input("please enter string (key) ")
        value=int(input("please enter integer number (value) "))
        dict[key]=value
    return dict


def str_in_dict(dict):
    """
    checks if str that was inputed is a key in dictionary.
    if it is: prints yes
    else: prints no
    """
    str=input("please type a string to check if it in the dictionary ")
    if str in dict:
        print("yes")
    else:
        print("no")



def main():

    dict=make_dictionary ()
    print(dict)
    str_in_dict(dict)


if __name__ == '__main__':
    main()