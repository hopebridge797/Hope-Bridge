// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Handle user form submission
  const userForm = document.getElementById('userForm');
  userForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    // Navigate to the appropriate page after form submission
    window.location.href = 'index2.html'; // Link to the page for request submissions
  });

  // Handle donor form submission
  const donorForm = document.getElementById('donorForm');
  donorForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    // Navigate to the appropriate page after form submission
    window.location.href = 'index3.html'; // Link to the page for donation submissions
  });
});