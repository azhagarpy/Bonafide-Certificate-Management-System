const cancelButton = document.getElementById("cancel");
const model = document.querySelector(".model");
const closeModel = document.querySelector("#closeModel");


closeModel.addEventListener("click",()=>{
    model.style.display="none";
})

cancelButton.addEventListener("click",popUp)

function popUp() {
        model.style.display="flex";

}
