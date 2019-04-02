$(function() { 
    $("#booksType h2").click(function(){
            $(this).toggleClass("expand");
            if ($(this).attr("class") !== "expand"){
                $(this).next().hide(); //Hide
            }
            else{
                $(this).next().show(); //Show
            }
            $("#image").attr("src", "");   	
			}
		);

    $("#web_images a, #java_images a, #net_images a, #database_images a").each(function(){
        var getURL = $(this).attr("href"); //get href attribute
        var coverBook = new Image();
		coverBook.src = getURL;

        // Event handler		
        $(this).click(
			function(){
				$("#image").attr("src", getURL);
			return false;
		});
	});
}); 