window.onload = function() {
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