document.getElementById("stats-Example").style.visibility= "visible";
document.getElementById("card-Example").className = "hover-br-active mycard";

// THIS FUNCTION HANDLES IMAGE CLICK AND SHOW/HIDE DIV BEHAVIOUR
$(".mycard").click(function(e){
	e.preventDefault();
	// console.log(e.currentTarget.id)
	var string = e.currentTarget.id.replace("card-",".")
	// console.log(e)

	class_elems =  document.getElementsByClassName('mycard');
	for (i = 0; i < class_elems.length; i++) {
	  // class_elems[i].style.backgroundColor = "transparent";
	  class_elems[i].className = "hover-br mycard"
	}

	// document.getElementById(e.currentTarget.id).style.backgroundColor = "#BC8F8F"
	document.getElementById(e.currentTarget.id).className = "hover-br-active mycard";
    //  $(".replace-this").hide();
    //  console.log('djeeh')
    //  console.log(string)
    // $(string).show();
    document.querySelectorAll(".replace-this").forEach(a=>a.style.visibility = "hidden")

    // document.querySelectorAll(".replace-this").forEach(a=>a.style.display = "none");
    // document.querySelectorAll(string).forEach(a=>a.style.display = "block");
    document.querySelectorAll(string).forEach(a=>a.style.visibility = "visible");
    document.getElementById("stats-"+string.replace(".","")).scrollIntoView({ behavior: 'smooth', block: 'center' });


});





// THIS FUNCTION HANDLES IMAGE CLICK AND SHOW/HIDE DIV BEHAVIOUR
$(".mycard").click(function(e){
	e.preventDefault();
	// console.log(e.currentTarget.id)
	var string = e.currentTarget.id.replace("card-",".")
	// console.log(e)

	class_elems =  document.getElementsByClassName('mycard');
	for (i = 0; i < class_elems.length; i++) {
	  // class_elems[i].style.backgroundColor = "transparent";
	  class_elems[i].className = "hover-br mycard"
	}

	// document.getElementById(e.currentTarget.id).style.backgroundColor = "#BC8F8F"
	document.getElementById(e.currentTarget.id).className = "hover-br-active mycard";
    //  $(".replace-this").hide();
    //  console.log('djeeh')
    //  console.log(string)
    // $(string).show();
    // document.querySelectorAll(".replace-this").forEach(a=>a.style.visibility = "hidden")

    document.querySelectorAll(".replace-this-form").forEach(a=>a.style.display = "none");
    document.querySelectorAll(string).forEach(a=>a.style.display = "block");
    // document.querySelectorAll(string).forEach(a=>a.style.visibility = "visible");
    document.getElementById("stats-"+string.replace(".","")).scrollIntoView({ behavior: 'smooth', block: 'center' });


});