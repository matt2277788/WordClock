import re
import numpy as np 

word = "hiuedhiwdjbibuchkjwebuchjwkerjfbwkejbwljekbcfkjbuchnioeunbuchijubcnio2unboi2ufh2iofuhiubucho3iun2o3iubuchi3rhfdp23uh"
pinVector = []
startOfDoubleItems = ([m.start() for m in re.finditer("buch", word)])
for j in startOfDoubleItems:
    for i in range (j, j+4):
        pinVector.append(i)

print(pinVector)


zeroMatrix = np.zeros(195, int)
zeroMatrix[pinVector] = 1
b = np.reshape(zeroMatrix, (15,13))


for i in range(15):
    if (i % 2 != 0):
        b[i] = b[i][::-1]
#print(b)
b = b.ravel()


testVector = []
for m in range (len(b)):
    if (b[m] != 0):
        #print(m)
        testVector.append(m)
print(testVector)


# for i in pinVector:
#     zeroMatrix(i) = 1
# print(zeroMatrix)