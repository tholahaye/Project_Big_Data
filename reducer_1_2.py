import sys
import math

current_cp = None
current_city = None
current_name = None
current_cde = None
current_feature = None
current_nbcde = 0
current_package_list = []
current_sum_points = 0
current_qte = 0
list_results = []
count_results = 0
villecli = None
codcde = None
codobj = None


for line in sys.stdin:
    # Enlève les espaces au début et à la fin de la ligne
    line = line.strip()
    mapper = line.split('\t')
    if len(mapper) != 7:
        # Gérer anomalie ?
        continue
    else:
        villecli = mapper[0]
        cpcli = mapper[1]
        name = mapper[2]
        try:
            points = int(mapper[3])
        except ValueError:
            continue
        try:
            qte = int(mapper[4])
        except ValueError:
            continue
        codcde = mapper[5]
        try:
            nbcolis = int(mapper[6])
        except ValueError:
            continue

        # On vérifie que la ville est la même que la ligne précédente
        if current_name and current_name == name:
            # On vérifie que la commande est la même qu'à la ligne précédente pour sommer la quantité
            current_sum_points += qte * points
            if current_cde != codcde:
                current_package_list.append(nbcolis)
                current_nbcde += 1

        else:
            # On vérifie que current_city est bien définie pour afficher le résultat
            if current_name:
                # Incrémentation du décompte résultat
                count_results += 1

                # Calcul de la moyenne
                sum_nbcolis = 0
                for element in current_package_list:
                    sum_nbcolis += element

                avg_nbcolis = sum_nbcolis / current_nbcde

                # Calcul de l'écart-type

                sum_nbcolis2 = 0
                for nbcolis in current_package_list:
                    sum_nbcolis2 += nbcolis ** 2
                avg_nbcolis2 = sum_nbcolis2 / current_nbcde
                standard_deviation_nbcolis = math.sqrt(avg_nbcolis2 - avg_nbcolis ** 2)

                # Création du dictionnaire du client
                dict_client = {"villecli": current_city, "cpcli": current_cp, "name": current_name,
                                "points": current_sum_points, "nbcde": current_nbcde, "avg_nbcolis": avg_nbcolis,
                                "standard_deviation_nbcolis": standard_deviation_nbcolis}
                
                # Ajout du dictionnaire client au dictionnaire de résultats
                list_results.append(dict_client)


            # Mise à jour des variables du décompte en cours
            current_cp = cpcli
            current_city = villecli
            current_name = name
            current_cde = codcde
            current_package_list = [nbcolis]
            current_nbcde = 1
            current_sum_points = qte * points

# Affichage du résultat dernier client
if current_name:
    # Incrémentation du décompte résultat
    count_results += 1
    
    sum_nbcolis = 0
    for element in current_package_list:
        sum_nbcolis += element

    avg_nbcolis = sum_nbcolis / current_nbcde

    sum_nbcolis2 = 0
    for nbcolis in current_package_list:
        sum_nbcolis2 += nbcolis ** 2
    avg_nbcolis2 = sum_nbcolis2 / current_nbcde
    standard_deviation_nbcolis = math.sqrt(avg_nbcolis2 - avg_nbcolis ** 2)

    # Création du dictionnaire du client
    dict_client = {"villecli": current_city, "cpcli": current_cp, "name": current_name,
                   "points": current_sum_points, "nbcde": current_nbcde, "avg_nbcolis": avg_nbcolis,
                   "standard_deviation_nbcolis": standard_deviation_nbcolis}

    # Ajout du dictionnaire client au dictionnaire de résultats
    list_results.append(dict_client)
    
# Tri des résultats en fonction du plus grand nombre de points
    list_results.sort(key=lambda dic: dic.get('points'), reverse=True)
    for x in range(10):
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(list_results[x]["villecli"], list_results[x]["cpcli"],
                                          list_results[x]["name"], list_results[x]["points"],
                                          list_results[x]["nbcde"], list_results[x]["avg_nbcolis"],
                                          list_results[x]["standard_deviation_nbcolis"]))
