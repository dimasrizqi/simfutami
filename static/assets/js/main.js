$(document).ready(function(){
	$(".button-collapse").sideNav();
	$(".dropdown-button").dropdown();
	$('select').material_select();
	$('.parallax').parallax();
	$('ul.tabs').tabs();

	$('a[href*="#_"]:not([href="#"])').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			if (target.length) {
				$('html, body').animate({
					scrollTop: target.offset().top - 71
				}, 1500);
				return false;
			}
		}
	});
});
