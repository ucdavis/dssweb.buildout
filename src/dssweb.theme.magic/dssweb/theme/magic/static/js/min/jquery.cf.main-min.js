!function($){function e(e){var t,a;return e.replace(/^(.*\/)?([^/]*)$/,function(e,n,o){t=n,a=o}),{dirPart:t,filePart:a}}var t=!0,a=!0,n,o="unknown",l=!1,i=.7292,r=474,s=432,d=418,c=!1,p=!1,h=!1,u="";$(document).ready(function(){function i(){0!==$("body.bio").length&&($("#about-bio").removeClass("panel panel-default"),$(".content-bio-container").removeClass(".panel-group"),$(".btn-more").show(),$("#about-bio div").removeClass("panel panel-default"),$("#about-bio h3").show(),$("#contC,#contB").addClass("more_text")),$(".panel-title a").removeAttr("data-toggle"),$(".nav > li a").removeAttr("data-toggle"),$(".nav > li").addClass("drop-on"),$(".panel-group").children().removeClass("panel panel-default"),$(".collapsible").css("height","auto"),$("#content div").children().removeClass("panel-collapse collapse active"),0!==$("body.happy-box").length&&$("#content-row div").children().removeClass("panel-collapse collapse active"),$(".panel-group .collapsible").addClass("in"),$(".more_text").hide(),$(".nav li").removeClass("open")}function s(){$("#contA",".panel .panel-collapse").addClass("active"),0!==$("body.bio").length?($(".content-bio-container").addClass("panel-group"),$("#about-bio > div").addClass("panel panel-default"),$("#sidebar-bio-right > div").addClass("panel panel-default"),$(".btn-bio").hide(),$("#about-bio h3").hide()):$(".panel-group").children().addClass("panel panel-default"),$(".panel-group .collapsible").addClass("panel-collapse collapse"),$(".panel-group .collapsible").removeClass("in"),$(".collapse > div").addClass("panel-body"),$(".nav > li").removeClass("drop-on"),$(".more_text").hide(),$(".par > a").attr("data-toggle","dropdown"),$(".panel-title a").addClass("collapsed"),$(".panel-title a").click(function(e){e.preventDefault(),g(".panel-group"),"collapsed"===$(this).attr("class")?$(this).removeClass("collapsed"):$(this).addClass("collapsed"),0===$("body.event").length&&$($(this).data("target")).show();var t=".in"+$(this).attr("data-target"),a=$(this).attr("data-target");if(u!=a){var n=0;n=$(a).offset().top>$(document).height()-$(window).height()?$(document).height()-$(window).height():$(a).offset().top,n-=35,$("html,body").animate({scrollTop:n},500,"swing"),u=a}})}function f(e){$(e).click(function(e){e.preventDefault();var t=$(this).attr("href"),a=0;a=$(t).offset().top>$(document).height()-$(window).height()?$(document).height()-$(window).height():$(t).offset().top,$("html,body").animate({scrollTop:a},500,"swing")})}function g(e){$(".in").collapse("hide")}function m(){$("#utility nav ul li").addClass("col-xs-3 col-sm-3 col-md-3 col-lg-3")}function w(){$("#utility nav ul li").removeClass("col-xs-3 col-sm-3 col-md-3 col-lg-3")}function b(){var e=0;if(0!==$(".wall").length){var t=$(".wall").height()-($("#top-bar-wrap").height()+$("#util-bar-wrap").height());e=t}return e}function v(){I(),h||k(n),A(),h||0!==$("#thumb-section").length&&x(n,"#thumb-section","section",".panel-heading"),h=!0}t&&"undefined"!=typeof window.console&&window.console.log("JQuery version:  "+$.fn.jquery),"undefined"!=typeof active_trail&&$(active_trail).addClass("active-trail"),$("#searchi").focus(function(){$("#LSResult").show()}),$("#searchi").blur(function(){$("#LSResult").hide()});var y=function(){$(".LSRow").each(function(){if($(this).find("a")){var e=$(this).find("a").attr("href");$(this).click(function(){window.open(e)})}})};0!==$("blockquote").length&&($("blockquote").addClass("open-quote"),$("blockquote").wrapInner('<span class="bq-content" />'),$("blockquote").wrapInner('<span class="close-quote" />'));var C=function(){var e=null;navigator.userAgent.match(/Windows NT 6.2; ARM(.+)Touch/)&&(e=document.createElement("style"),e.appendChild(document.createTextNode("@-ms-viewport{width:device-width}")),document.getElementsByTagName("head")[0].appendChild(e)),navigator.userAgent.match(/IEMobile\/10\.0/)&&(e=document.createElement("style"),e.appendChild(document.createTextNode("@-ms-viewport{width:auto!important}")),document.getElementsByTagName("head")[0].appendChild(e)),0!==$("form.placeholders").length&&$("form.placeholders .form-row").each(function(){var e=$(this).find("label").text();$(this).find("input, textarea").attr("placeholder",e)})};C(),$(document).foundation();var x=function(t,a,n,o){var l=a+" "+n,i=null;$(l).each(function(){if("M"===t||"L"===t)i=o+" a";else{i=".panel-body";var a=$(this).find(".thumb"),n=a.attr("src"),l=e(n),r=l.dirPart+"m-"+l.filePart;a.attr("src",r),"undefined"!=typeof window.console&&window.console.log("Bootstrapify_func: "+r+", dirPart = "+l.dirPart+", filePart = "+l.filePart)}var s=$(this).find(i);s.wrapInner('<span class="thumb-txt" />'),s.prepend($(this).find(".thumb")),$(this).addClass("thumbify-processed")}),_(a)},_=function(e){$(e+" .panel-group").children().addClass("panel panel-default"),$(e+" .panel-group .collapsible").addClass("panel-collapse collapse"),$(e+" .panel-group .collapsible").removeClass("in"),$(e+" .panel-title a").attr("data-toggle","collapse"),$(e+" .panel-title a").click(function(e){e.preventDefault(),$($(this).data("target")).show()})},S=function(e,t,a,n,o,l,i){var r=!1,s=i;if(0!==$(t).length){$(t).wrapInner('<div id="'+l+'" class="panel-group"></div>');var d=t+" "+a;return $(d).each(function(){var e=$(this),t="acont"+s,a="panel"+s;e.addClass("panel panel-default"),e.attr("id",a);var i=e.find(n);i.wrap('<div class="panel-heading" />'),i.addClass("panel-title");var d=i.find("a").attr("href");"string"==typeof i.find("a").attr("href")?(r=!0,i.find("a").addClass("collapsed").attr("data-parent",l).attr("data-target","#"+t).attr("data-toggle","collapse")):i.wrapInner('<a class="collapsed" data-parent="'+l+'" data-target="#'+t+'" data-toggle="collapse"></a>');var c=e.find(o);if(c.addClass("panel-body"),c.wrap('<div class="collapsible panel-collapse collapse" id="'+t+'"></div>'),"undefined"!=typeof window.console&&window.console.log("Bootstrapify_func: "+i.text()+" has link: "+r+", collapsible is: "+e.find(".collapsible").length),r){var p=$("<a />").addClass("readmore").attr("href",d).text("Read More");0!==e.find(".collapsible "+o).length?0!==e.find(".after-readmore").length?p.insertBefore(e.find(".after-readmore")):e.find(".collapsible "+o).append(p):0!==e.find(".after-readmore").length?p.insertBefore(e.find(".after-readmore")):e.find(".collapsible").append(p)}++s,r=!1}),s+1}return s},k=function(e){var t=20,a="XS"===e||"S"===e?!0:!1;"undefined"!=typeof window.console&&window.console.log("Is mobile: ActiveMQ: "+n+", Mobile: "+a),t=S(a,"#thumb-section","section","h3",".inline-content","accordion-thumb",t),t=S(a,".sidebar-right",".portlet","h3",".portlet-content","accordion-sr",t),a&&(t=S(a,"#cm-section","section","h2",".inline-content","accordion-cm",t),t=S(a,"#event-description","","h3",".inline-content","accordion-e",t))};if(0!==$(".picture").length&&$(".picture img").each(function(){var e=$(this).attr("title");$(this).wrap('<figure class="picture-processed" />'),"undefined"!=typeof e?$(this).parent().append("<figcaption>"+e+"</figcaption>"):0!==$(".picture .figcaption").length&&($(this).parent().append("<figcaption>"+$(".picture .figcaption").html()+"</figcaption>"),$(".picture .figcaption").remove())}),0!==$("#banner-row").length&&0!==$("#banner-row figcaption").length){var P=$("#banner-row figcaption").height(),B=$("#content-row").css("margin-top").replace("px","")-P;$("#content-row").css("margin-top",B)}0!==$("#downloads").length&&$("#downloads li").each(function(){var e=$(this).find("a"),t=e.attr("href").split(".");1===t.length||""===t[0]&&2===t.length||e.addClass(t.pop()+"-icon icon-processed")});var E={add:function(e,t,a){e.attachEvent?(e["e"+t+a]=a,e[t+a]=function(){e["e"+t+a](window.event)},e.attachEvent("on"+t,e[t+a])):e.addEventListener(t,a,!1)}};window.addEventListener("hashchange",function(e){var t=document.getElementById(location.hash.substring(1));t&&(/^(?:a|select|input|button|textarea)$/i.test(t.tagName)||(t.tabIndex=-1),t.focus())},!1);var I=function(){if(window.opera)n=window.getComputedStyle(document.body,":after").getPropertyValue("content");else if(window.getComputedStyle)n=window.getComputedStyle(document.head,null).getPropertyValue("font-family");else{window.getCompStyle=function(e,t){return this.pseudo=t,this.el=e,this.getPropertyValue=function(t){var a=/(\-([a-z]){1})/g;return"float"===t&&(t="styleFloat"),a.test(t)&&(t=t.replace(a,function(){return arguments[2].toUpperCase()})),e.currentStyle[t]?e.currentStyle[t]:null},this};var e=window.getCompStyle(document.getElementsByTagName("head")[0],"");n=e.getPropertyValue("font-family")}n=n.replace(/"/g,""),n=n.replace(/'/g,"")},L=function(){0===$("#footer #vcard").length||c||($("#footer #vcard").insertBefore($("#footer #copyright")),c=!0)},M=function(){"L"===n||"M"===n||p||($("#content").prepend($(".bio-card")),$(".bio-card .collapsible").addClass("in"),$(".breadcrumb").insertBefore($("#content .bio-card h4.fn")),p=!0)},T=function(){c&&($("#footer #vcard").insertAfter($("#footer #foot-social")),c=!1)},q=function(){p&&($(".sidebar-right .panel-group").prepend($("#content .bio-card")),$("#content").prepend($(".breadcrumb")),p=!1)},A=function(){var e=160,t=45;$("body.home #top-panel-row").height(b()),n!==o&&("XS"===n&&(o=n,m(),s(),L(),M()),"S"===n&&(o=n,0===$("body.home").length&&($(".wallpaper-image").width($(window).width()),$(".wallpaper-image").height(e),$(".wallpaper-image").css("left",0)),m(),s(),L(),M()),"M"===n&&(o=n,0!==$("body.ourpeople").length||0!==$("body.home").length,i(),L(),q()),"L"===n&&(o=n,w(),i(),T(),q()))};if(a&&(v(),E.add(window,"resize",v)),"L"===n||"M"===n){if(0!==$("body.home").length&&(f("#more-content-button a"),$(".tab").each(function(){if($(this).find("a")){var e=$(this).find("a").attr("href");$(this).click(function(){window.open(e)})}}),"none"===$("#bottom-panel-row").css("display")&&$("#bottom-panel-row").show()),0!==$(".content-title").length&&0!==$(".sidebar-right").length){var N=$(".content-title").position(),z=$(".content-title").height(),R=N.top+z+5;0!==$(".breadcrumb").length&&(R+=$(".breadcrumb").height()),$(".sidebar-right").css("margin-top",R)}var V=b();0!==$("body.has-front-am.happy-box #top-panel-row").length&&(V||(V=r),$("#top-panel-row").happybox({type:".panel",action_element_class:".action-element",canvas_element_class:".narrow-col",button_class:".btn-primary",height:V}),l=!0),0!==$("body.has-shadow-am.happy-box #top-panel-row").length&&(V||(V=d),$("#top-panel-row").happybox({type:".panel",action_element_class:".action-element",canvas_element_class:".narrow-col",button_class:".btn-primary",height:V,frozen:!0})),0!==$("body.has-shadow-am").length&&0===$("#top-panel-row").length&&0!==$("#content-row").length}else"S"===n&&0!==$("body.home").length&&(0!==$("#top-panel-row").length&&$("#top-panel-row").height("auto"),$("#bottom-panel-row").hide(),$(".homepage-title").css("cursor","pointer"),$(".homepage-title").click(function(){"none"===$("#bottom-panel-row").css("display")?$("#bottom-panel-row").show():$("#bottom-panel-row").hide()}));t&&$(window).resize(function(){"undefined"!=typeof window.console&&(window.console.log($(this).width()),window.console.log("Screen size: "+o))})})}(jQuery);