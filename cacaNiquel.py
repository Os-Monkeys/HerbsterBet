import random
from flask import Flask, render_template, request, flash, url_for, session, redirect

# Permissões básicas
array = dict(zip(['jusbiscreudo', 'Enxi', 'JesseChad'], [1, 2, 3]))

app = Flask(__name__)
app.secret_key = "qualquer_coisa"

def rodarRoleta():
    return random.randint(1, 10)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        if user in array:
            session['user_perm'] = user
            session['money'] = 500
            return redirect(url_for('index'))
        else:
            flash("Usuário inválido!")
    return render_template('login.html')

@app.route('/')
def index():
    if 'user_perm' not in session:
        return redirect(url_for('login'))
    
    return render_template('index.html', money=session['money'], resultado=None)

@app.route('/Gerar', methods=['POST'])
def gerar():
    if request.method == 'POST':
        dinheiro = request.form['Dinheiro']

        if dinheiro == "" or "-" in dinheiro:
            flash("Valor inválido ou negativo!")
            return render_template('index.html', money=session['money'], resultado=None)

        extra = float(dinheiro)

        if extra < 0 or extra >= 1000:
            flash("Valor inválido ou muito alto!")
            return render_template('index.html', money=session['money'], resultado=None)

        session['money'] = session.get('money', 0) + extra
        flash(f"Você gerou R$ {extra}!")
        return render_template('index.html', money=session['money'], resultado=None)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/clique", methods=['POST'])
def girar():
    simboloUm = rodarRoleta()
    simboloDois = rodarRoleta()
    simboloTres = rodarRoleta()

    flash(f'[{simboloUm}][{simboloDois}][{simboloTres}]')

    money = session.get('money', 500.0)
    money -= 25.0

    # Verificação de vitória
    if simboloUm == simboloDois == simboloTres:
        adicional = 500.50
        resultado = "jackpot"
    elif simboloUm == simboloDois or simboloTres == simboloUm or simboloDois == simboloTres:
        adicional = 30.0
        resultado = "win"
    else:
        adicional = 0.0
        resultado = "lose"

    money += adicional
    session['money'] = money

    flash(f"Você recebeu R${adicional:.2f}!")

    # Caso fique muito negativo → expulsar
    if money <= -100:
        flash("Você perdeu tudo! Expulso!")
        session.clear()
        return redirect(url_for('login'))

    return render_template("index.html", money=money, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
