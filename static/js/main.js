// Button
const btn = document.querySelector('#login')

// Eye
const eye = document.querySelector('#eye');

// Input
const inputPassword = document.querySelector('#password-field');
const inputLogin = document.querySelector('#username');

// Error
const errorLogin = document.querySelector('.error-feedback-login')
const errorPassword = document.querySelector('.error-feedback-password')

const form = document.querySelector(".signin-form");
form.addEventListener("submit", loginSubmit);
// Passord visibility
eye.addEventListener('click', () => {
	if (eye.classList.contains('fa-eye')) {
		eye.classList.remove('fa-eye')
		eye.classList.add('fa-eye-slash')
		inputPassword.type = 'text';
	} else {
		eye.classList.add('fa-eye')
		eye.classList.remove('fa-eye-slash')
		inputPassword.type = 'password';
	}
})


// Validation 
function loginSubmit(event) {
	event.preventDefault();
	if (inputLogin.value === '' && inputPassword.value === '') {
		errorLogin.textContent = 'Loginingizni kiriting.!'
		errorPassword.textContent = 'Parolingizni kiriting.!'
	}
	else if (inputLogin.value === '') {
		errorLogin.textContent = 'Loginingizni kiriting.!'
	}
	else if (inputPassword.value === '') {
		errorPassword.textContent = 'Parolingizni kiriting.!'
	}
}
inputLogin.addEventListener('change', () => {
	errorLogin.textContent = '';
})
inputPassword.addEventListener('change', () => {
	errorPassword.textContent = '';
})

