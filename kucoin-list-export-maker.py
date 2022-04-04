file = open("kucoin.txt" , "r")
newfile = open("file.txt" , "w")
fileLists = file.readlines()
del fileLists[0]
print(fileLists)
print(fileLists[0])
for x in fileLists: 
    sep = ","
    stripped = x.split(sep , 1)[0]
    z = stripped.replace( "\n", "")
    kucoin =  "KUCOIN:" + z + ","
    kucoin[-1].replace(",","")
    newfile.write(kucoin)
    print(kucoin)