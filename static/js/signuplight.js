
            function validateForm() {
                let email = document.querySelector('.email input');
                let password = document.querySelector('.password input');
                let repassword = document.querySelector('.repassword input');

                // Check if the email is empty
                if (email.value.trim() === '') {
                    alert('Email cannot be empty');
                    return false;
                }

                // Check if the email is valid
                let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
                if (!emailPattern.test(email.value)) {
                    alert('Please enter a valid email address');
                    return false;
                }

                // Check if the password is empty
                if (password.value.trim() === '') {
                    alert('Password cannot be empty');
                    return false;
                }

                // Check if the password and repeat password match
                if (password.value !== repassword.value) {
                    alert('Passwords do not match');
                    return false;
                }

                // Check if the terms and conditions checkbox is checked
                let termsCheckbox = document.querySelector('.policies input');
                if (!termsCheckbox.checked) {
                    alert('Please accept the terms of service and policies');
                    return false;
                }

                // If all checks pass, the form can be submitted
                return true;
            }
