"use strict";

$('a[data-rel]').each(function() {
    $(this).attr('rel', jQuery(this).data('rel'));
});

// Dropdown Menu
$('.dropdown-menu > li').click(function(){
    $(this).children('ul').toggle({display: "toggle"});
});

$('.menu-click-drop > a').click(function(){
    $(this).parents('div').children('.dropdown-menu').toggle({display: "toggle"});
});

/***********************************************************/
/* Back Slider
/***********************************************************/

function BackgroundSlider()
{
    // Slider Navigation
    $('#background-slider .flex-prev').hover(function(){
        $(this).css({ "background-image" : $('#background-slider li.flex-active-slide').next().css("background-image"), "width": "150px", "background-size": "cover" });
    }, function(){
        $(this).css({ "background" : "rgba(0, 0, 0, 0.2) url('css/images/left.png') no-repeat center", "width": "35px"  });
    });
    $('#background-slider .flex-next').hover(function(){
        $(this).css({ "background-image" : $('#background-slider li.flex-active-slide').next().css("background-image"), "width": "150px", "background-size": "cover" });
    }, function(){
        $(this).css({ "background" : "rgba(0, 0, 0, 0.2) url('css/images/right.png') no-repeat center", "width": "35px"  });
    });
    $('#background-slider .flex-prev').click(function(){
        $(this).css({ "background-image" : $('#background-slider li.flex-active-slide').next().css("background-image"), "width": "150px", "background-size": "cover" });
    });
    $('#background-slider .flex-next').click(function(){
        $(this).css({ "background-image" : $('#background-slider li.flex-active-slide').next().css("background-image"), "width": "150px", "background-size": "cover" });
    });
}

/***********************************************************/
/* HOME
/***********************************************************/

function InitHome()
{
    // Show Loading Animation
    function showLoaded() {
        $('#background-slider').addClass('loaded');
        $('#loading').remove();
    }
    if (window.addEventListener) { window.addEventListener('load', showLoaded, false); }
    else if (window.attachEvent) { window.attachEvent("onload", showLoaded); }
    else { showLoaded(); }

    // Slider INIT
    $('#background-slider').flexslider({
        animation: "slide",
        controlNav: false,
        prevText: "",
        nextText: "",
        start: function(){
            $('#background-slider section').removeClass('slideDown');
            $('#background-slider .flex-active-slide section').addClass('slideDown');
        },
        after: function(){
            $('#background-slider section').removeClass('slideDown');
            $('#background-slider .flex-active-slide section').addClass('slideDown');
        }
    });

    // Background SLider
    BackgroundSlider();

    // Slider FULL SCREEN + jSCROLL
    $(window).load(function(){
        var w_width  = $(window).innerWidth();
        var w_height = $(window).innerHeight();
        $("#background-slider .slides li").css({'height': w_height + 'px', 'width' : w_width + 'px'});
        $("#background-slider").css({'height': w_height + 'px', 'width' : w_width + 'px'});
    });
    $(window).resize(function(){
        var w_width  = $(window).innerWidth();
        var w_height = $(window).innerHeight();
        $("#background-slider .slides li").css({'height': w_height + 'px', 'width' : w_width + 'px'});
        $("#background-slider").css({'height': w_height + 'px', 'width' : w_width + 'px'});
    });
}

/***********************************************************/
/* BLOG
/***********************************************************/

function InitBlog()
{
    // Show Loading Animation
    function showLoaded() {
        $('#background-slider').addClass('loaded');
        $('#background-slider li').css("opacity","1");
        $('#loading').remove();
    }
    if (window.addEventListener) { window.addEventListener('load', showLoaded, false); }
    else if (window.attachEvent) { window.attachEvent("onload", showLoaded); }
    else { showLoaded(); }

    // Slider INIT
    $('#background-slider').flexslider({
        animation: "slide",
        controlNav: false,
        prevText: "",
        nextText: "",
        start: function(){
            $('#background-slider section').removeClass('slideDown');
            $('#background-slider .flex-active-slide section').addClass('slideDown');
        },
        after: function(){
            $('#background-slider section').removeClass('slideDown');
            $('#background-slider .flex-active-slide section').addClass('slideDown');
        }
    });

    // Background SLider
    BackgroundSlider();

    // Blog Filter Dropdown
    $(".blog-filter-line li").click(function(){
        $("ul", this).toggleClass("show");
    });
    $(".blog-filter-line li").mouseleave(function(){
        $("ul", this).removeClass("show");
    });
}

/***********************************************************/
/* BLOG COMMENTS
/***********************************************************/

function InitComments(){
    // Toggle Comments
    $('#hide-show-button').click(function(e){
        $('#show-hide').animate({opacity: "toggle", height: "toggle"}, 1000);
    });
}

/***********************************************************/
/* ABOUT 1 * 3
/***********************************************************/

function InitAbout()
{
    // Slider FULL SCREEN + jSCROLL
    $(window).load(function(){
        var w_height = $(window).innerHeight();
        init(w_height);
    });
    $(window).resize(function(){
        var w_height = $(window).innerHeight();
        init(w_height);
    });

    // INIT JSCROLLPANE
    var jpane;
    function init(w_height){
        $(".content-right").height(w_height);
        jpane = $('.content-right').jScrollPane({height: w_height ,  mouseWheelSpeed: 30});
    }

    // SYNAMIC TEXT + SCROLL RESET
    $(".peoples li .click").click(function(){
        // TEXT
        var text = $(this).parents('li').children('.dynamic-text').html();
        $(".content-right .text").html(text);
        // ACTIVE
        $(".peoples li").removeClass('active');
        $(this).parents('li').addClass('active');
        // SCROLL
        var api = jpane.data('jsp');
        api.reinitialise();
        api.scrollToY(0);
    });
}

/***********************************************************/
/* ABOUT 2
/***********************************************************/

function InitAboutScrollable()
{
    $("#scrollable").scrollable();

    var scrollable = $("#scrollable").data("scrollable");

    // Default Item Title
    $("#item-title").text($("#scrollable div:eq(" + (scrollable.getIndex()+1) + ") a").attr("data-title"));

    // When Scrolling Event
    scrollable.onSeek(function(event, index) {
        $("#scrollable .hover").css("background-color","rgba(0,0,0,0.6)");
        $("#scrollable div:eq(" + (scrollable.getIndex()+1) + ") .hover").css("background-color","transparent");

        // Change The Item Title
        $("#item-title").text($("#scrollable div:eq(" + (scrollable.getIndex()+1) + ") a").attr("data-title"));
    });

    $("#scrollable div a").click(function(event){

        // If Click on Item != firsd scrollable item
        if($(this).parent("div").index() != (scrollable.getIndex()) )
        {
            scrollable.seekTo($(this).parent("div").index());
            event.preventDefault();
        }
    });

    // Fancybox

    $("a.fancybox").fancybox({
        'transitionIn'	:	'elastic',
        'transitionOut'	:	'elastic',
        'speedIn'		:	600,
        'speedOut'		:	200,
        'overlayShow'	:	true,
        'overlayOpacity':   0.8,
        'overlayColor'  :   '#000',
        'padding'       :   0
    });

}

/***********************************************************/
/* PORTFOLIO
/***********************************************************/

function InitPortfolio()
{
    // Initialize scrollable
    $("#scrollable").scrollable();

    var scrollable = $("#scrollable").data("scrollable");
    var scroll = $('.pseudo-scroll .scrollbar');

    // Мне нужны числа
    var count = scrollable.getSize()

    // Смещение относительно Item
    var offset = (100 / count);
    scroll.width( offset + '%' );

    scrollable.onSeek(function() {
        var current = scrollable.getIndex() + 1;
        scroll.animate({'left': ((current * offset) - offset) + '%'});
    });
}

function InitPortfolioFlexSlider()
{
    var count = $('#carousel li').length;
    var scroll = $('.slider .scrollbar');

    var offset = (100 / count);
    scroll.width( offset + '%' );

    // Slider
    $('#slider').flexslider({
        animation: "slide",
        controlNav: false,
        animationLoop: false,
        slideshow: false,
        sync: "#carousel",
        nextText: "",
        prevText: "",
        after: function(slider){
            var current = slider.currentSlide + 1;
            scroll.animate({'left': ((current * offset) - offset) + '%'});
        }
    });

    var slider = $("#carousel");

    // Thumbs
    $('#carousel').flexslider({
        animation: "slide",
        controlNav: false,
        directionNav: false,
        animationLoop: false,
        slideshow: false,
        asNavFor: '#slider',
        itemWidth: 100,
        smoothHeight: true
    });

    // Show Story When Click
    $('.slider .hover .content').click(function(){
        $(this).parent('.hover').css({display: 'none'});
        $(this).parents('li').children('.story').css({visibility: 'visible', opacity: 1});
    });

    // Close Story
    $('.slider .close').click(function(){
        $(this).parents('.story').css({visibility: 'hidden', opacity: 0});
        $(this).parents('li').children('.hover').css({display: 'block'});
    });
}

