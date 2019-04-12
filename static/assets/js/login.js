jQuery(function($) {
	$('.form-control').on('focus', function() {
		$(this).parents('.input-group').find('.input-group-addon', 0).css('color', '#2ed1a2');
	}).on('focusout', function() {
		$(this).parents('.input-group').find('.input-group-addon', 0).css('color', '#dddddd');
	});
});
