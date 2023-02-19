$(document).ready(function() {

    // // Capture the contact form
    $('#contact-form').submit(function(event) {
        event.preventDefault();
        let form_message = $("#id_message").val();
        let form_subject = $("#id_subject").val();
        let form_email = $("#id_email").val();


        var templateParams = {
            message: form_message,
            subject: form_subject,
            email: form_email,
        };
    
        emailjs.send("service_3a4d0k4", "the_maintenance_co", templateParams)
            .then(function(response) {
            console.log('SUCCESS!', response.status, response.text);
            }, function(error) {
            console.log('FAILED...', error);
            });
        
        $("#form-sent").css("display", "inline-block").html("Your message was sent successfully!");
        
        // Resets the contact form
        this.reset();

    })

})