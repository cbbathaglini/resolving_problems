# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    #cat_A = abs(x - z)
    #cat_B = abs(y - z)
    if(abs(x - z) < abs(y - z)):
        return "Cat A"
    elif(abs(x - z) > abs(y - z)):
        return "Cat B"
    else:
        return "Mouse C"