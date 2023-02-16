$(document).ready(function() {

    // Contact form subject field
    $("#id_subject").focusout(function() {
        if (/^\s*$/.test($(this).val())) {
            $(this).val("");
        }
    })
    // Contact form message field
    $("#id_message").focusout(function() {
        if (/^\s*$/.test($(this).val())) {
            $(this).val("");
        }
    })



    // // RegEx no whitespaces only
    // // /^\s*$/
    // // RegEx username
    // // /^(?=.{4,16}$)(?!.*[_]{2})[a-zA-Z0-9_]+$/


    // Capture the contact form
    $('#contact-form').submit(function(event) {
        event.preventDefault();
        let form = $('#form-sent');
        form.html('Your message was sent successfully!');
        form.css("display", "block");
        this.reset();
    })

})