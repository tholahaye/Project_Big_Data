import sys
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
        print("{}\t{}\t{}\t{}\t{}".format(current_libobj, current_dep, current_year,
                                          current_nbcde, current_qte))
