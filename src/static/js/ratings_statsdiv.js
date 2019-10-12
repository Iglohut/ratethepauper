
// THIS FUNCTION HANDLES IMAGE CLICK AND SHOW/HIDE DIV BEHAVIOUR
$(".card").click(function(e){
	e.preventDefault();
	console.log(e.currentTarget.id)
	var string = '.' + e.currentTarget.id
	console.log(e)

	class_elems =  document.getElementsByClassName('card');
	for (i = 0; i < class_elems.length; i++) {
	  class_elems[i].style.backgroundColor = "transparent";
	}

	document.getElementById(e.currentTarget.id).style.backgroundColor = "#BC8F8F"
     $(".replace-this").hide();
     console.log('djeeh')
     console.log(string)
    $(string).show();
});
