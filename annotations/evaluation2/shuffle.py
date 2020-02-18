import random
x = [1,2,3,4,5]
for i in range(0,100):
    smpl=random.sample(x, k=len(x))
    print(str(smpl[0]) + "," + str(smpl[1]) + "," + str(smpl[2]) + "," + str(smpl[3]) + "," + str(smpl[4]))
