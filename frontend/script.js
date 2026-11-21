// FastAPI backend URL
const API_URL = "https://fuzzy-happiness-wv74j4v5qx5vhg79w-8000.app.github.dev/predict";
// Get HTML form
const jobForm = document.getElementById("jobForm");
const resultDiv = document.getElementById("result");

// Form submit event
jobForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    resultDiv.className = "";
    resultDiv.innerText = "Analyzing job posting... Please wait.";

    // Collect form data
    const jobData = {
        title: document.getElementById("title").value,
        company_profile: document.getElementById("company_profile").value,
        description: document.getElementById("description").value,
        requirements: document.getElementById("requirements").value,
        benefits: document.getElementById("benefits").value,

        employment_type: document.getElementById("employment_type").value,
        required_experience: document.getElementById("required_experience").value,
        required_education: document.getElementById("required_education").value,

        industry: document.getElementById("industry").value,
        function: document.getElementById("function").value,
        location: document.getElementById("location").value,

        telecommuting: Number(document.getElementById("telecommuting").value),
        has_company_logo: Number(document.getElementById("has_company_logo").value),
        has_questions: Number(document.getElementById("has_questions").value)
    };

    try {

        // Send request to FastAPI
        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(jobData)
        });

        // Check response
        if (!response.ok) {
            throw new Error("API request failed: " + response.status);
        }

        // Get prediction
        const data = await response.json();

        // Display result
        if (data.prediction === 1) {

            resultDiv.className = "danger";
            resultDiv.innerText = "⚠️ Fake Job Posting Detected!";

        } else {

            resultDiv.className = "success";
            resultDiv.innerText = "✅ This appears to be a Real Job Posting.";

        }

    } catch (error) {

        resultDiv.className = "error";
        resultDiv.innerText = "Error: " + error.message;

        console.error(error);

    }

});

