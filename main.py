from flask import Flask, request, make_response, redirect, render_template,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap = Bootstrap(app) #Initiate bootstrap (clase 15 del curso)
#clase 15, ordenar logo y navbar

app.config['SECRET_KEY'] = 'SUPER SECRETO'




#When a route is not found we modify the default 404 error
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session ['user_ip']= user_ip
    #response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    return render_template('hello.html', user_ip=user_ip)

@app.route('/registro-clientes')
def add():
    return render_template('add-client.html')

@app.route('/test')
def test():
    return render_template('bstemplate.html')
    
if __name__ == '__main__':
   app.run()