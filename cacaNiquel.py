import random
from flask import Flask, render_template, request, flash, url_for, session, redirect

array = dict(zip(['jusbiscreudo','Enxi','JesseChad'],[1,2,3]))

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
    return render_template('login.html')

@app.route('/')
def index():
    if 'user_perm' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', money=session['money'])

@app.route('/Gerar', methods=['GET','POST'])
def gerar():
    if request.method == 'POST':
        if request.form['Dinheiro'] == "":
            flash("Valor Invalido")
            return render_template('index.html', money=session['money'])
        elif "-" in request.form['Dinheiro']:
            flash("Valor Invalido")
            return render_template('index.html', money=session['money'])
        extra = float(request.form['Dinheiro'])
        session['money'] = session.get('money', 0) + extra
        flash(f"Você Gerou {extra} !")
    return render_template('index.html', money=session['money'])


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

    money = session.get('money', 500.00)
    money -= 25.00

    if simboloUm == simboloDois == simboloTres:  # Jackpot
        adicional = 500.50
    elif simboloUm == simboloDois or simboloTres == simboloUm or simboloDois == simboloTres:
        adicional = 30.00
    else:
        adicional = 0.00

    money += adicional
    session['money'] = money

    flash(f"Você recebeu R${adicional:.2f}!!")
    if money < 0:
        flash(f"Você Esta {money} No Negativo Cuidado Se Cheagar A -100 Você É Expulso(a) !! ")
    if money <= -100:
        session.clear()
        return redirect(url_for('login'))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
