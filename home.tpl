<html>
<head>
  <title>80 Vignobles - Acceuil</title>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="cssHome/reset.css" type="text/css">
  <link rel="stylesheet" href="cssHome/main.css" type="text/css">
  <link href='https://fonts.googleapis.com/css?family=Shadows+Into+Light' rel='stylesheet' type='text/css'>
  <link rel= "stylesheet" type= "text/css" href= "cssHome/home.css"/>
  <link rel="stylesheet" href="cssHome/searchBar.css" type="text/css">
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
  <script type="text/javascript" src="js/home.js"></script>
</head>
<body>
  <header>
    <h1>80 Vignobles</h1>
    <ul class="nav">
      <li class="header-menu selected"><a href="details.html" class="menu">Acceuil</a></li><!--
        ---><li class="header-menu"><a href="details.html" class="menu">Selection</a></li><!--
        ---><li class="header-menu"><a href="details.html" class="menu">Carte</a></li><!--
        ---><li class="header-menu"><a href="details.html" class="menu">Contact</a></li>
      </ul>
    </header>

    <div class="all">
      <form action="/home" method="post">
      <div class="container-1">
        <input type="search" id="search" name="search" placeholder="Recherche..." />
      </div>
      <div class="container-2">
        <button type="submit" id="bsearch">Rechercher</button>
      </div>
      </form>
    </div>

  <footer>
    <ul class="footer-content">
      <li class="footer-category">
        <h3 class="footer-title">A propos</h3>
        <p class="footer-description">Bienvenue sur 80 Vignobles, la référence en matière de tourisme viticole. Nous vous proposons de découvrir les meilleurs vignobles, les caves les plus prestigieuses, et tant d'autres.</p>
      </li><!--
        ---><li class="footer-category">
        <h3 class="footer-title">Nous contacter</h3>
        <ul class="footer-contact">
          <li><a class="email-button" href="mailto:livinnantes@gmail.com?subject=[CONTACT]" target="_blank"><img src="img/email_logo.png" alt="Send Email" />E-mail à 80 Vignobles</a></li>
        </ul>
      </li>
    </ul>
  </footer>
</body>

</html>
