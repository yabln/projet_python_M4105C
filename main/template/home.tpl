<html>
<head>
  <title>Installations Sportives en Pays de la Loire</title>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="css/reset.css" type="text/css">
  <link rel="stylesheet" href="css/main.css" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Shadows+Into+Light' rel='stylesheet' type='text/css'>
  <link rel= "stylesheet" type= "text/css" href= "css/home.css"/>
  <link rel="stylesheet" href="css/searchBar.css" type="text/css">
  <link rel="stylesheet" href="css/installations.css">
</head>
<body>
  <header>
    <h1>Installations Sportives</h1>
    <ul class="nav">
      <li class="header-menu selected"><a href="home" class="menu">Accueil</a></li>
      <li class="header-menu"><a href="home" class="menu">Carte</a></li>
    </ul>
    </header>

    <div class="all">
      <form action="/home" method="post">
      <div class="container-1">
        <input type="search" id="searchActivity" name="searchActivity" placeholder="Recherche Activité" />
        <input type="search" id="searchCity" name="searchCity" placeholder="Recherche Ville" />
      </div>
      <div class="container-2">
        <button type="submit" id="bsearch">Rechercher</button>
      </div>
      </form>
      <div class="installations">
        %if is_search_asked == "true" :
          %for installation in installations :
        <div class="installation">
          <div class="nameInstallation">
            <h3># {{installation.id}} - {{installation.name}}</h3></div>
          <div class="installationBody">
            <p><span></span><span>{{installation.address}} {{installation.postal_code}} {{installation.city}}</span></p>
            <p><span></span><span> lat : {{installation.latitude}} ; lon : {{installation.longitude}}</span></p>
            <hr>
            <b>Equipements</b></p>
            <table class="equipement">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Nom</th>
                  <th>Activités</th>
                </tr>
                </thead>
                <tb>
                  %for equipment in installation.equipments :
                  <tr>
                    <td>{{equipment.id}}</td>
                    <td>{{equipment.name}}</td>
                    <td>
                      %for activity in equipment.activities :
                        <p>{{activity.name}}
                          %if len(equipment.activities) != 1 :
                          ;
                          %end
                        </p>
                      %end
                    </td>
                  </tr>
                  %end
                  </tbody>
            </table>
          </div>
        </div>
        %end
        %end
      </div>
    </div>
  <footer>
    <ul class="footer-content">
      <li class="footer-category">
        <h3 class="footer-title">À propos</h3>
        <p class="footer-description">Bienvenue sur le site Installations Sportives en Pays de la Loire, l'annuaire de référence pour les activités et les équipements sportifs dans la région. </p>
      </li>
      <li class="footer-category">
        <h3 class="footer-title">Nous contacter</h3>
        <ul class="footer-contact">
          <li>
            <a class="email-button" href="mailto:livinnantes@gmail.com?subject=[CONTACT]" target="_blank">
              <img src="img/email_logo.png" alt="Send Email" />Contact E-mail
            </a>
          </li>
        </ul>
      </li>
    </ul>
  </footer>
</body>
</html>
