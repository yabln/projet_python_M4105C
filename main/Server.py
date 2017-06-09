#!/usr/bin/python3
# -*- coding: utf-8 -*-

from CsvReader import *
from DatabaseAdmin import *
from lib.bottle import get, post, route, template, request, run, static_file

# initialising database
reader = CsvReader()
reader.parse_csv_files()
admin = DatabaseAdmin("resources/data.db")
admin.create_tables()
admin.insert_from_csv_reader(reader)


# configuring server
@route('/css/<filename>')
def style(filename):
    return static_file(filename, root='css/')


@route('/img/<filename>')
def picture(filename):
    return static_file(filename, root='img/')


@get('/home')
def home():
    """
    Main point of entry of the server
    :return: the home page
    """
    return template('template/home', is_search_asked="false")


@post('/home')
def do_home():
    """
    Point of entry used only when one the form fields is not empty
    :return: the home page with the results of the request added
    """
    search_request_activity = request.forms.get('searchActivity')
    search_request_city = request.forms.get('searchCity')

    installations_test = admin.get_search_result([search_request_activity, search_request_city])

    return template('template/home', installations=installations_test, is_search_asked="true")


run(host='localhost', port=8080)
