$(function(){	
	$(document).ready(function() {
		
		$(document).foundation();
		
		if (typeof window.console == "object") 
			window.console.log("JQuery version:  " + $.fn.jquery);
		
		if($('body.home #top-panel-row').length != 0) {
			$('body.home #top-panel-row').happybox(
				{
					'type': '.panel', // element type to make happy
					'action_element_class': '.action-element',
					'canvas_element_class': '.narrow-col',
					'button_class': ".btn-primary",
					'height': 478 // total height of the happy viewport
				}
			);
		}
	});
});