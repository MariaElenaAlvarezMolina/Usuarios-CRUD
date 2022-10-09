from flask import Flask, render_template, request, redirect

from users import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template('index.html', usuarios=users)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    formulario = {"id": id}
    User.borrar(formulario)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    formulario = {"id": id}
    user = User.mostrar(formulario)
    return render_template('edit.html', usuario=user)

@app.route('/update', methods=['POST'])
def update():
    User.actualizar(request.form)
    return redirect('/')

@app.route('/users/<int:id>')
def show(id):
    formulario = {"id": id}
    user = User.mostrar(formulario)
    return render_template('show.html', usuario=user)



if __name__=="__main__":
    app.run(debug=True)