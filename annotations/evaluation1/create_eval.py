file_qu="kallpa.qu.lowercase"
file_sys1="sys1/translation.txt"
file_sys2="sys2/translation.txt"
file_sys3="sys3/translation.txt"
file_rand="rand.txt"


final_tuple = []
with open(file_rand) as fr, open(file_qu) as fq, open(file_sys1) as f1, open(file_sys2) as f2, open(file_sys3) as f3: 
    for v, w, x, y, z in zip(fr,fq,f1,f2,f3):
        inner_tuple = []
        v = v.strip()#rand
        w = w.strip()#quechua
        v = v.split(",")
        x = x.strip()
        y = y.strip()
        z = z.strip()
        inner_tuple.append(w)
        if v[0]=='1':
            inner_tuple.append(x)
        elif v[0]=='2':
            inner_tuple.append(y)
        elif v[0]=='3':
            inner_tuple.append(z)
        if v[1]=='1':
            inner_tuple.append(x)
        elif v[1]=='2':
            inner_tuple.append(y)
        elif v[1]=='3':
            inner_tuple.append(z)
        if v[2]=='1':
            inner_tuple.append(x)
        elif v[2]=='2':
            inner_tuple.append(y)
        elif v[2]=='3':
            inner_tuple.append(z)
        final_tuple.append(inner_tuple)

cntr=1
for sents in final_tuple:
    qsent=sents[0]
    rand1=sents[1]
    rand2=sents[2]
    rand3=sents[3]
    print("|------------- Frase Quechua " + str(cntr) + "--------------------------------|")
    print(qsent)
    print("|------------------------------------------------------------|")
    print("|------------- Frase Esp 1 ----------------------------------|")
    print(rand1)
    print("|------------------------------------------------------------|")
    print("|------------- Frase Esp 2 ----------------------------------|")
    print(rand2)
    print("|------------------------------------------------------------|")
    print("|------------- Frase Esp 3 ----------------------------------|")
    print(rand3)
    print("|------------------------------------------------------------|")
    print("\n\n\n\n")
    cntr=cntr+1


