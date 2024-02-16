// async function fetchSymbols() {
//     try {
//         const response = await fetch(`http://127.0.0.1:8000/getsymbols?exchange=${document.getElementById("exchangeSelect").value}`);
//         const data = await response.json();
//         const symbolList = document.getElementById("symbolList");
//         symbolList.innerHTML = ''; // Clear existing symbols
//         data.forEach(symbol => {
//             const li = document.createElement("li");
//             li.textContent = symbol.symbol + ": " + symbol.last_price;
//             symbolList.appendChild(li);
//         });
//     } catch (error) {
//         console.error('Error fetching symbols:', error);
//     }
// }

// // Fetch symbols for the selected exchange when the page loads
// window.onload = fetchSymbols;

// // Handle form submission
// document.getElementById("priceForm").addEventListener("submit", async (event) => {
//     event.preventDefault(); // Prevent default form submission
//     const symbol = document.getElementById("symbol").value; // Get symbol value from input field
//     try {
//         const response = await fetch(`http://127.0.0.1:8000/getprice?symbol=${symbol}&exchange=${document.getElementById("exchangeSelect").value}`,
//             {method:'POST'}
//         );
//         const data = await response.json(); // Parse JSON response
//         document.getElementById("priceResult").innerHTML = `
//             <p><strong>Symbol:</strong> ${data.symbol}</p>
//             <p><strong>Last Price:</strong> ${data.last_price}</p>
//         `;
//     } catch (error) {
//         console.error('Error fetching price:', error);
//     }
// });

// // Update symbols when the exchange selection changes
// document.getElementById("exchangeSelect").addEventListener("change", fetchSymbols);


// Fetch all symbols for the selected exchange when the page loads
async function fetchSymbols() {
    try {
        const response = await fetch(`http://127.0.0.1:8000/getsymbols/${document.getElementById("exchangeSelect").value}`);
        const data = await response.json();
        const symbolList = document.getElementById("symbolList");
        symbolList.innerHTML = ''; // Clear existing symbols
        data.forEach(symbol => {
            const li = document.createElement("li");
            li.textContent = symbol.symbol + ": " + symbol.last_price;
            symbolList.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching symbols:', error);
    }
}

// Fetch symbols for the selected exchange when the page loads
window.onload = fetchSymbols;
async function fetchExchanges() {
    try {
        const response = await fetch(`http://127.0.0.1:8000/getexchanges`);
        const data = await response.json();
        const exchangeList = document.getElementById("exchangeSelect");
        exchangeList.innerHTML = ''; // Clear existing symbols
        data.forEach(exchange => {
            const option = document.createElement("option");
            option.value = exchange;
            option.innerText = exchange.toUpperCase();
            exchangeList.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching symbols:', error);
    }
}

// Fetch symbols for the selected exchange when the page loads
window.onload = fetchExchanges;

// Handle form submission
document.getElementById("priceForm").addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission
    const selectedSymbol = document.getElementById("symbol").value; // Get symbol value from input field
    const selectedExchange = document.getElementById("exchangeSelect").value.toLowerCase() // Get Exchange value from input field
    let payload = {
        symbol: selectedSymbol,
        exchange: selectedExchange
    }
    try {
        const response = await fetch(`http://127.0.0.1:8000/getprice`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
            body: JSON.stringify(payload)
        });
        const data = await response.json(); // Parse JSON response
        document.getElementById("priceResult").innerHTML = `
            <p><strong>Symbol:</strong> ${data.symbol}</p>
            <p><strong>Last Price:</strong> ${data.last_price}</p>
        `;
    } catch (error) {
        console.error('Error fetching price:', error);
    }
});

// Update symbols when the exchange selection changes
document.getElementById("exchangeSelect").addEventListener("change", fetchSymbols);

















// // Fetch all symbols when the page loads
// async function fetchSymbols() {
//     try {
//         const response = await fetch("http://127.0.0.1:8000/getsymbols");
//         const data = await response.json();
//         const symbolList = document.getElementById("symbolList");
//         symbolList.innerHTML = ''; // Clear existing symbols
//         data.forEach(symbol => {
//             const li = document.createElement("li");
//             li.textContent = symbol.symbol + ": " + symbol.last_price;
//             symbolList.appendChild(li);
//         });
//     } catch (error) {
//         console.error('Error fetching symbols:', error);
//     }
// }

// // Fetch symbols when the page loads
// window.onload = fetchSymbols;

// // Handle form submission
// document.getElementById("priceForm").addEventListener("submit", async (event) => {
//     event.preventDefault(); // Prevent default form submission
//     const symbol = document.getElementById("symbol").value; // Get symbol value from input field
//     try {
//         const response = await fetch(`http://127.0.0.1:8000/getprice?symbol=${symbol}`,
//             {method:'POST'}
//         );
//         console.log(response)
//         const data = await response.json(); // Parse JSON response
//         document.getElementById("priceResult").innerHTML = `
//             <p><strong>Symbol:</strong> ${data.symbol}</p>
//             <p><strong>Last Price:</strong> ${data.last_price}</p>
//         `;
//     } catch (error) {
//         console.error('Error fetching price:', error);
//     }
// });
