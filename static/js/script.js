$( document ).ready(function() {
    
    // Add the strong-underline class to the active link or url.
    // path = location.pathname;

    // if (path == "/manager/new_jobs") {
    //     $("a[href$='/manager/new_jobs']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Jobs <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/manager/signup") {
    //     $("a[href$='/manager/signup']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Add User <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/manager/show-users") {
    //     $("a[href$='/manager/show-users']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Users <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/client/jobs-list") {
    //     $("a[href$='/client/jobs-list']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Jobs <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/client/categories") {
    //     $("a[href$='/client/categories']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Settings <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/client/categories") {
    //     $("a[href$='/client/equipments']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Settings <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/client/contact") {
    //     $("a[href$='/client/contact']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Send Message <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/employee/active-jobs") {
    //     $("a[href$='/employee/active-jobs']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Active Jobs <i class="fa-solid fa-chevron-down"></i>')
    // } else if (path == "/employee/completed-jobs") {
    //     $("a[href$='/employee/completed-jobs']").addClass("strong-underline")
    //     $("#dash_menu_2_toggle").html('Completed Jobs <i class="fa-solid fa-chevron-down"></i>')
    // }


    // Feth the equipments list when a category is selected in the create job form
    $("#id_category").change(function() {
        let url = $("#create-job").attr("data-fetch-equipments-url");
        let category_id = $(this).val();
        
        fetch(`${url}?category_id=${category_id}`).then(function(response) {
            return response.json();
        }).then(function(data) {

            // loop through the response data and generate the html
            let html_data = '<option value selected>Select an equipment</option>';

            for (equipment of data) {
                html_data += `<option value="${equipment.id}">${equipment.name}</option>`;
            }
            
            $("#id_equipment").html(html_data);

        }).catch(function(err) {
            console.warn("An error ocurred:", err);
        })

    })


    // Capture the contact form
    $('#contact-form').submit(function(event) {
        event.preventDefault();
        $('#form-sent').html('Your message was sent successfully!');
        this.reset();
    })

});
