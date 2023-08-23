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

        if (cpcli.startswith('49') or cpcli.startswith('53') or cpcli.startswith('72')):

            datcde = list_data[7]

            datcde = datcde.split('-', 2)

            year = datcde[0]
            try:
                year = int(year)
            except ValueError:
                continue
            if year >= 2008:

                try:
                    qte = int(list_data[15])
                except ValueError:
                    continue

                if cpcli.startswith('49'):
                    depcli = "Maine-et-Loire (49)"
                elif cpcli.startswith('53'):
                    depcli = "Mayenne (53)"
                else:
                    depcli = "Sarthe (72)"
                codcde = list_data[6]
                codobj = list_data[14]
                feature = list_data[18]
                if feature == "NULL":
                    libobj = list_data[17]
                else:
                    libobj = list_data[17] + " (" + feature + ")"

                print('{}\t{}\t{}\t{}\t{}\t{}'.format(codobj, depcli, year, codcde, libobj, qte))
