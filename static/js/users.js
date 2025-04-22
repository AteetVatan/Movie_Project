document.addEventListener('DOMContentLoaded', function () {
    // Modal functionality
    const modal = document.getElementById('addUserModal');
    const addUserCard = document.getElementById('addUserCard');
    const closeButtons = document.querySelectorAll('.modal .delete, .modal .button[onclick="closeModal()"]');
    const addUserForm = document.getElementById('addUserForm');

    // Open modal when clicking add user card
    if (addUserCard) {
        addUserCard.addEventListener('click', function () {
            modal.classList.add('is-active');
        });
    }

    // Close modal when clicking close buttons
    closeButtons.forEach(button => {
        button.addEventListener('click', function () {
            modal.classList.remove('is-active');
        });
    });

    // Close modal when clicking outside
    modal.addEventListener('click', function (e) {
        if (e.target === modal) {
            modal.classList.remove('is-active');
        }
    });

    // Handle form submission
    if (addUserForm) {
        addUserForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const submitButton = this.querySelector('button[type="submit"]');
            const errorMessage = this.querySelector('.error-message');
            const nameInput = this.querySelector('input[name="name"]');

            // Disable submit button and show loading state
            submitButton.disabled = true;
            submitButton.classList.add('is-loading');

            // Get form data
            const formData = new FormData(this);

            // Send POST request
            fetch(this.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: new URLSearchParams(formData)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.success) {
                        // Close modal and reload page to show new user
                        modal.classList.remove('is-active');
                        window.location.reload();
                    } else {
                        // Show error message
                        errorMessage.textContent = data.error || 'Failed to add user. Please try again.';
                        errorMessage.style.display = 'block';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    errorMessage.textContent = 'An error occurred while adding the user. Please try again.';
                    errorMessage.style.display = 'block';
                })
                .finally(() => {
                    // Re-enable submit button
                    submitButton.disabled = false;
                    submitButton.classList.remove('is-loading');
                });
        });
    }

    // Handle user card hover effects
    const userCards = document.querySelectorAll('.user-card');
    userCards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-2px)';
        });
        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    });

    // Handle responsive layout
    function handleResponsiveLayout() {
        const userCards = document.querySelectorAll('.user-card');
        userCards.forEach(card => {
            if (window.innerWidth < 768) {
                card.classList.add('is-mobile');
            } else {
                card.classList.remove('is-mobile');
            }
        });
    }

    // Initial call and event listener for responsive layout
    handleResponsiveLayout();
    window.addEventListener('resize', handleResponsiveLayout);
}); 