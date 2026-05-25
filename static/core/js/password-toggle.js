/**
 * Password Toggle Functionality
 * Handles show/hide password functionality for login forms
 */

document.addEventListener('DOMContentLoaded', function() {
    // Get all password toggle buttons
    const passwordToggleButtons = document.querySelectorAll('.password-toggle');

    passwordToggleButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            // Find the password input in the same input-group or sc-input-group
            const inputGroup = this.closest('.input-group') || this.closest('.sc-input-group');
            if (!inputGroup) return;

            const passwordInput = inputGroup.querySelector('input[type="password"], input[type="text"]');
            const icon = this.querySelector('i');

            if (!passwordInput || !icon) return;

            // Toggle between password and text input types
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                passwordInput.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });
});
