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
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/')
def index():
    #if user not in session:
    #    return redirect(url_for('login.html'))
    if 'money' not in session:
        session['money'] = 500.00
    return render_template('index.html', money=session['money'])

@app.route("/clique", methods=['POST'])
def girar():
    simboloUm = rodarRoleta()
    simboloDois = rodarRoleta()
    simboloTres = rodarRoleta()

    print(f'[{simboloUm}][{simboloDois}][{simboloTres}]')

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

    flash(f"Você recebeu R${adicional:.2f}!!!")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
