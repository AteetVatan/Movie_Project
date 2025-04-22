document.addEventListener('DOMContentLoaded', function () {
    const updateForm = document.getElementById('updateMovieForm');
    const notification = document.getElementById('notification');
    const submitButton = updateForm.querySelector('button[type="submit"]');

    updateForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Disable submit button and show loading state
        submitButton.disabled = true;
        submitButton.classList.add('is-loading');

        // Get form data
        const formData = new FormData(updateForm);
        const notes = formData.get('notes');

        // Create request body
        const requestBody = new URLSearchParams();
        requestBody.append('notes', notes);

        // Send update request
        fetch(updateForm.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: requestBody
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    // Show success message
                    notification.className = 'notification is-success';
                    notification.innerHTML = `
                    <button class="delete"></button>
                    Movie updated successfully!
                `;
                    notification.style.display = 'block';

                    // Redirect to user movies page after a short delay
                    setTimeout(() => {
                        window.location.href = `/users/${userId}/movies`;
                    }, 1500);
                } else {
                    // Show error message
                    notification.className = 'notification is-danger';
                    notification.innerHTML = `
                    <button class="delete"></button>
                    ${data.error || 'Failed to update movie. Please try again.'}
                `;
                    notification.style.display = 'block';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                notification.className = 'notification is-danger';
                notification.innerHTML = `
                <button class="delete"></button>
                An error occurred while updating the movie. Please try again.
            `;
                notification.style.display = 'block';
            })
            .finally(() => {
                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.classList.remove('is-loading');
            });
    });

    // Handle notification close button
    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('delete')) {
            e.target.parentElement.style.display = 'none';
        }
    });
}); 