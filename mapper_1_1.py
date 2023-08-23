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

        cpcli = list_data[4]

        if cpcli.startswith('53'):

            datcde = list_data[7]

            datcde = datcde.split('-', 2)

            year = datcde[0]
            try:
                year = int(year)
            except ValueError:
                continue
            if year >= 2010:

                try:
                    qte = int(list_data[15])
                except ValueError:
                    continue

                villecli = list_data[5].replace("SAINT ", "ST ")
                codcde = list_data[6]
                codobj = list_data[14]
                libobj = list_data[17]
                size = list_data[18]

                print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(cpcli, villecli, year, codobj, codcde, libobj, size, qte))
