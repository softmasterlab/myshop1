'use strict';

$(window).load(function () {

    $('.add-to-cart-btn').click(function () {

        let product_id = $(this).parent().next().val();
        alert('Product_Id = ' + product_id);

        $.ajax({
            url: '/catalog/ajax_basket',
            data: 'pid=' + product_id,
            success: function (result) {
                alert(result.mess);
            }
        });

    });

});