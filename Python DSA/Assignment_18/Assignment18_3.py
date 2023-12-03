def foo(a, b, c, *args):
    """
    Computes the length of args.

    Parameters:
    - a (int): First parameter.
    - b (int): Second parameter.
    - c (int): Third parameter.
    - args (tuple): Variable-length arguments.

    Returns:
    int: Length of args.
    """
    return len(args)


def bar(a, b, c, **kwargs):
    """
    Checks if the 'magicnumber' key in kwargs is equal to 7.

    Parameters:
    - a (int): First parameter.
    - b (int): Second parameter.
    - c (int): Third parameter.
    - kwargs (dict): Keyword arguments.

    Returns:
    bool: True if 'magicnumber' is 7, False otherwise.
    """
    return kwargs.get("magicnumber", 0) == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
