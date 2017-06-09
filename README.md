# projet_python_M4105C

## Quick description
  This repository contains a project which we are doing for our software production technologies course.
  The website will allow you to display the sports installations, equipments and activities of the Pays de la Loire region,
  while making searching through them easier. We also aim to offer the possibility to display the results on a map.


## How to get the source files

  1. Go to https://github.com/yabln/projet_python_M4105C.
  2. Click on "Clone or Download".
  3. Click "Download ZIP".
  4. Unzip the downloaded file wherever you want.

## How to run the server (Linux only)

  1. Open a Bash terminal.
  2. Navigate to the directory where you unzipped the project
  3. Navigate to `projet_python_M4105C-master/main/`.
  4. Execute `chmod +x Server.py`.
  5. Execute `./Server.py`.
  6. You will then see something like this in your Bash terminal :
      
 *Bottle v0.13-dev server starting up (using WSGIRefServer())...
      Listening on http://localhost:8080/
      Hit Ctrl-C to quit.*

## How to use the service

  1. Once the server is launched, open a web browser.
  2. Go to http://localhost:8080/home.
  3. On the web site, you'll see two search fields. One for the activity, the
  other for the city. You can use one or the other or even both. Click the
  button "Rechercher" to search what you just typed into the fields. The result are
  displayed below the search button.
  4. If nothing new is displayed it means that your request returned no results.
  5. Notice that the map isn't functional yet.
