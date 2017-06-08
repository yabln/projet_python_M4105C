#!/usr/bin/python3
# -*- coding: utf-8 -*-

from CsvReader import *
from DatabaseAdmin import *
from bottle import get, post, route, template, request, run, static_file

reader = CsvReader()
reader.parse_csv_files()

admin = DatabaseAdmin("datas.db")
admin.create_tables()
admin.insert_from_csv_reader(reader)


@route("/cssHome/<filename>")
def style(filename):
    return static_file(filename, root='cssHome/')


@get('/home')
def home():
    return template('home', is_search_asked="false")


@post('/home')
def do_home():
    search_request_activity = request.forms.get('searchActivity')
    search_request_city = request.forms.get('searchCity')

    installations_test = admin.get_search_result([search_request_activity, search_request_city])

    return template('home', installations=installations_test, is_search_asked="true")


run(host='localhost', port=8080)
