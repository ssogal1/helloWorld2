function changeText() {
  document.getElementById("originalParagraph").textContent = "The paragraph text has been changed since you clicked the button.";
}

function helloName() {
    let textInput = document.getElementById("textInput");
    alert("Hello " + textInput.value + "!");
}

let foods = ["Sushi", "Tacos", "Ice cream"];
for (let x=0; x <foods.length; x++) {
    document.write("<p>" + foods[x] + "</p>");
}

function chooseClasses() {
    let checkboxes = document.querySelectorAll ('input[name="class"]');
    let selectedClasses = " ";
    for(let i=0; i < checkboxes.length; i++) {
        selectedClasses = selectedClasses + " " + checkbox.value;
    }
}

alert(selectedClasses);
