from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#importar routes del API


#Rutas


#Ubicacion rutas



#ubicacion del api


#Ubicacion rutas



@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/Templates/Home.html', titles=titulo)

@app.route("/Dainer")
def otr():
    return "Dainer"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


