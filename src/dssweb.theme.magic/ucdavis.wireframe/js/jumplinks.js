$(function () {
    /* CREATES JUMPLINKS MENU   */
    if ($('#about-bio h3').length != 0) {
        var cnt = $('#about-bio h3').length;
        var idx = 1;
        var anchorsTxt = [];
        anchorsTxt += '<ul id="about-bio-h3-anchors">' + "\n";



        $('#about-bio h3').each(function () {
            var anchorTxt = 'about-bio-anchor-' + idx;
            if ((idx > 1) && (idx < cnt)) {
                anchorsTxt += '<li class="leaf first">';
            } else if (idx == cnt) {
                anchorsTxt += '<li class="leaf last">';
            } else {
                anchorsTxt += '<li class="leaf">';
            }
            anchorsTxt += '<a href="#' + anchorTxt + '">' + $(this).html() + '</a>';
            anchorsTxt += '</li>' + "\n";

            // Add id to heading
            $(this).attr('id', anchorTxt);

            ++idx;
        });

        anchorsTxt += '</ul>' + "\n";
        $('.sidebar-info #overview').append(anchorsTxt);

    }
	
});