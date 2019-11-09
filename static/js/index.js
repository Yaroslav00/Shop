
$(document).ready(function(){
    changePage(1)
    if (localStorage.getItem('token') != null)
    {
    var token = localStorage.getItem('token');
    parsed_token = parseJwt(token);
  
    console.log(parsed_token.exp);
    console.log(Math.floor(Date.now() / 1000));
    if (parsed_token.exp < Math.floor(Date.now() / 1000))
    {
        localStorage.removeItem('token');
        localStorage.removeItem('name');
        greetingsRef.innerHTML = "";
    }
    else{
        greetingsRef.innerHTML = `Hi, ${localStorage.getItem('name')}`;
    }
}
    if (localStorage.getItem('token') != null)
    {
        console.log("Token in storage");
    $.ajax(
        {
            url: "/api/v1/auth/isauth", 
            type: "get",
            data: {token: token},
    success: function(result){
        
        if (parseInt(result.message) == 0) {
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
    }
    );
}
    else{
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

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
};