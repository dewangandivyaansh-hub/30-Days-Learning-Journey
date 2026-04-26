window.onload = function () {
    loadTasks();
};

function getTasks() {
    return JSON.parse(localStorage.getItem("tasks")) || [];
}

function saveTasks(tasks) {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task.");
        return;
    }

    let tasks = getTasks();
    tasks.push({ text: taskText, completed: false });

    saveTasks(tasks);
    renderTasks();

    taskInput.value = "";
}

function renderTasks() {
    let taskList = document.getElementById("taskList");
    taskList.innerHTML = "";

    let tasks = getTasks();

    tasks.forEach((task, index) => {
        let li = document.createElement("li");

        li.innerText = task.text + " ";

        if (task.completed) {
            li.style.textDecoration = "line-through";
        }

        let completeBtn = document.createElement("button");
        completeBtn.innerText = "Complete";

        completeBtn.onclick = function () {
            toggleComplete(index);
        };

        let editBtn = document.createElement("button");
        editBtn.innerText = "Edit";

        editBtn.onclick = function () {
            editTask(index);
        };

        let deleteBtn = document.createElement("button");
        deleteBtn.innerText = "Delete";

        deleteBtn.onclick = function () {
            deleteTask(index);
        };

        li.appendChild(completeBtn);
        li.appendChild(editBtn);
        li.appendChild(deleteBtn);

        taskList.appendChild(li);
    });
}

function toggleComplete(index) {
    let tasks = getTasks();
    tasks[index].completed = !tasks[index].completed;

    saveTasks(tasks);
    renderTasks();
}

function editTask(index) {
    let tasks = getTasks();

    let newText = prompt("Edit your task:", tasks[index].text);

    if (newText && newText.trim() !== "") {
        tasks[index].text = newText.trim();

        saveTasks(tasks);
        renderTasks();
    }
}

function deleteTask(index) {
    let tasks = getTasks();

    tasks.splice(index, 1);

    saveTasks(tasks);
    renderTasks();
}

function loadTasks() {
    renderTasks();
}