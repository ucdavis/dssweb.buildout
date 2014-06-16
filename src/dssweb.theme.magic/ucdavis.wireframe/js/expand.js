// KS: JavaScript Document

/* Change history: 

  - 2014-06-12 RAK: Fix style assignment error and add debug and toggleActive mode
  - 
  TODO:
  
  - Refactor ...
  
*/

$(function(){
	var debug = false;
	var toggleActive = true;
	
    $('.btn-more').click(function(event){ 
 
        event.preventDefault(); /* prevent the a from changing the url */
        $(this).parents('.about-bio').find('.more_text').show(); 
		$('.btn-more').hide();
		$('.btn-less').show();
	});
	
	$('.btn-less').click(function(event){ 
	
		event.preventDefault(); 
        $(this).parents('.about-bio').find('.more_text').hide(); 
		$('.btn-less').hide();
		$('.btn-more').show();
	});
		
		/*--used for tabs view---*/
    $('#myTab a').click(function(e) {
		e.preventDefault();
		$(this).tab('show');
	  });
	 		
	if(toggleActive) {
	  $("contA").collapse('toggle');
  	$("contB").collapse('toggle');
  	$("contC").collapse('toggle');
	}
	
		// Add Events Cross-browser
	var event = {
		add: function(elem, type, fn) {
			if (elem.attachEvent) {
				elem['e'+type+fn] = fn;
				elem[type+fn] = function() {elem['e'+type+fn](window.event);}
				elem.attachEvent('on'+type, elem[type+fn]);
			} else
			elem.addEventListener(type, fn, false);
		}
	};
	
	// Set default
	var currentMQ = "unknown";
	
	// Checks CSS value in active media query and syncs Javascript functionality
	var mqSync = function(){
	
		// Fix for Opera issue when using font-family to store value
		if (window.opera){
			var activeMQ = window.getComputedStyle(document.body,':after').getPropertyValue('content');
		}
		// For all other modern browsers
		else if (window.getComputedStyle) 
		{
			var activeMQ = window.getComputedStyle(document.head,null).getPropertyValue('font-family');
		}
		// For oldIE
		else {
			// Use .getCompStyle instead of .getComputedStyle so above check for window.getComputedStyle never fires true for old browsers
			window.getCompStyle = function(el, pseudo) {
				this.el = el;
				this.getPropertyValue = function(prop) {
					var re = /(\-([a-z]){1})/g;
					if (prop == 'float') prop = 'styleFloat';
					if (re.test(prop)) {
						prop = prop.replace(re, function () {
							return arguments[2].toUpperCase();
						});
					}
					return el.currentStyle[prop] ? el.currentStyle[prop] : null;
				}
				return this;
			}
			var compStyle = window.getCompStyle(document.getElementsByTagName('head')[0], "");
			var activeMQ = compStyle.getPropertyValue("font-family");
		}
	
		activeMQ = activeMQ.replace(/"/g, "");
		activeMQ = activeMQ.replace(/'/g, "");
	
		// Conditions for each breakpoint
		if (activeMQ != currentMQ) {
			
			
			if (activeMQ == 'XS') {
				 currentMQ = activeMQ;
				console.log('XS');
				 $(".landscape div").removeClass("tab-pane");
				 $(".landscape div").addClass("col-lg-4");
				 $(".landscape").removeClass("span12");				
				 $(".nav-tabs").hide();
				 $(".content-main").show();
				 $(".btn-less").show();
				 
					 								
			    $(".panel div").removeClass("panel-collapse collapse in");
				$(".panel div").removeClass("panel-collapse collapse");
				$(".panel div").removeClass("panel-collapse collapse");
				$(".about-bio").removeClass("panel panel-default");
				$(".collapse > div").removeClass("panel-body");
				$(".content-bio-container").removeClass(".panel-group");
				
			    $(".btn-more").show();
				$(".panel-heading").hide();
				$("#contB").addClass("more_text");
				$("#contC").addClass("more_text");
				$(".about-bio div").removeClass("panel panel-default");
				$(".more_text").hide();
				$(".about-bio h3").show();
				 
			}
			if (activeMQ == 'S') {
				 currentMQ = activeMQ;
				console.log('S');
				$(".landscape div").removeClass("tab-pane");
				$(".landscape div").addClass("col-lg-4");
				$(".landscape").removeClass("span12");	
				$(".content-main").show();		
				$(".nav-tabs").hide();
				$(".btn-less").show();
				$(".sidebar-bio").css("margin",'0 auto');

				$(".collapse > div").removeClass("panel-body");				
			    $(".panel div").removeClass("panel-collapse collapse in");
				$(".panel div").removeClass("panel-collapse collapse");
				$(".panel div").removeClass("panel-collapse collapse");
				$(".about-bio").removeClass("panel panel-default");
				$(".content-bio-container").removeClass(".panel-group");
				
				$(".btn-more").show();
				$(".panel-heading").hide();
				
				$(".about-bio div").removeClass("panel panel-default");
				$(".more_text").hide();
			    $(".about-bio").attr("style", "width:100%");
				//$(".sidebar-bio-right").style.marginLeft ='0';
				$(".about-bio h3").show();
			
				
			}
			if (activeMQ == 'M') {
				 currentMQ = activeMQ;
				console.log('M');
			    $(".ls-content").addClass("tab-content");
				$(".landscape div").addClass("tab-pane");
				$(".landscape").removeClass("tab-content");
				$("#contA").addClass("active");			
				$(".landscape div").removeClass("col-lg-4");
				$(".landscape").addClass("span12");			
				$(".nav-tabs").show();
				
				
			
				$(".panel-heading").show();		
				$(".collapse > div").addClass("panel-body");	
			   	$(".more_text").hide();
			    $("#contA").addClass("panel-collapse collapse in");
				$("#contB").addClass("panel-collapse collapse");
				$("#contC").addClass("panel-collapse collapse");
				$(".about-bio").attr("style", "width:62%");
				$(".content-bio-container").addClass("panel-group");				
				$(".about-bio > div").addClass("panel panel-default");
				
			
				
				$(".panel-title a").click(function(e){
					e.preventDefault();
					 $($(this).data("target")).show();
				});
			
				$(".btn-bio").hide();
				
				
				/* FIX: cannot target panel-body h3 element directly, work-around ".about-bio h3" used */
				//alert($(".panel-body > h3").text());
				
				$(".about-bio h3").hide();


			}
			if (activeMQ == 'L') {
				currentMQ = activeMQ;
				console.log('L');
				$(".ls-content").removeClass("tab-content");
				$(".landscape div").removeClass("tab-pane");
				$(".landscape div").addClass("col-lg-4");
				$(".ls-content").removeClass("col-lg-4");
				$(".landscape").removeClass("span12");				
				$(".nav-tabs").hide();
				
				
				$(".collapse > div").removeClass("panel-body");				
			    $("#contA").removeClass("panel-collapse collapse in");
				$("#contB").removeClass("panel-collapse collapse");
				$("#contC").removeClass("panel-collapse collapse");
				$(".about-bio").removeClass("panel panel-default");
				$(".content-bio-container").removeClass(".panel-group");
				$(".about-bio").attr("style", "width:62%");
				$(".btn-more").show();
				$(".panel-heading").hide();
				$("#contB").addClass("more_text");
				$("#contC").addClass("more_text");
				$(".about-bio div").removeClass("panel panel-default");
				$(".more_text").hide();
				$(".about-bio h3").show();
			}
		}
	
	}; // End mqSync
	
	
	if(toggleActive) {
	  mqSync();
	
	  // Run on resize
	  event.add(window, "resize", mqSync);
  }
	
	if(debug) {
  	$(window).resize(function(){
  		console.log($(this).width());
  	});
	}
	
});
	
