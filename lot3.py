import sys
import happybase
import datetime
import uuid
import csv

file_name = sys.argv[1]

file = open(file_name, errors='surrogateescape', encoding='utf-8')
try:
    csvreader = csv.reader(file)
    
    connection = happybase.Connection('127.0.0.1', 9090)
    
    connection.open()

    print("Connection a HBase reussi")

    table_name = "dataw_fro03bis"

    column_family_name = "fidelity"

    try:
        # Creation de la table si elle n'existe pas deja dans HBase
        if not table_name.encode() in connection.tables():
            connection.create_table(table_name, {column_family_name: dict()})
        
        # Instanciation de la table dans python
        table = connection.table(table_name)
        # Initialisation de compteurs de lignes et lignes inserees dans HBase
        nb_row = 0
        nb_row_put = 0

        nb_error = 0
        
        list_headers = []

        for line in csvreader:
            nb_row += 1
            if len(line) != 25:
                print("Wrong index of arguments: {}".format(line))
                nb_error += 1
                continue
            else:

                dict_data = {}
                encoding_error = False
                # Generation du row_key
                unique_id = uuid.uuid4()
                timestamp = datetime.datetime.now().timestamp()
                row_key = "{}-{}".format(timestamp, unique_id)

                if nb_row == 1:
                    # Remplissage de la liste de headers
                    for index in range(len(line)):
                        list_headers.append("{}:{}".format(column_family_name, line[index]))
                    continue

                for index in range(len(line)):
                    # Elimination des guillemets autour des donnees de champs
                    line[index] = line[index].strip('"')
                    # Remplacement des "NULL" par des chaines de caracteres vides pour
                    # permettre l'insertion des donnees dans PowerBI
                    if line[index].upper() == "NULL":
                        line[index] = line[index].upper().replace("NULL", "")
                    # Encodage en utf-8 des valeurs de cellules
                    try:
                        line[index] = line[index].encode('utf-8')
                    except UnicodeEncodeError:
                        encoding_error = True
                        break
                        # Ajout de la paire clé valeur au dictionnaire de donnees
                    dict_data[list_headers[index]] = line[index]

                # Continue si il y a eu une erreur d'encodage
                if encoding_error:
                    print(40*"*")
                    print("Encoding error row number {}: {}".format(nb_row, line))
                    nb_error += 1
                    print(nb_error)
                    continue
                # Ajout dans Hbase de la ligne en cours de traitement
                table.put(row_key, dict_data)

                # Incrementation du decompte de lignes inserees
                nb_row_put += 1

# Fermeture de la connection HBase
    finally:
        connection.close()
# Fermeture du fichier .csv
finally:
    file.close()

print("{} rows inserted".format(nb_row_put))
print("{} errors".format(nb_error))
