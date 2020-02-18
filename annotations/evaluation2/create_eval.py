file_qu="test.qu.lowercase"
file_sys1="sys1/translation.txt"
file_sys2="sys2/translation.txt"
file_sys3="sys3/translation.txt"
file_sys4="sys4/translation.txt"
file_sys5="sys5/translation.txt"
file_rand="rand.txt"


final_tuple = []
with open(file_rand) as fr, open(file_qu) as fq, open(file_sys1) as f1, open(file_sys2) as f2, open(file_sys3) as f3, open(file_sys4) as f4, open(file_sys5) as f5: 
    for v, w, x, y, z, a, b in zip(fr,fq,f1,f2,f3,f4,f5):
        inner_tuple = []
        v = v.strip()#rand
        v = v.split(",")
        w = w.strip()#quechua
        x = x.strip()
        y = y.strip()
        z = z.strip()
        a = a.strip()
        b = b.strip()
        inner_tuple.append(w)
        if v[0]=='1':
            inner_tuple.append(x)
        elif v[0]=='2':
            inner_tuple.append(y)
        elif v[0]=='3':
            inner_tuple.append(z)
        elif v[0]=='4':
            inner_tuple.append(a)
        elif v[0]=='5':
            inner_tuple.append(b)
        if v[1]=='1':
            inner_tuple.append(x)
        elif v[1]=='2':
            inner_tuple.append(y)
        elif v[1]=='3':
            inner_tuple.append(z)
        elif v[1]=='4':
            inner_tuple.append(a)
        elif v[1]=='5':
            inner_tuple.append(b)
        if v[2]=='1':
            inner_tuple.append(x)
        elif v[2]=='2':
            inner_tuple.append(y)
        elif v[2]=='3':
            inner_tuple.append(z)
        elif v[2]=='4':
            inner_tuple.append(a)
        elif v[2]=='5':
            inner_tuple.append(b)
        if v[3]=='1':
            inner_tuple.append(x)
        elif v[3]=='2':
            inner_tuple.append(y)
        elif v[3]=='3':
            inner_tuple.append(z)
        elif v[3]=='4':
            inner_tuple.append(a)
        elif v[3]=='5':
            inner_tuple.append(b)
        if v[4]=='1':
            inner_tuple.append(x)
        elif v[4]=='2':
            inner_tuple.append(y)
        elif v[4]=='3':
            inner_tuple.append(z)
        elif v[4]=='4':
            inner_tuple.append(a)
        elif v[4]=='5':
            inner_tuple.append(b)
        final_tuple.append(inner_tuple)

cntr=1
for sents in final_tuple:
    qsent=sents[0]
    rand1=sents[1]
    rand2=sents[2]
    rand3=sents[3]
    rand4=sents[4]
    rand5=sents[5]
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
    print("|------------- Frase Esp 4 ----------------------------------|")
    print(rand4)
    print("|------------------------------------------------------------|")
    print("|------------- Frase Esp 5 ----------------------------------|")
    print(rand5)
    print("|------------------------------------------------------------|")
    print("\n\n\n\n")
    cntr=cntr+1


