var actualizarBtns = document.getElementsByClassName('actualizar-carrito');

var updateBtn = document.getElementsByClassName('update-cart');


for (i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('idProducto: ', productId, 'Action:', action);

        console.log('USER:', user);

        if (user === 'AnonymousUser') {
            console.log('Usuario no registrado');
        } else {
            updateUserOrderOnCart(productId, action);
        }
    });
}

for (i = 0; i < actualizarBtns.length; i++) {
    actualizarBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('idProducto: ', productId, 'Action:', action);

        console.log('USER:', user);

        if (user === 'AnonymousUser') {
            console.log('Usuario no registrado');
        } else {
            updateUserOrder(productId, action);
        }
    });
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...');

    var url = 'agregar_producto/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action }),
    })
        .then((response) => {
            return response.json();
        })

        .then((data) => {
            console.log('data:', data);
            location.reload();
        });
}

function updateUserOrderOnCart(productId, action) {
    console.log('User is logged in, sending data...');

    var url = '../agregar_producto/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action }),
    })
        .then((response) => {
            return response.json();
        })

        .then((data) => {
            console.log('data:', data);
            location.reload();
        });
}


