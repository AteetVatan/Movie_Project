document.addEventListener('DOMContentLoaded', function () {
    const sortSelect = document.getElementById('sortSelect');
    const sortOrderSelect = document.getElementById('sortOrderSelect');
    const movieList = document.getElementById('movieList');
    const notification = document.getElementById('notification');

    // Handle sort changes
    function handleSortChange() {
        const sortBy = sortSelect.value;
        const sortOrder = sortOrderSelect.value;

        fetch(`/users/${userId}/sort_movies`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: `sort_by=${encodeURIComponent(sortBy)}&sort_order=${encodeURIComponent(sortOrder)}`
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Update the movie list
                    movieList.innerHTML = data.html;
                } else {
                    // Show error message
                    notification.className = 'notification is-danger';
                    notification.innerHTML = `
                    <button class="delete"></button>
                    ${data.error || 'Failed to sort movies. Please try again.'}
                `;
                    notification.style.display = 'block';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                notification.className = 'notification is-danger';
                notification.innerHTML = `
                <button class="delete"></button>
                An error occurred while sorting movies. Please try again.
            `;
                notification.style.display = 'block';
            });
    }

    // Add event listeners for sort controls
    sortSelect.addEventListener('change', handleSortChange);
    sortOrderSelect.addEventListener('change', handleSortChange);

    // Handle notification close button
    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('delete')) {
            e.target.parentElement.style.display = 'none';
        }
    });

    // Handle movie deletion
    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('delete-movie')) {
            e.preventDefault();
            const movieId = e.target.dataset.movieId;
            const movieTitle = e.target.dataset.movieTitle;

            if (confirm(`Are you sure you want to delete "${movieTitle}" from your favorites?`)) {
                fetch(`/users/${userId}/remove_movie/${movieId}`, {
                    method: 'POST',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            // Remove the movie card from the DOM
                            const movieCard = e.target.closest('.movie-card');
                            movieCard.remove();

                            // Show success message
                            notification.className = 'notification is-success';
                            notification.innerHTML = `
                            <button class="delete"></button>
                            Movie removed successfully!
                        `;
                            notification.style.display = 'block';
                        } else {
                            // Show error message
                            notification.className = 'notification is-danger';
                            notification.innerHTML = `
                            <button class="delete"></button>
                            ${data.error || 'Failed to remove movie. Please try again.'}
                        `;
                            notification.style.display = 'block';
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        notification.className = 'notification is-danger';
                        notification.innerHTML = `
                        <button class="delete"></button>
                        An error occurred while removing the movie. Please try again.
                    `;
                        notification.style.display = 'block';
                    });
            }
        }
    });
}); 