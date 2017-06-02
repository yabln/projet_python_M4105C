from bottle import get, post, route, template, request, run, static_file
from DatabaseModel import *

installationsTest = []
installationsTest.append(Installation(50, "test equipement 1", "10 rue rabelais", 44000, "nantes", 150, 150))
installationsTest.append(Installation(51, "test equipement 2", "10 rue rabelais", 44000, "nantes", 150, 150))
installationsTest[0].add_equipements(Equipement(1, "terrain de foot", installationsTest[0]))
installationsTest[0].add_equipements(Equipement(2, "terrain de foot2", installationsTest[0]))
installationsTest[1].add_equipements(Equipement(3, "terrain de foot3", installationsTest[1]))
installationsTest[1].add_equipements(Equipement(4, "terrain de foot4", installationsTest[1]))

                                



@route("/cssHome/<filename>")
def style(filename):
    return static_file(filename, root='cssHome/')


@get('/home')
def home():
    return template('home', isSearchAsked="false")


@post('/home')
def do_home():
    searchRequest = request.forms.get('search')
    
    return template('home', installations=installationsTest, isSearchAsked="true")


run(host='localhost', port=8080)