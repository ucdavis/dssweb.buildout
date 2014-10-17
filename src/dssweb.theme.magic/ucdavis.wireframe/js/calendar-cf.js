

/* TODO: Figure out why mover function is double wrapping elements */

/* Pending completion 
$(document).ready(function() {
	
	var activeMQ;
	var elems = document.getElementsByTagName('div'), i; // get all divs and index them for parsing
  var el; 
	var tag;
	var content;
	
	//set the class data to be used depending on page
	function initialize() {
		if($('body.event').length !== 0) {
			if ((activeMQ === 'S') || (activeMQ === 'XS')) {				
				el = 'todays-event';//class to grab
				tag = document.getElementsByTagName(el);	// get tags			
				content = document.getElementById('calendar');//What element to insert after
				var items = new itemizer(el, tag, content);
			}		
			items.mover(items.el, items.content);			
		}			
	}	
	
	function itemizer (el, tag, content) {
		this.el = el;
		this.tag = tag;
		this.content = content;
	}
	
	//function to move the item to after the specified div
	itemizer.prototype.mover = function (matchClass, content) {
		
		var x = 0;
		var event_id = 'active-event-';
		var item;		
		
		for (i in elems) {			
			// matches the class name to the el list. this method is supported cross browsers
			if((' ' + elems[i].className + ' ').indexOf(' ' + matchClass + ' ') > -1) {
					item = document.getElementsByClassName(elems[i].className);
					//console.log(item);					
					$(item).wrapInner('<div id="'+ event_id + x + '" class="event-group visible-sm visible-xs"></div>');
					$(item).insertAfter(content);
					console.log(elems[i]);
					x++;
			}
    }
	}

	var mqSync = function () {
        // Fix for Opera issue when using font-family to store value
        if (window.opera) {
					// TODO: Check that content is available after changing this from class to id
           activeMQ = window.getComputedStyle(document.body, ':after').getPropertyValue('content');
        }
        // For all other modern browsers
        else if (window.getComputedStyle) {
           activeMQ = window.getComputedStyle(document.head, null).getPropertyValue('font-family');
        }
        // For oldIE
        else {
            // Use .getCompStyle instead of .getComputedStyle so above check for window.getComputedStyle never fires true for old browsers
            window.getCompStyle = function (el, pseudo) {
							this.pseudo = pseudo;
                this.el = el;
                this.getPropertyValue = function (prop) {
                    var re = /(\-([a-z]){1})/g;
                    if (prop === 'float') {
											prop = 'styleFloat';
										}
                    if (re.test(prop)) {
                        prop = prop.replace(re, function () {
                            return arguments[2].toUpperCase();
                        });
                    }
                    return el.currentStyle[prop] ? el.currentStyle[prop] : null;
                };
                return this;
            };
            var compStyle = window.getCompStyle(document.getElementsByTagName('head')[0], "");
            activeMQ = compStyle.getPropertyValue("font-family");
        }
        activeMQ = activeMQ.replace(/"/g, "");
        activeMQ = activeMQ.replace(/'/g, "");
    }; // End mqSync
		mqSync();
		initialize();
});
*/