import sys

for line in sys.stdin:

    line = line.strip()  

    datafro = line.split(',')
    if len(datafro) < 24 :
        print('AN\t-%s' % line)
    else:
        for n in range(len(datafro)):
                datafro[n] = datafro[n].strip('"')

        codcli = datafro[0]
        codecde = datafro[6]
        villecli = datafro[5]
        cpcli = datafro[4][:2]
        nbcoli = datafro[10]
        timbrecli = datafro[8]
        timbrecde = datafro[9]
        date = datafro[7].split('-')[0]
        qte = datafro[15]
        point = datafro[20]
        try:
            year = int(date)
            
        except ValueError:
            continue
        

    if 2006 <= year <= 2016:
            print('\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(codcli, codecde, villecli, cpcli, nbcoli, timbrecde, date,qte, point))
