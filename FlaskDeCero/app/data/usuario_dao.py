
from app.data.modelo.usuario import usuario

class usuarioDao:

    def select_all(self,db) -> list[usuario]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Usuarios')
        Usuarios_en_db = cursor.fetchall()
        Usuarios : list[usuario]= list()
        for usuario_en_db in Usuarios_en_db:
            Usuarios.append(usuario(usuario_en_db[0], usuario_en_db[1], usuario_en_db[2]))

        cursor.close()
        
        return Usuarios

    def insert(self,db,nombre,genero):
        cursor = db.cursor()
        cursor.execute('INSERT INTO Usuarios (nombre,genero) VALUES (%s,%s)',(nombre,genero))
        db.commit()
        cursor.close()