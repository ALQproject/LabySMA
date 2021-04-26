import mysql.connector
from mysql.connector import Error
##
# * ********************************************************************************************************************
# * * * connectionBDD : fonction qui permet d'établir la connexion avec la base de donnée MySQL
# * * * Input   : strings déterminant les paramètre de configuration de la connexion
# * * * Output  : vide
# * 
# *********************************************************************************************************************
# **/
def connectionBDD(host_name, user_name, user_password, db_name):
    cnx = None
    cnx = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
    )

    return cnx

##
# * ********************************************************************************************************************
# * * * execution_requete : fonction qui permet d'exécuter une requête SQL
# * * * Input   : string déterminant les champs de la requête
# * * * Output  : vide
# * 
# *********************************************************************************************************************
# **/
def execution_requete(cnx, requete):
    cursor = cnx.cursor()
    cursor.execute(requete)
    cnx.commit()