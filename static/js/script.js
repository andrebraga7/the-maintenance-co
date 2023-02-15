$( document ).ready(function() {
    
    // Add the strong-underline class to the active link defined by the hidden input.
    let activeButtonId = $("#active-button").val();
    let activeToggleValue = $("#active-button").attr("name");
    
    // Add the .strong-underline class
    $(activeButtonId).addClass("strong-underline");

    // Define the html for the active toggle button
    $("#dash_menu_2_toggle").html(activeToggleValue + ' <i class="fa-solid fa-chevron-down"></i>');


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
