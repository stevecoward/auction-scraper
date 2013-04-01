jQuery(document).ready(function() {
    $('.view-listing').on('click',function() {
        $.ajax({
            url: '/admin/json/listing',
            type: 'POST',
            dataType: 'json',
            data: { listing_id: $(this).attr('data-listing-id') },
            done: function(data) {
                if(data['status'] == 'error') {
                    alert(data['message']);
                } else {
                    $('#listing_data').empty().val(data['data']);
                }
            }
        });
    });
});
