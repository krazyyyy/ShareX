window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 4000);

$(function () {

        $('.form-register input.first').blur(function () {
           if ($(this).val() == "") {
             $('.err-one').fadeIn();
           } else {
              $('.err-one').fadeOut();
           }
        });
    /************************************************************/
       // Second input
        $('.form-register input.second').blur(function () {
           if ($(this).val() == "") {
             $('.err-two').fadeIn();
           } else {
              $('.err-two').fadeOut();
           }
        });
    /************************************************************/
       // Third input
        $('.form-register input.third').blur(function () {
           if ($(this).val() == "") {
             $('.err-three').fadeIn();
           } else {
              $('.err-three').fadeOut();
           }
        });
    /************************************************************/
       // Last input
        $('.form-register input.forth').blur(function () {
           if ($(this).val() == "") {
             $('.err-four').fadeIn();
           } else {
              $('.err-four').fadeOut();
           }
        });
    /************************************************************/
    }); // Main function 

