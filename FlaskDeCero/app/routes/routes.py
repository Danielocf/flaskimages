from flask import Blueprint, render_template, request, redirect

from app import db
from app.data.usuario_dao import usuarioDao
from app.data.medidas_dao import medidasDao

rutas_usuarios = Blueprint("routes", __name__)


@rutas_usuarios.route('/')
def index():
    return render_template('index.html')

@rutas_usuarios.route('/formulario', methods=['GET' , 'POST'])
def formusu():
    usuario_dao = usuarioDao()
   
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        usuario_dao.insert(db,nombre,genero)
        return redirect('/test')
    return render_template('formulario.html')




@rutas_usuarios.route('/test', methods=['GET'])
def pepe():
    usuario_dao = usuarioDao()

    Usuarios = usuario_dao.select_all(db)

    return render_template('test.html',Usuarios=Usuarios)




rutas_medidas = Blueprint("med", __name__)


@rutas_medidas.route('/formedidas', methods=['GET', 'POST'])
def formmed():
    medidas_dao = medidasDao()
    if request.method == 'POST':
        id = request.form['id']
        peso_en_kg = request.form['peso_en_kg']
        altura_en_cm = request.form['altura_en_cm']
        edad = request.form['edad']
        nombre = request.form['nombre']
        medidas_dao.insert(db,id,peso_en_kg,altura_en_cm,edad,nombre)
        return redirect('/medidas')
    return render_template('formedidas.html')


@rutas_medidas.route('/medidas', methods=['GET'])
def medidas():
    medidas_dao = medidasDao()
    medidas = medidas_dao.select_all(db)
    return render_template('medidas.html',medidas=medidas)


    





