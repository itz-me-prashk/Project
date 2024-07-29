/*const signInButton = document.getElementById('signIn');
const signUpButton = document.getElementById('signUp');
const container = document.querySelector('.container');

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
    container.classList.remove('left-panel-active');
});

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
    container.classList.add('left-panel-active');
});
*/
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');
    
    if (username === 'user' && password === 'password') {
        alert('Login successful!');
        errorMessage.style.display = 'none';
    } else {
        errorMessage.textContent = 'Invalid username or password';
        errorMessage.style.display = 'block';
    }
});
