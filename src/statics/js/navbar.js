
// HIGHLIGHT THE CURRENT PAGE AT NAVBAR
var url = location.href.split("/"); //replace string with location.href
var navLinks = document.getElementsByClassName("sidebar-nav")[0].getElementsByTagName("a");
//naturally you could use something other than the <nav> element
var i=0;
var count = 0
var currentPage = url[url.length - 2];
for(i;i<navLinks.length;i++){
  var lb = navLinks[i].href.split("/");
  if(lb[lb.length-1] == currentPage) {
   navLinks[i].className = "active";
   count += 1;
   // console.log(currentPage)
  } 
}
if (count==0){
	navLinks[0].className = "active";
}
