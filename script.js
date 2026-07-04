async function checkURL() {
    const url = document.getElementById("url").value;
    const resultDiv = document.getElementById("result");

    if (!url) {
        resultDiv.innerHTML = "Please enter a URL.";
        return;
    }

    resultDiv.innerHTML = "Checking...";

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });

        const data = await response.json();

        if (data.is_phishing === 1) {
            resultDiv.innerHTML = "<span style='color:red;'>⚠ Phishing URL!</span>";
        } else {
            resultDiv.innerHTML = "<span style='color:green;'>✔ Legitimate URL</span>";
        }

    } catch (error) {
        resultDiv.innerHTML = "Server Error!";
    }
}


