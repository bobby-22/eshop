function dropdown_list_show() {
  document.getElementById("dropdown_list").classList.toggle("dropdown_list_show");
}

var donate_button = document.getElementById("donate_button");
donate_button.onclick = function() {
  document.getElementById("window").style.display = "block";
}

var close_button = document.getElementById("close_button");
close_button.onclick = function() {
  document.getElementById("window").style.display = "none";
}