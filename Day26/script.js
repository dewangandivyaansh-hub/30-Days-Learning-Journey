function submitForm(event) {
    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let message = document.getElementById("message").value.trim();
    let response = document.getElementById("response");

    if (name === "" || email === "" || message === "") {
        response.innerText = "Please fill in all fields.";
        return;
    }

    if (!email.includes("@") || !email.includes(".")) {
        response.innerText = "Please enter a valid email address.";
        return;
    }

    response.innerText =
        "Thank you! Your message has been submitted successfully.";
}