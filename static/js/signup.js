
$(document).ready(function(){
        $("form").submit(function(event){
            event.preventDefault();
            var email = $("#email").val();
            var password = $("#password").val();
            var name = $("#name").val();
            signup_data = {
                name: name,
                email:email,
                password: password
                
            };
            request = $.ajax({
                url: "/api/v1/auth/signup",
                type: "post",
                data: signup_data
            });
            console.log(signup_data)
            // Callback handler that will be called on success
            request.done(function (response){
                // Log a message to the console
                console.log("Hooray, it worked!");
                console.log(response.token);
                // Put the object into storage
                localStorage.setItem('token', response.token);
                localStorage.setItem('name', response.name);
                var token = localStorage.getItem('token');
                console.log(token);
                // Retrieve the object from storage
                
            });
        
        
        });
});
    