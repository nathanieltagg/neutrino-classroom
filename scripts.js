$(function(){
  // var currentUrl = window.location.href; 
  var url = window.location.href.split('/');
  var currentUrl =  url[url.length-1];
  
  var currentMenuItem = $("#cssmenu li a[href='" + currentUrl + "']");
  currentMenuItem.parents('li').addClass("active");
  // console.log("currentUrl",currentUrl);
  // console.log("currentMenuItem",currentMenuItem);
});