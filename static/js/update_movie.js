document.addEventListener('DOMContentLoaded', function () {
    const updateMovieForm = document.getElementById('updateMovieForm');
    const submitButton = updateMovieForm.querySelector('button[type="submit"]');
    const notification = document.getElementById('notification');
    const closeNotification = document.getElementById('closeNotification');
    const usersList = document.querySelector('#usersList .sidebar-list');
    const movieNotes = document.getElementById('movieNotes');
    const notesError = document.getElementById('notesError');

    // Load users list
    function loadUsersList() {
        fetch('/users', {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (!data.users || data.users.length === 0) {
                        usersList.innerHTML = `
                        <li class="no-users-message">
                            <div class="has-text-centered">
                                <span class="icon is-large">
                                    <i class="fas fa-user-plus fa-2x"></i>
                                </span>
                                <p class="mt-2">No users yet</p>
                                <a href="/users" class="button is-small is-info mt-2">
                                    Add Your First User
                                </a>
                            </div>
                        </li>
                    `;
                    } else {
                        usersList.innerHTML = data.users.map(user => `
                        <li>
                            <a href="/users/${user.id}">
                                <span class="icon-text">
                                    <span class="icon">
                                        <i class="fas fa-user"></i>
                                    </span>
                                    <span>${user.name}</span>
                                </span>
                            </a>
                            <span class="tag is-info is-light">${user.movie_count} movies</span>
                        </li>
                    `).join('');
                    }
                }
            })
            .catch(error => {
                console.error('Error loading users:', error);
                usersList.innerHTML = `
                <li class="has-text-danger has-text-centered">
                    <span class="icon">
                        <i class="fas fa-exclamation-circle"></i>
                    </span>
                    <p>Error loading users</p>
                    <button class="button is-small is-danger mt-2" onclick="location.reload()">
                        <span class="icon">
                            <i class="fas fa-redo"></i>
                        </span>
                        <span>Try Again</span>
                    </button>
                </li>
            `;
            });
    }

    // Close notification when clicking the close button
    if (closeNotification) {
        closeNotification.addEventListener('click', function () {
            notification.classList.add('is-hidden');
        });
    }

    // Handle form submission
    if (updateMovieForm) {
        updateMovieForm.addEventListener('submit', function (e) {
            const notes = movieNotes.value.trim();

            if (!notes) {
                e.preventDefault();
                notesError.style.display = 'block';
                notification.classList.remove('is-hidden', 'is-success');
                notification.classList.add('is-danger');
                notification.querySelector('.message').textContent = 'Please enter some notes about the movie.';
                return false;
            }

            notesError.style.display = 'none';
            notification.classList.add('is-hidden');

            // Disable submit button and show loading state
            submitButton.classList.add('is-loading');
            submitButton.disabled = true;

            // Create request body
            const requestBody = new URLSearchParams();
            requestBody.append('notes', notes);

            // Send request to server
            fetch(updateMovieForm.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: requestBody
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.success) {
                        // Show success message
                        notification.classList.remove('is-hidden', 'is-danger');
                        notification.classList.add('is-success');
                        notification.querySelector('.message').textContent = 'Movie updated successfully!';

                        // Redirect to user's movies page after 2 seconds
                        setTimeout(() => {
                            window.location.href = `/users/${data.user_id}`;
                        }, 2000);
                    } else {
                        throw new Error(data.error || 'Failed to update movie');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    // Show error message
                    notification.classList.remove('is-hidden', 'is-success');
                    notification.classList.add('is-danger');
                    notification.querySelector('.message').textContent = error.message;
                })
                .finally(() => {
                    // Re-enable submit button
                    submitButton.classList.remove('is-loading');
                    submitButton.disabled = false;
                });
        });
    }

    // Load users list when the page loads
    if (usersList) {
        loadUsersList();
    }
}); 