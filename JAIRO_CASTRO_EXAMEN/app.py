from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
        return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre, total_sin_descuento, total_con_descuento = None, None, None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        cantidad = int(request.form.get('cantidad'))
        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

    return render_template(
        'ej1.html',
        nombre=nombre,
        total_sin_descuento=total_sin_descuento,
        total_con_descuento=total_con_descuento
    )


# Usuarios predefinidos
usuario = {
    "juan": "admin",
    "pepe": "user"
}


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        # Validación del usuario
        if nombre in usuario and usuario[nombre] == contrasena:
            if nombre == "juan":
                mensaje = f"Bienvenido Administrador {nombre}"
            elif nombre == "pepe":
                mensaje = f"Bienvenido Usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ej2.html', mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)