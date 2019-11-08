window.onload = function() {
    var token = localStorage.getItem('token');
    $.ajax(
        {
            url: "localhost/api/v1/", 
    success: function(result){
        console.log(result);
      }
    }
    );
    changePage(1);
    console.log(page);
};