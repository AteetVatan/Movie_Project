document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('movieSearch');
    const searchResults = document.getElementById('searchResults');
    const addMovieForm = document.getElementById('addMovieForm');
    const selectedMovieTitle = document.getElementById('selectedMovieTitle');
    const submitButton = addMovieForm.querySelector('button[type="submit"]');
    const notification = document.getElementById('notification');
    const closeNotification = document.getElementById('closeNotification');
    const loadingSpinner = searchResults.querySelector('.loading');
    const usersList = document.querySelector('#usersList .sidebar-list');

    let searchTimeout;

    searchInput.addEventListener('input', function () {
        clearTimeout(searchTimeout);
        const searchText = this.value.trim();

        if (searchText.length < 2) {
            searchResults.innerHTML = `
                <div class="loading" style="display: none;">
                    <div class="loading-spinner"></div>
                    <p>Searching for movies...</p>
                </div>
            `;
            return;
        }

        // Show loading spinner
        searchResults.innerHTML = `
            <div class="loading">
                <div class="loading-spinner"></div>
                <p>Searching for movies...</p>
            </div>
        `;

        searchTimeout = setTimeout(() => {
            fetch('/get_imdb_movie', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `title=${encodeURIComponent(searchText)}`
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Received data:', data);
                    if (data.success) {
                        const movie = data.movie;
                        console.log('Movie data:', movie);

                        // Helper function to format arrays and handle N/A values
                        const formatValue = (value) => {
                            if (Array.isArray(value)) {
                                return value.join(', ');
                            }
                            if (typeof value === 'string' && value.includes(',')) {
                                return value.split(',').map(item => item.trim()).join(', ');
                            }
                            return value === 'N/A' ? 'Not Available' : value;
                        };

                        // Format the movie data
                        const formattedMovie = {
                            title: movie.title || 'Unknown Title',
                            rating: formatValue(movie.rating),
                            year: formatValue(movie.year),
                            genre: formatValue(movie.genre),
                            director: formatValue(movie.director),
                            plot: formatValue(movie.plot),
                            poster: movie.poster || 'https://via.placeholder.com/300x450?text=No+Poster'
                        };
                        console.log('Formatted movie:', formattedMovie);

                        const movieHTML = `
                            <div class="movie-result" data-movie='${JSON.stringify(movie)}'>
                                <div class="movie-result-header">
                                    <img src="${formattedMovie.poster}" alt="${formattedMovie.title}" class="movie-poster">
                                    <div class="movie-details">
                                        <h2 class="movie-title">${formattedMovie.title}</h2>
                                        <div class="movie-meta">
                                            <span class="movie-rating">${formattedMovie.rating}</span>
                                            <span class="movie-year">${formattedMovie.year}</span>
                                        </div>
                                        <div class="movie-info">
                                            <p><strong>Genre:</strong> ${formattedMovie.genre}</p>
                                            <p><strong>Director:</strong> ${formattedMovie.director}</p>
                                            <p class="movie-plot">${formattedMovie.plot}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `;
                        console.log('Generated HTML:', movieHTML);
                        searchResults.innerHTML = movieHTML;
                    } else {
                        searchResults.innerHTML = `
                            <div class="notification is-warning">
                                <p>${data.error}</p>
                            </div>
                        `;
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    searchResults.innerHTML = `
                        <div class="notification is-danger">
                            <p>Error searching for movies. Please try again.</p>
                        </div>
                    `;
                });
        }, 300);
    });

    searchResults.addEventListener('click', function (e) {
        const movieResult = e.target.closest('.movie-result');
        if (movieResult && movieResult.dataset.movie) {
            try {
                const movie = JSON.parse(movieResult.dataset.movie);
                console.log('Selected movie:', movie);

                // Update hidden form fields
                selectedMovieTitle.value = movie.title;
                document.getElementById('selectedMovieData').value = JSON.stringify(movie);

                // Update displayed movie information
                const display = document.getElementById('selectedMovieDisplay');
                display.style.display = 'block';

                // Helper function to format arrays and handle N/A values
                const formatValue = (value) => {
                    if (Array.isArray(value)) {
                        return value.join(', ');
                    }
                    if (typeof value === 'string' && value.includes(',')) {
                        return value.split(',').map(item => item.trim()).join(', ');
                    }
                    return value === 'N/A' ? 'Not Available' : value;
                };

                // Update all display elements
                document.getElementById('selectedMovieTitleDisplay').textContent = movie.title || 'Unknown Title';
                document.getElementById('selectedMoviePoster').src = movie.poster || 'https://via.placeholder.com/300x450?text=No+Poster';
                document.getElementById('selectedMovieRating').textContent = formatValue(movie.rating);
                document.getElementById('selectedMovieYear').textContent = formatValue(movie.year);
                document.getElementById('selectedMovieGenre').textContent = formatValue(movie.genre);
                document.getElementById('selectedMovieDirector').textContent = formatValue(movie.director);
                document.getElementById('selectedMoviePlot').textContent = formatValue(movie.plot);

                // Enable submit button
                submitButton.style.display = 'block';

                // Clear search results and input
                searchResults.innerHTML = '';
                searchInput.value = movie.title;
            } catch (error) {
                console.error('Error parsing movie data:', error);
            }
        }
    });

    // Close notification when clicking the close button
    closeNotification.addEventListener('click', function () {
        notification.classList.add('is-hidden');
    });

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

    // Handle form submission
    addMovieForm.addEventListener('submit', function (e) {
        // Do not prevent default - let the form submit normally
        submitButton.classList.add('is-loading');
        submitButton.disabled = true;
    });

    // Load users list when the page loads
    if (usersList) {
        loadUsersList();
    }
}); 