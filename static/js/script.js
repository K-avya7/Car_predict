// Store references to commonly used DOM elements
const form = document.getElementById('form1');
const salaryInput = document.getElementById('id101');
const ageInput = document.getElementById('id102');
const genderInput = document.getElementById('gender');
const predictionHeading = document.getElementById('heading2');
const submitButton = document.getElementById('id104');

// Attach a single submit event listener
form.addEventListener('submit', (event) => {
    // Prevent default submission for client-side validation
    const salary = salaryInput.value;
    const age = ageInput.value;

    if (salary <= 0 || age <= 0) {
        event.preventDefault(); // Prevent the form from being submitted
        alert("Please enter valid positive values for Age and Salary.");
        return; // Exit early
    }

    // If validation passes, show a processing message
    predictionHeading.textContent = "Processing...";
    submitButton.disabled = true; // Disable the button to prevent duplicate submissions
});

// Provide helpful hints when the salary input gains focus
salaryInput.addEventListener('focus', () => {
    predictionHeading.textContent = "Enter your salary in numbers.";
});

ageInput.addEventListener('focus', ()=> {
    predictionHeading.textContent="Enter your age in numbers. ";
})
