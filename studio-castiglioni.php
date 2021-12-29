
<html lang="en-US" class="gallerypage">
<head>
    <meta charset="utf-8">
    <title>Corrado Maria Crisciani</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Prefetching Fonts -->
    <link rel="dns-prefetch" href="//fonts.googleapis.com" />

    <!-- Styles -->

    <link rel="stylesheet" href="css/general.css">
    <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <link href="css/animate.css" rel="stylesheet">
    <link href="css/bootstrap.css" rel="stylesheet">
    <link href="css/default.css" rel="stylesheet" >
    <link href="css/style.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,300' rel='stylesheet' type='text/css'>
    <!-- Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Raleway:600' rel='stylesheet' type='text/css'>
    <script src="js/modernizr.custom.js"></script>
</head>
<body class="dark  docenza">
    <!-- Header -->
    <button id="openmenu" class="cmc-button" type="button" role="button" aria-label="Toggle Navigation">
        <div class="doubleframe">
            <span class="logo"></span>
        </div>
    </button>


    <nav class="menu menu-vertical menu-left " id="menu-s1">
        <div class="overlay_blank_mobile"></div>
        <div class="nav_wrapper transparent">
            <ul>
                <li><a href="index.html">About</a></li>
                <li><a href="portfolio.html">Portfolio</a></li>
                <li><a class="sub" href="de-carli-triennale.php">De Carli Triennale</a></li>
                <li><a class="sub" href="palladio-digitale.php">Palladio Digitale</a></li>
                <li><a class="sub active" href="studio-castiglioni.php">Studio Castiglioni</a></li>
                <li><a href="mailto:cmcrisciani@fastwebnet.it">Contatti</a></li>
            </ul>
            <footer>All images © 1995-2014</br>Corrado Maria Crisciani.</footer>
        </div>
        <div class="overlay_blank_mobile"></div>
    </nav>

    <!-- Content -->
    <div id="main" class="menu-push">
        <div class="gallery">
            <div id="page">
            <div class="row">
            	<div class="col-md-12 text-center">
            		<h2>Studio Castiglioni</h2>
            	</div>
            </div>
                <div class="portfolio-single-center-align">


                    <section class="slider">
                        <div id="slider" class="flexslider">
                            <ul class="slides">
                                <?php 
                            // Inizio script per il caricamento di file da ftp
                                $path = '/img/gallery/docenza/ricerca/studio-castiglioni';
                                $files = array();
                                if( file_exists($_SERVER['DOCUMENT_ROOT'] . $path )) {
                                    if( $handle = opendir( $_SERVER['DOCUMENT_ROOT'] . $path )) {

                                        while (false !== ($entry = readdir($handle))) {
                                            if(!($entry=='..' || $entry=='.')) {
                                                $files[] = $path . '/' . $entry;
                                            }

                                        }

                                        closedir($handle);
                                    }
                                }
                                sort($files);
                                ?>
                                <?php foreach ($files as $img): ?>
                                    <li>
                                        <img src="<?=$img ?>"/>
                                    </li>
                                <?php endforeach; 
                            // Fine script per il caricamento di file da ftp
                                ?>
                            </ul>
                        </div>

                        <div id="carousel" class="flexslider">
                            <ul class="slides">
                                <?php 
                                // Inizio script per il caricamento di file da ftp
                                $path = '/img/gallery/docenza/ricerca/studio-castiglioni';
                                $files = array();
                                if( file_exists($_SERVER['DOCUMENT_ROOT'] . $path )) {
                                    if( $handle = opendir( $_SERVER['DOCUMENT_ROOT'] . $path )) {

                                        while (false !== ($entry = readdir($handle))) {
                                            if(!($entry=='..' || $entry=='.')) {
                                                $files[] = $path . '/' . $entry;
                                            }

                                        }

                                        closedir($handle);
                                    }
                                }
                                sort($files);
                                ?>
                                <?php foreach ($files as $img): ?>
                                    <li>
                                        <div class="hover"></div>
                                        <img src="<?=$img ?>"/>
                                    </li>
                                <?php endforeach; 
                                // Fine script per il caricamento di file da ftp
                                ?>


                            </ul>
                        </div>

                        <!-- Scroll -->
                        <div class="pseudo-scroll">
                            <div class="scrollbar"></div>
                        </div>

                    </section>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    
    <!-- Scripts -->
    <script src="js/libs/jquery-1.10.2.min.js"></script>
    <script src="js/libs/jquery.flexslider.js"></script>

    <!-- Custom -->
    <script src="js/scripts.js"></script>

    <script src="js/classie.js"></script>

    <!-- BUTTON ANIMATION & PUSH MENU  -->

    <script type="text/javascript">
        var menuLeft = document.getElementById( 'menu-s1' ),
        showLeftPush = document.getElementById( 'showLeftPush' ),
        main = document.getElementById( 'main' );

        
        $('body').on('click', '#openmenu', function() {

            event.preventDefault();
            var flexnavigation = document.getElementById( 'nextprev' );
            classie.toggle( this, 'open' );
            classie.toggle( main, 'menu-push-toright' );
            classie.toggle( menuLeft, 'menu-open' );
            classie.toggle( flexnavigation, 'hidden' );

        });


    </script>

    <!-- For This Page Only  -->
    <script type="text/javascript">
        // Menu Active Page Link
        $('.menu-right > li > a:eq(2)').addClass('active');

        // Other Stuff
        InitPortfolioFlexSlider();
    </script>


</body>
</html>
