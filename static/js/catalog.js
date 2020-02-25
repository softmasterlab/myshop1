'use strict';

$(window).load(function () {

    function uploadBasket() {
        $.ajax({
            url: '/catalog/upload_basket',
            success: function(result) {
                $('#count').text(result.count);
                $('#count2').text('General count: ' + result.count + ' items');
                $('#amount').text('General amount: ' + result.amount + ' uah');
            }
        });
    }
    uploadBasket();

    $('.add-to-cart-btn').click(function () {
        let product_id = $(this).parent().next().val();
        alert('Product_Id = ' + product_id);
        $.ajax({
            url: '/catalog/ajax_basket',
            data: 'pid=' + product_id,
            success: function (result) {
                alert(result.mess);
                uploadBasket();
            }
        });
    });

});