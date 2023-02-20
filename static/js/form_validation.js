$(document).ready(function() {


    // Contact form subject field validation
    $("#id_subject").focusout(function() {
        if ($(this).val().trim() === "") {
            $(this).val("");
        }
    });

    // Contact form message field
    $("#id_message").focusout(function() {
        if ($(this).val().trim() === "") {
            $(this).val("");
        }
    });

    // Job description field
    $("#id_description").focusout(function() {
        if ($(this).val().trim() === "") {
            $(this).val("");
        }
    });

    // Signup form username field

    $("#id_username").attr("pattern", "^[a-zA-Z0-9@]{5,}$");
    $("#div_id_username").append(
        `<span class='form-help-text ps-2'>
            Username must contain only letters, numbers and @
        </span>`
    );

    // Signup form name field
    $("#id_name").attr("pattern", "^[a-zA-Z0-9]+( [a-zA-Z0-9]+)*$");

    // Signup form password fields
    $("#id_password1").attr("minlength", "8");
    $("#id_password2").attr("minlength", "8");

    $("#id_password2").focusout(function() {
        
        let pass1 = $("#id_password1");
        let pass2 = $(this);

        if (pass1.val() != pass2.val()) {
            pass1.addClass("is-invalid");
            pass2.addClass("is-invalid");
            $("#div_id_password2").append(
                "<span class='invalid-feedback'><strong>Passwords are not the same!<strong></span>");
        } else {
            pass1.removeClass("is-invalid");
            pass2.removeClass("is-invalid");
        }


    });

});