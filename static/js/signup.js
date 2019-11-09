
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
           
            // Callback handler that will be called on success
            request.done(function (response){
                email.innerHTML = "";
                password.innerHTML = "";
                name.innerHTML = "";
                if (response.token != 0) {
                    accountRef.style.visibility = "visible";
                    contactusRef.style.visibility = "visible";
                    cartRef.style.visibility = "visible";
                    logoutRef.style.visibility= "visible";
                    greetingsRef.style.visibility = "visible";
                    loginRef.style.visibility = "hidden";
                    signupRef.style.visibility = "hidden";
                    greetingsRef.innerHTML = `Hi, ${localStorage.getItem('name')}`;
                    localStorage.setItem('token', response.token);
                    localStorage.setItem('name', response.name);
        
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
                
                
                
               
                
                
            });
        
        
        });
});
    