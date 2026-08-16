const translateBtn = document.getElementById("translateBtn");
const textInput = document.getElementById("text");
const languageInput = document.getElementById("language");
const resultBox = document.getElementById("result");

// Load supported languages into dropdown
async function loadLanguages() {
    try {
        const response = await fetch("/languages");

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();

        console.log("Languages API response:", data);

        // Clear dropdown
        languageInput.innerHTML =
            '<option value="">Select Language</option>';

        /*
         * Expected backend response:
         * {
         *   "english": "en",
         *   "tamil": "ta",
         *   "hindi": "hi"
         * }
         */

        let languages = data;

        // If backend returns { "languages": {...} }
        if (data.languages) {
            languages = data.languages;
        }

        // Convert object to array and sort alphabetically
        const languageList = Object.entries(languages).sort(
            ([nameA], [nameB]) =>
                nameA.localeCompare(nameB)
        );

        // Add languages
        languageList.forEach(([name, code]) => {
            const option = document.createElement("option");

            option.value = code;
            option.textContent =
                `${name.charAt(0).toUpperCase() + name.slice(1)} (${code})`;

            languageInput.appendChild(option);
        });

        console.log(
            `${languageList.length} languages loaded successfully.`
        );

    } catch (error) {
        console.error("Unable to load languages:", error);

        languageInput.innerHTML =
            '<option value="">Unable to load languages</option>';
    }
}

// Load languages when page opens
loadLanguages();


// Translate button
translateBtn.addEventListener("click", async () => {

    const text = textInput.value.trim();
    const targetLanguage = languageInput.value;

    // Clear previous result
    resultBox.textContent = "";

    // Validate text
    if (!text) {
        resultBox.textContent = "❌ Please enter text.";
        return;
    }

    // Validate language
    if (!targetLanguage) {
        resultBox.textContent =
            "❌ Please select a target language.";
        return;
    }

    // Loading message
    resultBox.textContent = "⏳ Translating...";

    try {

        const response = await fetch("/translate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                target_language: targetLanguage
            })
        });

        const data = await response.json();

        if (response.ok) {

            resultBox.textContent = data.translated_text;

        } else {

            resultBox.textContent =
                "❌ " + (data.detail || "Translation failed.");

        }

    } catch (error) {

        console.error("Translation error:", error);

        resultBox.textContent =
            "❌ Unable to connect to the translation service.";
    }

});