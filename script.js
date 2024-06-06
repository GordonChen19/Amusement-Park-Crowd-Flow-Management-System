const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});


document.getElementById('ticketQuantity').addEventListener('change', function() {
    var ticketQuantity = parseInt(this.value);
    if (!isNaN(ticketQuantity)) {
        var totalPrice = ticketQuantity * 599; // Calculate total price
        document.getElementById('priceDisplay').textContent = 'Pay (' + totalPrice + ' RMB)';
    }
});


