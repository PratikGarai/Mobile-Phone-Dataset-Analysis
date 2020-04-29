$(document).ready(function(){	
	var actives = 0;
	var menus = [];
	$('.menu').mouseenter(function(){
	var present = $(this).next().next().next();
	if(JSON.stringify(actives) === JSON.stringify(present)){
		return false;
	}
	else
	{
	if(actives!=0){
		actives.slideUp();
	}
	actives = $(this.children[0]).next().next();
    	actives.show();
    	return false;
	}
	});


	$('.menu').mouseleave(function(){
	actives.hide();
	actives = 0;
	return false;
	});


	$('.upb').click(function(){
	document.documentElement.scrollTop = 0;
	});
});
