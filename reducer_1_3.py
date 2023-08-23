import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

current_dep = None
current_year = None
current_obj = None
current_libobj = None
current_cde = None
current_nbcde = 1
current_qte = 0
depcli = None
codcde = None
codobj = None

#initiation du dataframe
data = pd.DataFrame(columns = ['objet', 'departement', 'annee', 'nombre_commandes', 'quantite'])

for line in sys.stdin:
    # Enlève les espaces au début et à la fin de la ligne
    line = line.strip()
    mapper = line.split('\t')
    if len(mapper) != 6:
        # Gérer anomalie ?
        continue
    else:
        codobj = mapper[0]
        depcli = mapper[1]
        year = mapper[2]
        codcde = mapper[3]
        libobj = mapper[4]
        try:
            qte = int(mapper[5])
        except ValueError:
            continue
        # On vérifie que le departement est le même que sur la ligne précédente
        if current_dep and current_dep == depcli and current_year == year and current_obj == codobj:
            # On vérifie que la commande est la même qu'à la ligne précédente pour sommer la quantité
            if current_cde == codcde:
                current_qte = qte
            else:
                current_nbcde += 1
                current_cde = codcde
                current_qte += qte
        else:
            # On vérifie que current_dep est bien définie pour afficher le résultat
            if current_dep:
                # ajout de la ligne au dataframe
                row = {'objet':current_libobj, 'departement':current_dep, 'annee':current_year,
                       'nombre_commandes':current_nbcde, 'quantite':current_qte}
                data = pd.concat([data, pd.DataFrame([row])], ignore_index=True)
                print("{}\t{}\t{}\t{}\t{}".format(current_libobj, current_dep, current_year,
                                                  current_nbcde, current_qte))
            # Mise à jour des variables du décompte en cours
            current_dep = depcli
            current_year = year
            current_obj = codobj
            current_libobj = libobj
            current_cde = codcde
            current_qte = qte
            current_nbcde = 1
# Affichage du résultat du dernier objet
if current_dep and current_obj and current_cde and \
   current_dep == depcli and current_obj == codobj and current_cde == codcde:
    # ajout de la ligne au dataframe
    row = {'objet': current_libobj, 'departement': current_dep, 'annee': current_year,
           'nombre_commandes': current_nbcde, 'quantite': current_qte}
    data = pd.concat([data, pd.DataFrame([row])], ignore_index=True)
    print("{}\t{}\t{}\t{}\t{}".format(current_libobj, current_dep, current_year,
                                      current_nbcde, current_qte))


#### Graphiques de croissance ####
data = data.convert_dtypes()
data["annee"] = pd.to_numeric(data["annee"])
min_annee = data["annee"].min()
max_annee = data["annee"].max()
x = range(min_annee, max_annee+1)

#### quantités commandées ####
obj_set = list(set(data["objet"]))
for obj in obj_set[0:2]:
    data_obj = data[data["objet"] == obj]
    dep_set = list(set(data_obj["departement"]))
    for dep in dep_set:
        data_obj_dep = data_obj[data_obj["departement"] == dep]
        x_tmp = list(data_obj_dep["annee"])
        y_tmp = list(data_obj_dep["quantite"])
        y = np.zeros(len(x))
        for year in x:
            ind = x.index(year)
            if year in x_tmp:
                ind_tmp = x_tmp.index(year)
                y[ind] = y_tmp[ind_tmp]
        plt.plot(x, y, label=dep, marker='o')
        plt.title(obj)
        plt.ylabel("Quantité commandée")
        plt.xlabel("Année")
    plt.legend()
    plt.show()


#### nombres de commandes ####
obj_set = list(set(data["objet"]))
for obj in obj_set[0:2]:
    data_obj = data[data["objet"] == obj]
    dep_set = list(set(data_obj["departement"]))
    for dep in dep_set:
        data_obj_dep = data_obj[data_obj["departement"] == dep]
        x_tmp = list(data_obj_dep["annee"])
        y_tmp = list(data_obj_dep["nombre_commandes"])
        y = np.zeros(len(x))
        for year in x:
            ind = x.index(year)
            if year in x_tmp:
                ind_tmp = x_tmp.index(year)
                y[ind] = y_tmp[ind_tmp]
        plt.plot(x, y, label=dep, marker='o')
        plt.title(obj)
        plt.ylabel("Nombre de commandes")
        plt.xlabel("Année")
    plt.legend()
    plt.show()


