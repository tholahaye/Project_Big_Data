import sys
# print(sys.maxunicode > 0xffff)

for line in sys.stdin:

    line = line.strip()
    list_data = line.split(',')
    if len(list_data) != 25:
        #TODO Gérer l'anomalie
        continue
    else:
        for n in range(len(list_data)):
            list_data[n] = list_data[n].strip('"')

        depcli = list_data[4][:2]

        datcde = list_data[7]

        datcde = datcde.split('-', 2)

        year = datcde[0]
        try:
            year = int(year)
        except ValueError:
            continue
        if year >= 2008:

            try:
                points = int(list_data[20])
            except ValueError:
                continue

            try:
                nbcolis = int(list_data[10])
            except ValueError:
                continue

            try:
                qte = int(list_data[15])
            except ValueError:
                continue

            client = list_data[1] + " " +list_data[2] + " " + list_data[3]
            villecli = list_data[5].replace("SAINT ", "ST ")
            codcde = list_data[6]

            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(depcli, villecli, client, points, qte, codcde, nbcolis))
