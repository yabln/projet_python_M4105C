#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bottle import get, post, route, template, request, run, static_file
from DatabaseAdmin import *
from CsvReader import *

reader = CsvReader()
reader.parse_Csv_files()

admin = DatabaseAdmin("datas.db")
admin.create_tables()
admin.insert_from_csv_reader(reader)


@route("/cssHome/<filename>")
def style(filename):
    return static_file(filename, root='cssHome/')


@get('/home')
def home():
    return template('home', isSearchAsked="false")


@post('/home')
def do_home():
    searchrequestactivity = request.forms.get('searchActivity')
    searchrequestcity = request.forms.get('searchCity')

    installationstest = admin.get_search_result([searchrequestactivity, searchrequestcity])

    return template('home', installations=installationstest, isSearchAsked="true")


run(host='localhost', port=8080)
