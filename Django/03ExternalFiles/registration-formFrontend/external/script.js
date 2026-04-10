document.getElementById("registerForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirmPassword").value;
    let message = document.getElementById("message");

    if (name === "" || email === "" || password === "" || confirmPassword === "") {
        message.style.color = "red";
        message.innerText = "All fields are required!";
        return;
    }

    if (password.length < 6) {
        message.style.color = "red";
        message.innerText = "Password must be at least 6 characters!";
        return;
    }

    if (password !== confirmPassword) {
        message.style.color = "red";
        message.innerText = "Passwords do not match!";
        return;
    }

    message.style.color = "green";
    message.innerText = "Registration Successful!";
});