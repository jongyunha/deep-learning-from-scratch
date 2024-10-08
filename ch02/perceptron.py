import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    theta = -0.7
    temp = np.sum(weight*x) + theta
    if temp <= 0:
        return 0

    return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([-0.5, -0.5])
    theta = 0.7
    temp = np.sum(weight * x) + theta
    if temp <= 0:
        return 0

    return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    theta = -0.2
    temp = np.sum(weight * x) + theta
    if temp <= 0:
        return 0

    return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)

    return y

if __name__ == "__main__":
    print(XOR(0, 0))
    print(XOR(1, 0))
    print(XOR(0, 1))
    print(XOR(1, 1))
