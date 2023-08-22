import sys
current_cp = None
current_city = None
current_year = None
current_obj = None
current_libobj = None
current_cde = None
current_feature = None
current_details = ""
current_sum = 0
current_qte = 0
villecli = None
codcde = None
codobj = None

for line in sys.stdin:
    # Enlève les espaces au début et à la fin de la ligne
    line = line.strip()
    mapper = line.split('\t')
    if len(mapper) != 8:
        # Gérer anomalie ?
        continue
    else:
        cpcli = mapper[0]
        villecli = mapper[1]
        year = mapper[2]
        codobj = mapper[3]
        codcde = mapper[4]
        libobj = mapper[5]
        feature = mapper[6]
        try:
            qte = int(mapper[7])
        except ValueError:
            continue
        # On vérifie que la ville est la même que la ligne précédente
        if current_city and current_city == villecli and current_year == year and current_obj == codobj:
            # On vérifie que la commande est la même qu'à la ligne précédente pour sommer la quantité
            if current_cde == codcde:
                current_qte += qte
            else:
                if current_qte > 5:
                    current_sum += 1
                    current_details += "{},{}-{}({}),{};"\
                        .format(current_cde, current_obj, current_libobj, current_feature, current_qte)

                current_cde = codcde
                current_feature = feature
                current_qte = qte
        else:
            # On vérifie que current_city est bien définie pour afficher le résultat
            if current_city:
                if current_qte > 5:
                    current_sum += 1
                    current_details += "{},{}-{}({}),{};" \
                        .format(current_cde, current_obj, current_libobj, current_feature, current_qte)
                if current_sum > 0:
                    print("{}\t{}\t{}\t{}\t{}".format(current_city, current_cp, current_year,
                                                      current_sum, current_details))
            # Mise à jour des variables du décompte en cours
            current_cp = cpcli
            current_city = villecli
            current_year = year
            current_obj = codobj
            current_libobj = libobj
            current_cde = codcde
            current_feature = feature
            current_details = ""
            current_qte = qte
            current_sum = 0
# Affichage du résultat de la dernière ville
if current_city and current_obj and current_cde and \
   current_city == villecli and current_obj == codobj and current_cde == codcde:
    if current_qte > 5:
        current_sum += 1
    if current_sum > 0:
        print("{}\t{}\t{}\t{}\t{}".format(current_city, current_cp, current_year,
                                          current_sum, current_details))
