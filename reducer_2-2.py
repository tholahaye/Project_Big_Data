import sys
import pandas as pd
import matplotlib.pyplot as plt

data = []
current_codecde = None
current_point = 0
nb_line = 0

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

    timbrecde = mapper[6]
    timbrecli = mapper[5]

    try:
        point = float(mapper[9])*float(mapper[8])
    except ValueError:
        continue

    if timbrecli in ['0','NULL']:
        continue

    if current_codecde is None:
        current_codecde = codecde

    if codecde != current_codecde:
        if nb_line > 0:
            moyenne = round(current_point / nb_line,2)
            data.append((codcli, current_codecde, villecli, cpcli, nbcoli, timbrecde, current_point, nb_line, moyenne))
        current_codecde = codecde
        current_point = 0
        nb_line = 1
    else:
        nb_line += 1

    current_point += point


if current_codecde is not None:
    data.append((codcli, current_codecde, villecli, cpcli, nbcoli, timbrecde, current_point,nb_line, moyenne))

df = pd.DataFrame(data, columns=['codcli', 'codecde', 'villecli', 'cpcli', 'nbcoli', 'timbrecde', 'point', 'commande', 'moyenne'])
cp_sample = ['53','61','28']
filtered_df = df.sort_values(by='point', ascending=False)
top100 = filtered_df.head(100)
sample5 = int(len(top100) * 0.05)

filtered_df = top100[top100['cpcli'].str.startswith(tuple(cp_sample))]
list_sample = filtered_df.sample(sample5)


list_sample.to_excel('/datavolume1/list_sample5%.xlsx', index=False)

#print(list_sample)


# Pie chart
labels = cp_sample
table = list_sample.groupby('cpcli')['point'].sum()

#print(table)

# only "explode" the 2nd slice (i.e. 'Hogs')
#explode = (0.1, 0, 0)
#add colors
colors = ['#ff9999','#66b3ff','#99ff99']
fig1, ax1 = plt.subplots()
# labels=labels,
# colors=colors,
# explode=explode,
ax1.pie(table,  autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
plt.tight_layout()
plt.legend(cp_sample)
plt.savefig("pie.pdf", format="pdf", bbox_inches="tight")

#plt.show()
'''
if table(len) == 2:
    explode = (0.1,0.1)
elif table(len) == 3:
    explode = (0.1,0.1,0.1)
else:
    explode = (0.1)
'''