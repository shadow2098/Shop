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
/*
function update_order(product_id, action){
    console.log('User is authenticated, sending data...')

        var url = '/update_item/'

        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            }, 
            body:JSON.stringify({'product_id':product_id, 'action':action})
        })
        .then((response) => {
           return response.json();
        })
        .then((data) => {
            console.log('data:', data)
        });
}
*/
// Function to send a POST request to update_item endpoint
async function update_order(product_id, action){
    console.log('User is logged in');

    var url = 'http://127.0.0.1:8000/update_item/';

    // Prepare data object with product_id and action
    var data = {'product_id': product_id, 'action': action};

    // Send POST request with JSON payload
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        // Handle response
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .then(data => {
        // Handle JSON response data
        console.log('Response from server:', data);
        location.reload()
    })
    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });
}