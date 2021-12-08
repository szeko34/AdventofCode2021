# Tu napíšte svoj kód :-)
subor = open("8.txt", "r")
znaky = [x.split("|")[-1] for x in subor]
dlzky = {}
for x in znaky:
    for a in x.strip().split():
        if len(a) in dlzky:
            dlzky[len(a)] += 1
        else:
            dlzky[len(a)] = 1

print(dlzky)

print(dlzky[2]+dlzky[7]+dlzky[3]+dlzky[4])
