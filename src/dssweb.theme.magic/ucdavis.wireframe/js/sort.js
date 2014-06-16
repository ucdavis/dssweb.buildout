/*        Table Sorter     */
	
$(function(){	
	
	//$(".table").tablesorter(); 
	
   $.extend($.tablesorter.themes.bootstrap, {
		table      : '.table',
		icons      : '', // add "icon-white" to make them white; this icon class is added to the <i> in the header
		sortNone   : 'glyphicon glyphicon-sort',
		sortAsc    : 'icon-chevron-up glyphicon glyphicon-chevron-up',     // includes classes for Bootstrap v2 & v3
		sortDesc   : 'icon-chevron-down glyphicon glyphicon-chevron-down', // includes classes for Bootstrap v2 & v3
		active     : '', // applied when column is sorted
		
		even       : '', // odd row zebra striping
		odd        : ''  // even row zebra striping
	  });
	
	  // call the tablesorter plugin and apply the uitheme widget
	  $("table").tablesorter({
		
		theme : "bootstrap",	
		widthFixed: true,
	
		headerTemplate : '{content} {icon}', 
		widgets : [ "uitheme" ],
	
		
	  });
});