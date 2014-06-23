// KS: JavaScript Document
/* Change history: 

  - 2014-06-12 RAK: Fix style assignment error and add debug and toggleActive mode
  - 
  TODO:
  
  - Refactor ...
  
*/
/* toggles the text shown on bio */
$(function () {
    var debug = false;
    var toggleActive = true;

    $('.btn-more').click(function (event) {

        event.preventDefault(); /* prevent the a from changing the url */
        $(this).parents('#about-bio').find('.more_text').show();
        $('.btn-more').hide();
        $('.btn-less').show();
    });

    $('.btn-less').click(function (event) {

        event.preventDefault();
        $(this).parents('#about-bio').find('.more_text').hide();
        $('.btn-less').hide();
        $('.btn-more').show();
    });

    /*--used for tabs view---*/
    $('#myTab a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

    if (toggleActive) {
        $("contA").collapse('toggle');
        $("contB").collapse('toggle');
        $("contC").collapse('toggle');
    }

    // Add Events Cross-browser
    var event = {
        add: function (elem, type, fn) {
            if (elem.attachEvent) {
                elem['e' + type + fn] = fn;
                elem[type + fn] = function () {
                    elem['e' + type + fn](window.event);
                }
                elem.attachEvent('on' + type, elem[type + fn]);
            } else
                elem.addEventListener(type, fn, false);
        }
    };

    // Set default
    var currentMQ = "unknown";

    // Checks CSS value in active media query and syncs Javascript functionality
    var mqSync = function () {

        // Fix for Opera issue when using font-family to store value
        if (window.opera) {
            var activeMQ = window.getComputedStyle(document.body, ':after').getPropertyValue('content');
        }
        // For all other modern browsers
        else if (window.getComputedStyle) {
            var activeMQ = window.getComputedStyle(document.head, null).getPropertyValue('font-family');
        }
        // For oldIE
        else {
            // Use .getCompStyle instead of .getComputedStyle so above check for window.getComputedStyle never fires true for old browsers
            window.getCompStyle = function (el, pseudo) {
                this.el = el;
                this.getPropertyValue = function (prop) {
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
								utilStack();
                collapsedView();

            }
            if (activeMQ == 'S') {
                currentMQ = activeMQ;
                console.log('S');
								utilStack();
                collapsedView();
            }
            if (activeMQ == 'M') {
                currentMQ = activeMQ;
                console.log('M');
								rmvStack();
                collapsedView();								

            }
            if (activeMQ == 'L') {
                currentMQ = activeMQ;
                console.log('L');
								rmvStack();
                expandedView();

            }
        }


    }; // End mqSync


    if (toggleActive) {
        mqSync();

        // Run on resize
        event.add(window, "resize", mqSync);
    }

    if (debug) {
        $(window).resize(function () {
            console.log($(this).width());
        });
    }

    function expandedView() {
        $(".ls-content").removeClass("tab-content");
        $(".landscape div").removeClass("tab-pane");
        $(".nav-tabs").hide();

        $(".collapsible").children().removeClass("panel-body");
        /* If Bio Page */
				if ($("body.bio").length != 0) {
            $("#about-bio").removeClass("panel panel-default");
            $(".content-bio-container").removeClass(".panel-group");
            $(".btn-more").show();                                     
            $("#contC,#contB").addClass("more_text");
            $("#about-bio div").removeClass("panel panel-default");
						$("#about-bio h3").show();
        }
        
				$(".panel-title a").removeAttr('data-toggle');
				$(".sidebar-panel").removeClass("panel-collapse collapse in");;
          							
				$(".sidebar").children().removeClass("panel panel-default");
				$(".collapsible").css("height", "auto"); //Fix for contA height not being reset to auto	
				$(".content div").children().removeClass("panel-collapse collapse active");
				$(".content .panel-heading").hide();
				$(".panel-group").children().removeClass("panel panel-default")        
        $(".more_text").hide();
       

    }

    function collapsedView() {

        $(".ls-content").addClass("tab-content");
        $(".landscape div").addClass("tab-pane");
        $(".landscape").removeClass("tab-content");
        $("#contA").addClass("active");
        $(".nav-tabs").show();
								
        $(".panel-heading").show();
        $(".more_text").hide();				

        if ($("body.bio").length == 0) {					  
            $(".sidebar").children().addClass("panel panel-default");
						$(".panel-group").children().addClass("panel panel-default");
            $(".sidebar-panel").addClass("panel-collapse collapse");
            $(".collapse div").addClass("panel-body");

        }
				/* If Bio Page */
				else if ($("body.bio").length != 0) {
            $(".content-bio-container").addClass("panel-group");
						$("#about-bio > div").addClass("panel panel-default");
						$("#sidebar-bio-right > div").addClass("panel panel-default");
						$(".btn-bio").hide();
						 $("#about-bio h3").hide();
        }
				$(".panel-title a").attr("data-toggle","collapse");
        $(".collapsible").addClass("panel-collapse collapse");
        $(".collapse > div").addClass("panel-body");
     
        $(".panel-title a").click(function (e) {
            e.preventDefault();
            $($(this).data("target")).show();
				
				});

        /* FIX: cannot target panel-body h3 element directly, work-around ".about-bio h3" used */
        //alert($(".panel-body > h3").text());

       

    }
		function utilStack(){
		  $("#utility nav ul li").addClass("col-xs-3 col-sm-3 col-md-3 col-lg-3");				
		}
		function rmvStack(){
			$("#utility nav ul li").removeClass("col-xs-3 col-sm-3 col-md-3 col-lg-3");					
		}
});