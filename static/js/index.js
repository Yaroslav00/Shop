
$(document).ready(function(){
    console.log("sdfscs");
    var token = localStorage.getItem('token');

    $.ajax(
        {
            url: "/api/v1/auth/isauth", 
            type: "get",
            data: {token: token},
    success: function(result){
        console.log(result);
        if (parseInt(result.message) == 0) {
            accountRef.style.visibility = "visible";
            contactusRef.style.visibility = "visible";
            cartRef.style.visibility = "visible";
            logoutRef.style.visibility= "visible";
            greetings.style.visibility = "visible";
            loginRef.style.visibility = "hidden";
            signupRef.style.visibility = "hidden";

        } else {
            accountRef.style.visibility = "hidden";
            contactusRef.style.visibility = "hidden";
            cartRef.style.visibility = "hidden";
            logoutRef.style.visibility= "hidden";
            greetings.style.visibility = "hidden";
            loginRef.style.visibility = "visible";
            signupRef.style.visibility = "visible";
        }
      }
    }
    );
    
  
});