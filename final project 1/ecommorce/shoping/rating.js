document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.star');
    const ratingValue = document.getElementById('rating-value');
    const productId = "{{ product.id }}";  // Product ID for backend use

    // Set the initial state based on the product's current rating
    const initialRating = parseInt(ratingValue.textContent);
    for (let i = 0; i < initialRating; i++) {
        stars[i].classList.add('selected');
    }

    // Handle star click
    stars.forEach(star => {
        star.addEventListener('click', () => {
            const rating = parseInt(star.getAttribute('data-value'));

            // Update the UI: fill stars up to the clicked one
            stars.forEach(star => {
                star.classList.remove('selected');
            });
            for (let i = 0; i < rating; i++) {
                stars[i].classList.add('selected');
            }
            ratingValue.textContent = rating;  // Update the rating value in the UI

            // Send the rating to the server (AJAX request)
            fetch(`/rate_product/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',  // CSRF token for security
                },
                body: JSON.stringify({ rating: rating }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Rating updated:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
