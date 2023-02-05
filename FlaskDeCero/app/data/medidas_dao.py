from app.data.modelo.medidas import Medidas


class medidasDao:
    
    def select_all(self,db) -> list[Medidas]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM medidas')
        medidas_en_db = cursor.fetchall()
        medida : list[Medidas]= list()
        for medida_en_db in medidas_en_db:
            medida.append(Medidas(medida_en_db[0], medida_en_db[1], medida_en_db[2], medida_en_db[3], medida_en_db[4], medida_en_db[5]))
        cursor.close()
        return medida

    def insert(self,db,id,peso_en_kg,altura_en_cm,edad,nombre):
        cursor = db.cursor()
        cursor.execute('INSERT INTO medidas (id,peso_en_kg,altura_en_cm,edad,nombre) VALUES (%s,%s,%s,%s,%s)',(id,peso_en_kg,altura_en_cm,edad,nombre))
        db.commit()
        cursor.close()
