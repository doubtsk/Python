import numpy as np
pytuple = (4, 5, 6)
l1 = np.array(pytuple)
# print(l1)
# print("\n")
# print(l1[0])
# print("\n")
pylist = [0, 1, 2]
l2 = np.array(pylist)
# print(l2)
# print("\n")
pylist1 = [1, 2, 3]
pylist2 = [4, 5, 6]
l3 = np.array([pylist1, pylist2])
mar = l3.T
# print(mar.size)
# print(mar.shape)
for item in mar.flat:  # flat:一维数组迭代器
    print(item)

print("\n")

# print(mar.nbytes)
# print(mar.dtype)
mar1 = np.arange(0, 10, 1)
# print(mar1)
# print(mar1.dtype)

black=np.zeros(10)
# print(black)

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a.reshape(6,2)
print(b)

mar2=np.arange(1,13,1)
print(mar2)
mar2.resize(3,4)
print(mar2)
print(mar2[2][3])