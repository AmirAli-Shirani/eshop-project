function addProductToOrder(productId) {
    const productCount = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button_text
        })
    });
}

function RemoveOrderDetail(detailId) {
    $.get('/dashboard/add-to-order/?detailId=' + detailId).then(res=>{
        if(res.status === 'success'){
            $('#order-detail-content').html(res.body);
        }
    });
}