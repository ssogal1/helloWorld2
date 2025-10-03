//What the text changes to
function changeText() {
  document.getElementById("originalParagraph").textContent =
    "YAY! You clicked the button!";
}

//Making the button work
document
    .getElementById("changeParagraphButton")
    .addEventListener("click", changeText);

//Alert with Hello, NAME!
function helloName() {
    let textInput = document.getElementById("nameInput");
    alert("Hello, " + textInput.value + "!");
}

//My favorite foods list loop
document.write("<p><strong>These are my favorite foods:</strong></p>");
let foods = ["Sushi", "Tacos", "Ice cream"];
for (let x=0; x <foods.length; x++) {
    document.write("<p>" + foods[x] + "</p>");
}

//Choose classes with checkboxes
function chooseClasses() {
    let checkboxes = document.querySelectorAll ('input[name="class"]:checked');
    let selectedClasses = "You have taken:";
    for(let i=0; i < checkboxes.length; i++) {
        selectedClasses = selectedClasses + " " + checkboxes[i].value;
    }
    alert(selectedClasses);
}

document.getElementById("submitCourses").addEventListener("click", chooseClasses);


