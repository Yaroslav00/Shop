
$(document).ready(function(){
    $("form").submit(function(event){
        event.preventDefault();
        var email = $("#email").val();
        var password = $("#password").val();
        
        signup_data = {
            email:email,
            password: password
        };
        request = $.ajax({
            url: "/api/v1/auth/login",
            type: "post",
            data: signup_data
        });
        
        // Callback handler that will be called on success
        request.done(function (response){
            // Log a message to the console
            console.log("Hooray, it worked!");
            console.log(response);
        });
    
    
    });
});
