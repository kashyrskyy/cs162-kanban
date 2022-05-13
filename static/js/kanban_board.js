// Function in JavaScript for the "Add a New Task" button in "kanban_board.html".
// I slightly modified it from the original version I found online (changed id names, and modified to "inline-block")

// Reference to tutorial where I learned about this function:
// https://karthikdevarticles.com/creating-a-kanban-board-with-html-css-and-javascript#heading-javascript

function createTask(){
    var x = document.getElementById("doing");
    var y = document.getElementById("done");
    var z = document.getElementById("create-new-task-block");
    
    if (x.style.display === "none") {
      x.style.display = "inline-block";
      y.style.display = "inline-block";
      z.style.display = "none";
    } 
    else {
      x.style.display = "none";
      y.style.display = "none";
      z.style.display = "flex";}
    }
