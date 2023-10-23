document.addEventListener("DOMContentLoaded", () =>{
    const loginInputs = document.querySelectorAll('.login-input-parent input')
    loginInputs.forEach((inputBox) =>{
        if(inputBox.value !==""){
            inputBox.classList.toggle('active-label')
        }
    })
})