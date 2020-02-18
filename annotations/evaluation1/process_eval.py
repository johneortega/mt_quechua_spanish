file_sys1="evaluation1_2.txt"
file_rand="rand.txt"


final_tuple = []
with open(file_rand) as fr, open(file_sys1) as f1: 
    for x, y in zip(fr,f1):
        inner_tuple = []
        x = x.strip()
        x_arr = x.split(",")
        y = y.strip()
        ## y is the subscript 1,2,or 3
        y = int(y) - 1
        newx = x_arr[y]
        print(newx)


