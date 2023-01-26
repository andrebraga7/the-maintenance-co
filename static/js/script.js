// // Toggle the active class in the dashboard menu buttons
$( document ).ready(function() {
    
    path = location.pathname;

    if (path == "/manager/") {
        $("a[href$='/manager/']").addClass("active")
    } else if (path == "/manager_active/") {
        $("a[href$='/manager_active/']").addClass("active")
    } else if (path == "/manager_completed/") {
        $("a[href$='/manager_completed/']").addClass("active")
    }

});
