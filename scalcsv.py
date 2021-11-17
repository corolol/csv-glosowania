import os

result = open("result.csv", "w", encoding="utf-8")

lista = os.listdir("csv")

resultArray = [['',''],['','']]

for file in range(len(lista)):
    f = open("csv/" + lista[file] + "", "r", encoding="utf-8")
    lines = f.readlines()
    for x in range(len(lines)):
        lines[x] = lines[x].split(",")

    if file == 0:
        for x in range(2, len(lines)):
            row_array = []
            for y in range(len(lines[x])):
                if (x == 2 and y > 1):
                    resultArray[1].append(lines[1][2])
                    id_glosowania = lines[0][y]
                    if (id_glosowania.find("\n") != -1):
                        id_glosowania = id_glosowania.replace("\n", "")
                    resultArray[0].append(lines[1][2] + "." + id_glosowania)
                elem = lines[x][y]
                if (elem.find("\n") != -1):
                    elem = elem.replace("\n", "")
                if elem == "":
                    elem = '0'
                row_array.append(elem)
            resultArray.append(row_array)
    else:
        for x in range(2, len(lines)):
            # row_array = []
            for y in range(2, len(lines[x])):
                if (x == 2 and y > 1):
                    resultArray[1].append(lines[1][2])
                    id_glosowania = lines[0][y]
                    if (id_glosowania.find("\n") != -1):
                       id_glosowania = id_glosowania.replace("\n", "")
                    resultArray[0].append(lines[1][2] + "." + id_glosowania)
                elem = lines[x][y]
                if (elem.find("\n") != -1):
                    elem = elem.replace("\n", "")
                if elem == "":
                    elem = '0'
                resultArray[x].append(elem)
            # resultArray.append(row_array)
    
for x in resultArray:
    for y in x:
        result.write(y + ",")
    result.write("\n")