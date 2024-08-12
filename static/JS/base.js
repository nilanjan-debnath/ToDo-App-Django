function show_updateform(id) {
  const update_form = document.getElementById("update_form" + id);
  const update_btn = document.getElementById("update_btn" + id);
  update_form.classList.add("show");
}
function hide_updateform(id) {
  const update_form = document.getElementById("update_form" + id);
  const cancel_update = document.getElementById("cancel_update" + id);
  update_form.classList.remove("show");
}
function delete_todo(id) {
  if (confirm("Are you sure?")) {
    window.location.href = "/delete/" + id;
  }
}
