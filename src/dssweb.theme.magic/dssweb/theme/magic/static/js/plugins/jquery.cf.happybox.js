/*!
 * jQuery Happy Box
 * Original author: regan@cakefarm.com
 * Licensed under the MIT license
 */

;(function ( $, window, document, undefined ) {
    
    // Create the defaults once
    var pluginName = 'happybox',
        defaults = {
            version: "1.0-alpha",
						type: "div",
						action_element_class: '.happy-content',
						canvas_element_class: '.happy-canvas',
						button_class: 'happy-btn',
						button_height: 50,
						pclass: "cf-happybox-processed",
						height: 200
        };

    // The actual plugin constructor
    function Plugin( element, options ) {
        this.element = element;

        // jQuery has an extend method that merges the 
        // contents of two or more objects, storing the 
        // result in the first object. The first object 
        // is generally empty because we don't want to alter 
        // the default options for future instances of the plugin
        this.options = $.extend( {}, defaults, options) ;
        
        this._defaults = defaults;
        this._name = pluginName;
        
        this.init();
				
    }

    Plugin.prototype.init = function () {
        // Place initialization logic here
        // You already have access to the DOM element and
        // the options via the instance, e.g. this.element 
        // and this.options
				
				$(this.element).addClass(this.options.pclass);
				$(this.element).height(this.options.height);
				
				if (typeof window.console == "object") 
					window.console.log("Happybox is happy!");
				
				var out = "";
				var item = $(this.element);
				//window.console.log("Target: " + $(this.element).attr('class'));
				var happy_parent = this;
				$(this.element).children().filter(this.options.type).each(function(index) {
					//out += "Element: "+$(this).attr('class')+"\n";
					var action_element = $(this).find(happy_parent.options.action_element_class);
					var canvas_element = $(this).find(happy_parent.options.canvas_element_class);
					var action_control = happy_parent.options.button_class;
					var h = action_element.height();
					
					// Activate canvas
					$(canvas_element).hover( happy_parent._handleCanvasIn, happy_parent._handleCanvasOut );
					
					// Box controls
					
					/*
					$(action_control).click(function(){
				    if (open == false){
				    	action_element.animate({
				        "bottom" : "0px"
				    	});

				    	open = true;
				    }else{
				    	action_element.animate({
				        "bottom" : "-170px"
				    	});

				    	open = false;
				    }
					});*/
					
					// Click event - Close
					$(canvas_element).click(function() {
						var animObj = $(this).parent().parent();
						/*if(typeof window.console == "object") window.console.log("Happybox: class="+$(this).attr('class')+", click event");
						animObj.stop().animate({
							'paddingTop': -270
						}, 900, "easeOutBounce");*/
						
						$(this).animate({
						'paddingTop': (happy_parent.options.button_height - happy_parent.options.height) // (how much of the box should peek out)
						}, 900, "easeOutBounce", function() {
							// $( this ).after( "<div>Animation complete.</div>" );
						});
						
					});
					
					// Hover event - Get happy feet
					$(canvas_element).hover(function() {
						var animObj = $(this).parent().parent();
						var height = $(this).height();
						if(typeof window.console == "object") window.console.log("Happybox: class="+$(this).attr('class')+", easeOutBounce1 event");
						animObj.stop().animate({
							'paddingTop': (happy_parent.options.height - height) // stick boxes to bottom: TODO: Have max-height 
						}, 900, "easeOutBounce");
						}, function() {
						var animObj = $(this).parent().parent();
						if(typeof window.console == "object") window.console.log("Happybox: class="+$(this).attr('class')+", easeOutBounce2 event");
						animObj.stop().animate({
							'paddingTop': (happy_parent.options.height - happy_parent.options.button_height)
						}, 900, "easeOutBounce");
					});
							
					if(typeof window.console == "object") 
						window.console.log("Happybox " + $(this).attr('class') + " height: "+ h);
					
					// Determine behavior
					
					happy_parent._happy();
					
					// Temporary: TODO: Remove ...
					action_element.css('padding-top', (happy_parent.options.height-happy_parent.options.button_height));
					//action_element.css('border','1px solid blue');
					
				});
				//window.console.log("Happybox has these parameters:\n" + out);
			
				
    };

		Plugin.prototype._happy = function (element) {
			window.console.log("Happybox: crazy");
			$
		};
		
		Plugin.prototype._handleCanvasIn = function () {
			window.console.log("Happybox: _handleCanvasIn()");
			// Move a box up a bit
			//$(this).css('border','1px solid white');
			//$(this).animate({ marginTop: 0 }, {duration: 1000, easing: 'easeOutBounce'});
		};
		
		Plugin.prototype._handleCanvasOut = function () {
			window.console.log("Happybox: _handleCanvasOut()");
			//$(this).css('border-color','#002855');
		};
		
    // A really lightweight plugin wrapper around the constructor, 
    // preventing against multiple instantiations
    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, 'plugin_' + pluginName)) {
                $.data(this, 'plugin_' + pluginName, 
                new Plugin( this, options ));
            }
        });
    }

})( jQuery, window, document );