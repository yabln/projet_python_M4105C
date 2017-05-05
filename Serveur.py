from bottle import get, post, route, template, request, run, static_file


@route("/cssHome/<filename>")
def style(filename):
    return static_file(filename, root='cssHome/')


@get('/home')
def login():
    return template('home', search='54615')


@post('/home')
def do_login():
    return template('home', search='ok')


run(host='localhost', port=8080)