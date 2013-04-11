jQuery(document).ready(function() {
    $('.pop').hover(function() {
        $(this).popover({
            'placement': 'left'
        });
        $(this).popover('toggle');
    });
});
