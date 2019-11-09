
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
            email.innerHTML = "";
            password.innerHTML = "";
            if (parseInt(response.message) == 0) {
                accountRef.style.visibility = "visible";
                contactusRef.style.visibility = "visible";
                cartRef.style.visibility = "visible";
                logoutRef.style.visibility= "visible";
                greetingsRef.style.visibility = "visible";
                loginRef.style.visibility = "hidden";
                signupRef.style.visibility = "hidden";
                greetingsRef.innerHTML = `Hi, ${localStorage.getItem('name')}`;
    
            } else {
                accountRef.style.visibility = "hidden";
                contactusRef.style.visibility = "hidden";
                cartRef.style.visibility = "hidden";
                logoutRef.style.visibility= "hidden";
                greetingsRef.style.visibility = "hidden";
                loginRef.style.visibility = "visible";
                signupRef.style.visibility = "visible";
                greetingsRef.innerHTML = "";
            }
          }
        
        );
    
       
    
    
    });
});
