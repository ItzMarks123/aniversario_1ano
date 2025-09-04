from flask import Flask, render_template
from art import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    eu_te_amo = [
    "I love you (Inglês)",
    "Te amo (Espanhol)",
    "Je t'aime (Francês)",
    "Ich liebe dich (Alemão)",
    "Ti amo (Italiano)",
    "Aishiteru (Japonês)",
    "Saranghae (Coreano)",
    "Eu te amo (Português)",
    "Ya tebya lyublyu (Russo)",
    "Wo ai ni (Chinês)",
    "Jag älskar dig (Sueco)",
    "Seni seviyorum (Turco)"
]
    mensagem = "🌍 Como dizer 'Eu te amo' ao redor do mundo:\n\n"
    for frase in eu_te_amo:
        mensagem += f"{frase}\n"
    mensagem += "\n"
    mensagem += "Amorrr, hoje é mais 1 ano, muito obrigado ❤️\n"
    mensagem += "Te amo hoje e sempre! - MAYCON\n\n"
    banner = text2art("MAYCON & LARISSA", font="block")
    return mensagem + banner

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
