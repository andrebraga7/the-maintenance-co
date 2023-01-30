// // Toggle the active class in the dashboard menu buttons
$( document ).ready(function() {
    
    path = location.pathname;

    if (path == "/manager/jobs-list") {
        $("a[href$='/manager/jobs-list']").addClass("strong-underline")
        $("#dash_menu_2_toggle").html('Jobs <i class="fa-solid fa-chevron-down"></i>')
    } else if (path == "/manager/signup") {
        $("a[href$='/manager/signup']").addClass("strong-underline")
        $("#dash_menu_2_toggle").html('Add User <i class="fa-solid fa-chevron-down"></i>')
    } else if (path == "/manager/show-users") {
        $("a[href$='/manager/show-users']").addClass("strong-underline")
        $("#dash_menu_2_toggle").html('Users <i class="fa-solid fa-chevron-down"></i>')
    }

});
