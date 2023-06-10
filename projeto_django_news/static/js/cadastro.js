function exibirPopup() {
    var popup = document.getElementById("popup");
    popup.classList.remove("hidden");
    
    setTimeout(function() {
      popup.classList.add("hidden");
    }, 3000); }
  
function exibirPopupCheck() {
    var popup = document.getElementById("popup-checkbox");
    popup.classList.remove("hidden");
      
      setTimeout(function() {
        popup.classList.add("hidden");
      }, 3000); }

function validarEmail(email) {
    var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function verificarCheckboxSelecionado(idCheckbox) {
    const checkbox = document.getElementById(idCheckbox);
    return checkbox.checked;
  }