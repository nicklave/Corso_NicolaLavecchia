import mysql

def update_students(tuple_list):
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "student_db"
        )
    mycursor = mydb.cursor()
    sql = """UPDATE studenti 
             SET nome = %s, cognome = %s, matematica = %s, fisica = %s, chimica = %s
             WHERE id_studente = %s"""
    #sql = """update students set(name,surname,maths,physics,chemistry) values (%s,%s,%s,%s,%s)"""
    mycursor.execute(sql,tuple_list)
    mydb.commit()
