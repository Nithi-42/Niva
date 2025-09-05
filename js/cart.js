document.addEventListener('DOMContentLoaded', function () {
    
    let user = window.user || 'AnonymousUser';
    let csrftoken = window.csrftoken || '';

    let updateBtns = document.querySelectorAll('.update-cart');

    updateBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            let productId = this.dataset.product;
            let action = this.dataset.action;

            console.log('Product ID:', productId, 'Action:', action);

            if (user === 'AnonymousUser') {
                console.log('User not logged in');
            } else {
                updateUserOrder(productId, action);
            }
        });
    });

    function updateUserOrder(productId, action) {
        console.log('User is authenticated, sending data...');

        fetch('/updateitem/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({'productId': productId, 'action': action})
        })
        .then(response => response.json())
        .then(data => {
            console.log('Data:', data);
            location.reload();
        });
    }
});
