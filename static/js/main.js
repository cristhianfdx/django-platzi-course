window.onload = () => {
    const password = document.querySelector('#password');
    const passwordConfirmation = document.querySelector('#password_confirmation');

    const confirmPassword = () => {
        passwordConfirmation.setCustomValidity('');
        if (password.value !== passwordConfirmation.value) {
            passwordConfirmation.setCustomValidity("Passwords do not match.");
        }
    };

    password.addEventListener('change', confirmPassword);
    passwordConfirmation.addEventListener('keyup', confirmPassword);
};