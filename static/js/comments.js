/* Get all elements that are needed for the following functions
Reused code from Code Institut see README.md credit */
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    // Set the value of the comment text area to the current content so the user can edit it
    commentText.value = commentContent;
    // Change the submit button's text to "Update" to indicate that this is an edit operation
    submitButton.innerText = "Update";
    // Update the form's action URL to point to the URL for editing the specific comment
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      // Set the href of the delete confirmation button to the URL for deleting the specific comment
      deleteConfirm.href = `delete_comment/${commentId}`;
      // Show the modal where the user can confirm their deletion choice
      deleteModal.show();
    });
  }
