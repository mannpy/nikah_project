$(document).ready(function() {

    $(".adm_btns").click(function() {
        $(".adm_menu ul").slideToggle();
    });

    $(".main_menu_button").click(function() {
        $(".main_menu ul").slideToggle();
    });

    $("#login_a").click(function(){
        $(".navbar-form").toggle(100);
    });


    //Попап менеджер FancyBox
    //Документация: http://fancybox.net/howto
    //<a class="fancybox"><img src="image.jpg" /></a>
    //<a class="fancybox" data-fancybox-group="group"><img src="image.jpg" /></a>
    $(".fancybox").fancybox({
        "padding": 0,
        "overlayOpacity": 0.1,
        });

    //Каруселька
    //Документация: http://owlgraphic.com/owlcarousel/
    var owl = $(".carousel");
    owl.owlCarousel({
        items:3,
        loop:true,
        //autoHeight:true,
    });
    $(".next_button").click(function() {
        owl.trigger("owl.next");
    });
    $(".prev_button").click(function() {
        owl.trigger("owl.prev");
    });


    //Аякс отправка форм
    //Документация: http://api.jquery.com/jquery.ajax/
    $("#callback").submit(function() {
        $.ajax({
            type: "POST",
            url: "/en/callback/",
            data: $("#callback").serialize()
        }).done(function() {
            alert("Спасибо за заявку!");
            setTimeout(function() {
                $.fancybox.close();
            }, 1000);
        });
        return false;
    });

});
