// Reset the entire form
function resetForm() {
    // Reset all fields in the form
    document.getElementById("methodForm").reset();

    // Reload the current page, which will reset all form fields
    location.reload();
}

// Remove the uploaded image from the form
function removeImageForm() {
    // Clear the value of the file input field (remove the uploaded image)
    document.getElementById("id_featured_image").value = '';
}
