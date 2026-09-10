console.log("JavaScript is running");

async function loadTours() {
    console.log("loadTours is running");

    try {
        const response = await fetch("http://127.0.0.1:8000/api/tours");

        console.log("Response received:", response);

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        console.log("Data received:", data);

        const container = document.getElementById("tours-container");

        if (!container) {
            console.log("No tours-container found on this page.");
            return;
        }

        container.innerHTML = "";

        data.tours.forEach((tour) => {
            const tourElement = document.createElement("div");

            tourElement.innerHTML = `
                <h3>${tour.name}</h3>
                <p>${tour.duration}</p>
                <p>₹${tour.price}</p>
            `;

            container.appendChild(tourElement);
        });
    } catch (error) {
        console.error("Failed to load tours:", error);
    }
}

async function loadDestinations() {
    console.log("loadDestinations is running");

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/api/destinations"
        );

        console.log("Destination response:", response);

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        console.log("Destination data:", data);

        const container = document.getElementById("destinations-container");

        if (!container) {
            console.log("No destinations-container found on this page.");
            return;
        }

        container.innerHTML = "";

        data.destinations.forEach((destination, index) => {
            const destinationElement = document.createElement("article");
            destinationElement.className = "destination-card";

            destinationElement.innerHTML = `
                <div class="destination-image">
                    <img
                        src="${destination.image}"
                        alt="${destination.name}"
                    >
                </div>

                <div class="destination-content">
                    <span class="destination-number">
                        ${String(index + 1).padStart(2, "0")}
                    </span>

                    <h3>${destination.name}</h3>
                    <p>${destination.description}</p>
                    <p>${destination.country}</p>
                    <p>${destination.duration}</p>
                    <p>₹${destination.price}</p>

                    <a href="${destination.link}">
                        Explore ${destination.name} &rarr;
                    </a>
                </div>
            `;

            container.appendChild(destinationElement);
        });
    } catch (error) {
        console.error("Failed to load destinations:", error);
    }
}

loadTours();
loadDestinations();
