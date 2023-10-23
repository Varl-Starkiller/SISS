const loginInputs = document.querySelectorAll('.login-input-parent input');
loginInputs.forEach((inputBox) =>{
    inputBox.addEventListener('input', ()=>{
        const label = inputBox.previousElementSibling;
        if(inputBox.value){
            label.classList.add('active-label');
            inputBox.style.borderColor = "#0038FF"
            inputBox.style.caretColor = "#000000"
        }
        else {
            label.classList.remove('active-label')
            inputBox.style.borderColor = "#000000"
            inputBox.style.caretColor = "#ffffff"
        }
    });
});
document.querySelector('.sign-in-button').addEventListener('click', ()=>{
    const email = document.getElementById('email').value;
    const passwordConfirm = document.getElementById('password').value;
    console.log(email)
    console.log(passwordConfirm);
})
