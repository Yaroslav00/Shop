
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
            console.log(response.token);
            email.innerHTML = "";
            password.innerHTML = "";
            if (response.token != null) {
                
                
                localStorage.setItem('token', response.token);
                localStorage.setItem('name', response.name);
                localStorage.setItem('admin', response.admin);
                if(response.admin=='false')
                {
                    window.location.href='Account.html';
                }
                else{
                    window.location.href='Admin.html';
                }
                
                
    
            } else {
                Warning.style.visibility = "visible";
                Warning.innerHTML = "Credentials are incorrect!";
                
            }
          }
        
        );
    
       
    
    
    });
});
