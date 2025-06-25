// Preview image when selected for upload
document.getElementById("image-input").addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const previewImage = document.getElementById("preview-image");
            previewImage.src = e.target.result;
            previewImage.style.display = "block";
        };
        reader.readAsDataURL(file);
    }
});

// Show/hide additional options based on selected action
const actionSelect = document.getElementById("action-select");
const actionOptions = document.querySelectorAll(".action-options");

actionSelect.addEventListener("change", function () {
    actionOptions.forEach(option => option.style.display = "none"); // Hide all options
    const selectedAction = actionSelect.value;
    const selectedOptions = document.getElementById(${selectedAction}-options);
    if (selectedOptions) {
        selectedOptions.style.display = "block"; // Show relevant options
    }
});