$(function() {
	var $form = $('#registerForm');
	var $tooltip = $('<div id="vld-tooltip">提示信息！</div>');
	$tooltip.appendTo($('#modal-register'));

	$form.validator();

	var validator = $form.data('amui.validator');

	$form.on('focusin focusout', '.am-form-error input', function(e) {
	  if (e.type === 'focusin') {
	    var $this = $(this);
	    var offset = $this.offset();
	    var msg = $this.data('foolishMsg') || validator.getValidationMessage($this.data('validity'));

	    $tooltip.text(msg).show().css({
	      left: 10,
	      top: offset.top-50
	    });
	  } else {
	    $tooltip.hide();
	  }
	});

	$('#detail').hover(function() {
		$('.classify').slideDown().css({'opacity':1});
	},function() {
		$('.classify').slideUp().css({'opacity':0});
	});
		
	$('.uinfo-inner').hover(function() {
		$('#user-menu-profile').filter(':not(:animated)').slideDown(300);
		$('.face').filter(':not(:animated)').addClass('scale-in')
	},function() {
		$('#user-menu-profile').filter(':not(:animated)').slideUp(300);
		$('.face').filter(':not(:animated)').removeClass('scale-in')
	})
})