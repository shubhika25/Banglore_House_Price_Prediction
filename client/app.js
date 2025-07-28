document.getElementById('price-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const location = document.getElementById('location').value.trim();
    const total_sqft = document.getElementById('sqft').value;
    const bhk = document.getElementById('bhk').value;
    const bath = document.getElementById('bath').value;

    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    resultDiv.textContent = '';
    errorDiv.textContent = '';

    if (!location || !total_sqft || !bhk || !bath) {
        errorDiv.textContent = 'Please fill all fields correctly.';
        return;
    }

    const payload = { location, total_sqft, bhk, bath };

    try {
        const res = await fetch('/predict_home_price', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });

        const data = await res.json();

        if (res.ok) {
            resultDiv.textContent = `Estimated Price: ₹${data.estimated_price} Lakhs`;
        } else {
            errorDiv.textContent = data.error || 'Prediction failed.';
        }
    } catch (err) {
        errorDiv.textContent = 'Error connecting to server.';
    }
});
