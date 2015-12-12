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

	//chooseReq
	function chooseReq(element) {
		var chooseInput = $('#chooseInput');
		$(element).each(function() {
			$(this).click(function() {
				var text = $(this).text();
				chooseInput.attr('placeholder',text).val(text);
			})
		})
	}
	chooseReq('.sub-list li');
	chooseReq('.cat-list span')

	//文件选择显示已选文件
	$('#des-file-input').on('change', function() {
      var fileNames = '';
      $.each(this.files, function() {
        fileNames += '<span class="am-badge">' + this.name + '</span> ';
      });
      $('#file-list').html(fileNames);
    });

    // servers标签切换
    function serverTab (tabs,content) {
    	$(tabs).each(function(index,element) {

    		$(this).click(function(e) {
    			e.preventDefault();
    			$(tabs).removeClass('active');
    			$(content).removeClass('active');
 
    			var id = $(this).find('a').attr('href');
    			showToggle(id);

    			if($(this).attr('class').indexOf('active')<=-1) {
    				$(this).addClass('active');
    			}

    		})
    	})
    }

    function showToggle(id) {
    	if($(id).attr('class').indexOf('active')<=-1) {
    		$(id).addClass('active')
    	} else {
    		return;
    	}
    }

    serverTab('.box-tabs-nav li','.server-tab-panel');
})