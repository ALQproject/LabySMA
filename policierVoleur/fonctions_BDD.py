# fonction pour se connecter à la base de données
def connectionBDD(host_name, user_name, user_password, db_name):
    cnx = None
    try:
        cnx = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
    except Error as e:
        print("La connextion a MySQL a echoue")

    return cnx

# fonction pour éxecuter une requete SQL
def execution_requete(cnx, requete):
    cursor = cnx.cursor()
    try:
        cursor.execute(requete)
        cnx.commit()
        print("L'execution de la requete a reussi")
    except Error as e:
        print("L'execution de la requete a echoue")