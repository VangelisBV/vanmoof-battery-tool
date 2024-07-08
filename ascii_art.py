def display_v(height: int):
    """
    Displays a static 'V' shape with the given height.

    :param int height: The number of lines
    """
    for i in range(height):
        if i == height - 1:
            line = " " * i + "\\\//"  
        else:
            line = " " * i + "\\\\" + " " * (2 * (height - i - 1)) + "//"
        print(line)