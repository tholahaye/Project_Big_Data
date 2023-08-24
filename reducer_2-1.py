import sys
import pandas as pd

#print('codcli\tcodecde\tvillecli\tcpcli\tnbcoli\ttimbrecde\tpoint')

data =[]
current_codecde = None
current_point = 0

for line in sys.stdin:
    line = line.strip()
    mapper = line.split('\t')

    codcli = mapper[0]
    codecde = mapper[1]
    villecli = mapper[2]
    cpcli = mapper[3]

    try:
        nbcoli = float(mapper[4])
    except ValueError:
        continue

    timbrecde = mapper[5]
    date = mapper[6]

    try:
        point = float(mapper[8])*float(mapper[7])
    except ValueError:
        continue

    if current_codecde is None:
        current_codecde = codecde

    if codecde != current_codecde:
        data.append((codcli, current_codecde, villecli, cpcli, nbcoli, timbrecde, current_point))
        current_codecde = codecde
        current_point = 0

    current_point += point

if current_codecde is not None:
    data.append((codcli, current_codecde, villecli, cpcli, nbcoli, timbrecde, current_point))

df = pd.DataFrame(data, columns=['codcli', 'codecde', 'villecli', 'cpcli', 'nbcoli', 'timbrecde', 'point'])

filtered_df = df.sort_values(by='point', ascending=False)
top100 = filtered_df.head(100)

top100.to_excel('/datavolume1/top100.xlsx', index=False)