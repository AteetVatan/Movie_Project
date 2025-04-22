document.addEventListener('DOMContentLoaded', function () {
    // Handle poster image error
    const moviePoster = document.querySelector('.card-image img');
    if (moviePoster) {
        moviePoster.onerror = function () {
            this.src = 'https://via.placeholder.com/300x450?text=No+Poster';
        };
    }

    // Handle breadcrumb navigation
    const breadcrumbLinks = document.querySelectorAll('.breadcrumb a');
    breadcrumbLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            window.location.href = this.getAttribute('href');
        });
    });

    // Handle responsive layout
    function handleResponsiveLayout() {
        const movieDetails = document.querySelector('.content');
        if (movieDetails) {
            if (window.innerWidth < 768) {
                movieDetails.classList.add('is-mobile');
            } else {
                movieDetails.classList.remove('is-mobile');
            }
        }
    }

    // Initial call and event listener for responsive layout
    handleResponsiveLayout();
    window.addEventListener('resize', handleResponsiveLayout);

    // Handle actor tags hover effect
    const actorTags = document.querySelectorAll('.tags .tag');
    actorTags.forEach(tag => {
        tag.addEventListener('mouseenter', function () {
            this.classList.add('is-primary');
        });
        tag.addEventListener('mouseleave', function () {
            this.classList.remove('is-primary');
        });
    });

    // Handle notes section if present
    const notesSection = document.querySelector('.notification');
    if (notesSection) {
        notesSection.addEventListener('click', function () {
            this.classList.toggle('is-light');
        });
    }
}); 