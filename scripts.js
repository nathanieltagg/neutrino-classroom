  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-67955401-1', 'auto');
  ga('send', 'pageview');


$(function(){
  // var currentUrl = window.location.href; 
  var url = window.location.href.split('/');
  var currentUrl =  url[url.length-1]; 
  if(currentUrl=="") currentUrl="index.html";
  console.log(currentUrl);
  var currentMenuItem = $("#cssmenu li a[href='" + currentUrl + "']");
  currentMenuItem.parents('li').addClass("active");
  // console.log("currentUrl",currentUrl);
  // console.log("currentMenuItem",currentMenuItem);
});
