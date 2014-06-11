// JavaScript Document

$(function(){
 
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
	
    });