jQuery(document).ready(function() {
    $('.view-listing').on('click',function() {
        var listing_id = $(this).attr('data-listing-id');
        $.getJSON('/admin/json/listing', {
            listing_id: listing_id
        }).done(function(json) {
            if(json['status'] == 'error') {
                alert(json['message']);
            } else {
                $('#listing_data').empty().val(json['data']['listing']);
                $('#listingModal').attr('data-listing-id',listing_id);
            }
        });
    });

    $('.update-listing').on('click',function() {
        var listing_id = $('#listingModal').attr('data-listing-id');
        var listing_data = $('#listing_data').val();
        $.post('/admin/json/listing/update', {
            id: listing_id,
            listing: listing_data
        }).done(function(json) {
            if(json['status'] == 'error') {
                alert(json['message']);
            } else {
                // noty notifications later on
                location.reload();
            }
        });
    });
});
