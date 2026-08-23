(function ($) {
    "use strict";

    $(function () {
        $("#spinner").removeClass("show");

        function updateNavigation() {
            $(".navbar").toggleClass("sticky-top", $(window).scrollTop() > 45);
            if ($(window).scrollTop() > 300) {
                $(".back-to-top").css("display", "grid");
            } else {
                $(".back-to-top").hide();
            }
        }

        updateNavigation();
        $(window).on("scroll", updateNavigation);

        $(".back-to-top").on("click", function (event) {
            event.preventDefault();
            $("html, body").animate({ scrollTop: 0 }, 500);
        });

        $("#menu .nav-link").on("click", function () {
            var menu = document.getElementById("menu");
            if (menu && menu.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(menu).hide();
            }
        });
    });
})(jQuery);
