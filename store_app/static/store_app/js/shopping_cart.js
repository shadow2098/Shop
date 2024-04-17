var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var product_id = this.dataset.product
        var action = this.dataset.action
        console.log('product_id:', product_id, 'Action:', action)

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
            
        }else{
            update_order(product_id, action)
        }

    })
}

async function update_order(product_id, action){
    console.log('User is logged in');

    var url = 'http://127.0.0.1:8000/update_item/';

    var data = {'product_id': product_id, 'action': action};

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        console.log('Response from server:', data);
        location.reload()
    })
    .catch(error => {
        console.error('Error:', error);
    });
}