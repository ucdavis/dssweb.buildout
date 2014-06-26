/*
	By Osvaldas Valutis, www.osvaldas.info
	Available for use under the MIT License
*/



;(function( $, window, document, undefined ){
	
	
	$.fn.doubleTapToGo = function( params )
	{
			
		//if( !( 'ontouchstart' in window ) &&
			//!navigator.msMaxTouchPoints &&
		 // !navigator.userAgent.toLowerCase().match( /windows phone os 7/i ) ) return false;

		this.each( function()
		{
			
			var curItem = false;

			$( this ).on( 'click', function( e )
			{
				// get element that is clicked
				var item = $( this );
				//if element has not already been clicked
				if( item[ 0 ] != curItem[ 0 ] )
				{
					//prevent window location change
					e.preventDefault();
					//set current element
					curItem = item;
				}
			});

			$( document ).on( 'click touchstart MSPointerDown', function( e )
			{
				var resetItem = true,
					parents	= $( e.target ).parents();
		
				for( var i = 0; i < parents.length; i++ )
					if( parents[ i ] == curItem[ 0 ] )
						resetItem = false;

				if( resetItem )
					curItem = false;
			});
		});
		return this;
	};
	//$( '.par:has(ul)' ).doubleTapToGo();
})( jQuery, window, document );
