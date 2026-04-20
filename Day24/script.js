let darkMode = false;

function changeText() {
    document.getElementById("intro").innerText =
        "Thanks for visiting my portfolio website!";
}

function toggleTheme() {
    let button = document.getElementById("themeBtn");

    if (!darkMode) {
        document.body.style.backgroundColor = "black";
        document.body.style.color = "white";
        button.innerText = "Light Mode";
        darkMode = true;
    } else {
        document.body.style.backgroundColor = "#f4f4f4";
        document.body.style.color = "black";
        button.innerText = "Dark Mode";
        darkMode = false;
    }
}