"""
Maayan Eliya
-method that make a dictionary contains x**2 for x in range(5)
"""

def make_dictionary ():
    """
    make dictionary that contains x**2 for the numbers in range(5) -> key=x, value=x**2
    :return: the dictionary
    """
    dict={}
    for x in range(5):
        dict[x]=x**2
    return dict


def main():
    dict=make_dictionary ()
    print(dict)


if __name__ == '__main__':
    main()