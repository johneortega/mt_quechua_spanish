import random
x = [1,2,3]
for i in range(0,100):
    smpl=random.sample(x, k=len(x))
    print(str(smpl[0]) + "," + str(smpl[1]) + "," + str(smpl[2]))
