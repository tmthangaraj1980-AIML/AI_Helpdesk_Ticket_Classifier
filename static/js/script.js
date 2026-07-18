/*
=========================================================
AI Helpdesk Ticket Classifier
Frontend JavaScript
=========================================================
*/

document.addEventListener("DOMContentLoaded", () => {

    // ==============================
    // DOM Elements
    // ==============================

    const predictBtn = document.getElementById("predictBtn");
    const clearBtn = document.getElementById("clearBtn");
    const copyBtn = document.getElementById("copyBtn");

    const ticketInput = document.getElementById("ticket");

    const prediction = document.getElementById("prediction");
    const confidence = document.getElementById("confidence");

    const assignedTeam = document.getElementById("assignedTeam");
    const priority = document.getElementById("priority");
    const eta = document.getElementById("eta");

    const resolution = document.getElementById("resolution");

    const topPredictions = document.getElementById("topPredictions");

    // ==============================
    // Sample Tickets
    // ==============================

    document.querySelectorAll(".sampleTicket").forEach(button => {

        button.addEventListener("click", () => {

            ticketInput.value = button.innerText;

            ticketInput.focus();

        });

    });

    // ==============================
    // Clear Button
    // ==============================

    clearBtn.addEventListener("click", () => {

        ticketInput.value = "";

        prediction.innerHTML = "--";
        confidence.innerHTML = "--";

        assignedTeam.innerHTML = "--";
        priority.innerHTML = "--";
        eta.innerHTML = "--";

        resolution.innerHTML = `
            <li class="list-group-item">--</li>
        `;

        topPredictions.innerHTML = `
            <li class="list-group-item">--</li>
        `;

        ticketInput.focus();

    });

    // ==============================
    // Predict
    // ==============================

    predictBtn.addEventListener("click", async () => {

        const ticket = ticketInput.value.trim();

        if (ticket === "") {

            alert("Please enter a helpdesk ticket.");

            ticketInput.focus();

            return;

        }

        predictBtn.disabled = true;

        predictBtn.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2"></span>
            Classifying...
        `;

        prediction.innerHTML = "...";
        confidence.innerHTML = "...";

        try {

            const response = await fetch("/predict", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    ticket: ticket

                })

            });

            const data = await response.json();

            if (response.ok) {

                prediction.innerHTML = data.prediction;

                confidence.innerHTML =
                    data.confidence.toFixed(2) + "%";

                assignedTeam.innerHTML =
                    data.assigned_team;

                priority.innerHTML =
                    data.priority;

                eta.innerHTML =
                    data.eta;

                resolution.innerHTML = "";

                data.resolution.forEach(step => {

                    resolution.innerHTML += `
                        <li class="list-group-item">${step}</li>
                    `;

                });

                topPredictions.innerHTML = "";

                data.top_predictions.forEach(item => {

                    topPredictions.innerHTML += `
                        <li class="list-group-item d-flex justify-content-between">

                            <span>${item.category}</span>

                            <strong>${item.probability}%</strong>

                        </li>
                    `;

                });

            }

            else {

                prediction.innerHTML = data.error;

            }

        }

        catch (error) {

            console.error(error);

            prediction.innerHTML = "Server Error";

        }

        predictBtn.disabled = false;

        predictBtn.innerHTML = `
            <i class="bi bi-cpu"></i>
            Classify Ticket
        `;

    });

    // ==============================
    // Copy Solution
    // ==============================

    copyBtn.addEventListener("click", () => {

        let text = "";

        text += "Category : " + prediction.innerText + "\n\n";

        text += "Confidence : " + confidence.innerText + "\n\n";

        text += "Assigned Team : " + assignedTeam.innerText + "\n\n";

        text += "Priority : " + priority.innerText + "\n\n";

        text += "Estimated Resolution : " + eta.innerText + "\n\n";

        text += "Suggested Resolution\n";

        resolution.querySelectorAll("li").forEach(item => {

            text += "• " + item.innerText + "\n";

        });

        navigator.clipboard.writeText(text);

        alert("Solution copied successfully.");

    });

});