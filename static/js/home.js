document.addEventListener('DOMContentLoaded', function () {
    // Handle movie card hover effects
    const movieCards = document.querySelectorAll('.movie-card');
    movieCards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-2px)';
        });
        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    });

    // Handle search functionality
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const searchDropdown = document.getElementById('searchDropdown');
    const sortDropdown = document.getElementById('sortDropdown');
    const usersList = document.querySelector('#usersList .sidebar-list');

    // Handle search form submission
    if (searchForm) {
        searchForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const searchText = searchInput.value.trim();

            if (!searchText) return;

            const formData = new URLSearchParams();
            formData.append('search_text', searchText);

            fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: formData
            })
                .then(response => response.json())
                .then(data => {
                    if (data.movies) {
                        updateMovieResults(data.movies);
                    }
                })
                .catch(error => {
                    console.error('Search error:', error);
                });
        });
    }

    // Handle search input for live search
    if (searchInput) {
        let searchTimeout;

        searchInput.addEventListener('input', function () {
            clearTimeout(searchTimeout);
            const searchText = this.value.trim();

            if (searchText.length < 2) {
                searchDropdown.style.display = 'none';
                return;
            }

            searchTimeout = setTimeout(() => {
                const formData = new URLSearchParams();
                formData.append('search_text', searchText);

                fetch('/search', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    body: formData
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.movies && data.movies.length > 0) {
                            const dropdownContent = searchDropdown.querySelector('.dropdown-content');
                            dropdownContent.innerHTML = data.movies.map(movie => `
                            <a href="/movie/${movie.id}" class="dropdown-item">
                                <div class="media">
                                    <div class="media-left">
                                        <img class="image is-32x32" src="${movie.poster || 'https://via.placeholder.com/32x48?text=No+Poster'}" 
                                            onerror="this.src='https://via.placeholder.com/32x48?text=No+Poster'">
                                    </div>
                                    <div class="media-content">
                                        <p class="has-text-weight-semibold">${movie.title}</p>
                                        <p class="is-size-7">${movie.year} • ${movie.genre}</p>
                                    </div>
                                </div>
                            </a>
                        `).join('');
                            searchDropdown.style.display = 'block';
                        } else {
                            searchDropdown.style.display = 'none';
                        }
                    })
                    .catch(error => {
                        console.error('Search error:', error);
                        searchDropdown.style.display = 'none';
                    });
            }, 300);
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function (e) {
            if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
                searchDropdown.style.display = 'none';
            }
        });
    }

    // Function to update movie results in the page
    function updateMovieResults(movies) {
        const movieList = document.querySelector('.columns.is-multiline');
        if (!movieList) return;

        movieList.innerHTML = movies.map(movie => `
            <div class="column is-one-third">
                <a href="/movie/${movie.id}" class="movie-link">
                    <div class="movie-card">
                        <img src="${movie.poster || 'https://via.placeholder.com/300x450?text=No+Poster'}" 
                            alt="${movie.title}" class="movie-poster"
                            onerror="this.src='https://via.placeholder.com/300x450?text=No+Poster'">
                        <div class="movie-info">
                            <h3 class="movie-title">${movie.title}</h3>
                            <div class="movie-meta">
                                <span class="metascore">${movie.rating}</span>
                                <span class="user-score">${movie.year}</span>
                            </div>
                            <div class="movie-details">
                                <p><strong>Director:</strong> ${movie.director}</p>
                                <p><strong>Genre:</strong> ${Array.isArray(movie.genre) ? movie.genre.join(', ') : movie.genre}</p>
                                <p><strong>Country:</strong> ${Array.isArray(movie.country) ? movie.country.join(', ') : movie.country}</p>
                            </div>
                        </div>
                    </div>
                </a>
            </div>
        `).join('');
    }

    // Handle responsive navigation
    const navbarBurger = document.querySelector('.navbar-burger');
    const navbarMenu = document.querySelector('.navbar-menu');
    if (navbarBurger && navbarMenu) {
        navbarBurger.addEventListener('click', function () {
            this.classList.toggle('is-active');
            navbarMenu.classList.toggle('is-active');
        });
    }

    // Handle active tab highlighting
    const tabs = document.querySelectorAll('.nav-tabs .tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', function (e) {
            e.preventDefault();
            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            // Add logic to switch content based on tab
        });
    });

    // Handle movie poster image errors
    const moviePosters = document.querySelectorAll('.movie-poster');
    moviePosters.forEach(poster => {
        poster.onerror = function () {
            this.src = 'https://via.placeholder.com/220x220?text=No+Poster';
        };
    });

    // Handle infinite scroll for movie list
    let isLoading = false;
    let currentPage = 1;
    const movieList = document.querySelector('.columns.is-multiline');

    if (movieList) {
        window.addEventListener('scroll', function () {
            if (isLoading) return;

            const scrollPosition = window.innerHeight + window.scrollY;
            const documentHeight = document.documentElement.scrollHeight;

            if (scrollPosition >= documentHeight - 100) {
                isLoading = true;
                currentPage++;

                // Add loading indicator
                const loadingIndicator = document.createElement('div');
                loadingIndicator.className = 'column is-full has-text-centered';
                loadingIndicator.innerHTML = '<div class="loader"></div>';
                movieList.appendChild(loadingIndicator);

                // Simulate loading more movies (replace with actual API call)
                setTimeout(() => {
                    // Remove loading indicator
                    loadingIndicator.remove();
                    isLoading = false;
                }, 1000);
            }
        });
    }

    // Handle sidebar interactions
    const sidebarItems = document.querySelectorAll('.sidebar-list a');
    sidebarItems.forEach(item => {
        item.addEventListener('click', function (e) {
            e.preventDefault();
            sidebarItems.forEach(i => i.classList.remove('is-active'));
            this.classList.add('is-active');
            // Add logic to filter movies based on sidebar selection
        });
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

    // Handle sort dropdown functionality
    if (sortDropdown) {
        const dropdownItems = sortDropdown.querySelectorAll('.dropdown-item');
        dropdownItems.forEach(item => {
            item.addEventListener('click', function (e) {
                e.preventDefault();
                const sortBy = this.dataset.sort;
                const order = this.dataset.order;

                // Update the button text
                const button = sortDropdown.querySelector('.dropdown-trigger button');
                const icon = button.querySelector('.icon:first-child i');
                const text = button.querySelector('span:not(.icon)');

                // Update icon based on sort type
                if (sortBy === 'rating') {
                    icon.className = 'fas fa-star';
                } else if (sortBy === 'year') {
                    icon.className = 'fas fa-calendar';
                } else if (sortBy === 'title') {
                    icon.className = 'fas fa-font';
                }

                // Update text
                text.textContent = this.textContent.trim();

                // Make the API call to sort movies
                fetch(`/sort?sort=${sortBy}&order=${order}`, {
                    method: 'GET',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success && data.movies) {
                            updateMovieResults(data.movies);
                        }
                    })
                    .catch(error => {
                        console.error('Error sorting movies:', error);
                    });

                // Close the dropdown
                sortDropdown.classList.remove('is-active');
            });
        });

        // Toggle dropdown
        const trigger = sortDropdown.querySelector('.dropdown-trigger');
        trigger.addEventListener('click', function () {
            sortDropdown.classList.toggle('is-active');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function (e) {
            if (!sortDropdown.contains(e.target)) {
                sortDropdown.classList.remove('is-active');
            }
        });
    }

    // Load users list when the page loads
    if (usersList) {
        loadUsersList();
    }
}); 