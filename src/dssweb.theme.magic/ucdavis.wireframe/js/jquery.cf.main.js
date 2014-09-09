$(function(){	
	$(document).ready(function() {
		
		// foundation top-bar support. Note: Add after any JavaScript constructed markup that relies on foundation
		$(document).foundation(); 
		
		if (typeof window.console == "object") {
			window.console.log("JQuery version:  " + $.fn.jquery);
		}
		
		// Activate home page happy boxes
		if($('body.home #top-panel-row').length != 0) {
			$('body.home #top-panel-row').happybox(
				{
					'type': '.panel', // element type to make happy
					'action_element_class': '.action-element',
					'canvas_element_class': '.narrow-col',
					'button_class': ".btn-primary",
					'height': 520 // total height of the happy viewport
				}
			);
		}
		
		// Get picture figure/figcaption
		// TODO: Plugin
		if($('.picture').length != 0) {
      $('.picture img').each(function () {
				var title = $(this).attr('title');
				$(this).wrap('<figure class="picture-processed" />');
				$(this).parent().append("<figcaption>"+title+"</figcaption>");
      });
		}		
		
	});
});