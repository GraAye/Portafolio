document.getElementById('distance-btn').addEventListener('click', () => {
    setupConverter('Distance', ['Meters', 'Kilometers', 'Miles', 'Yards']);
});

document.getElementById('weight-btn').addEventListener('click', () => {
    setupConverter('Weight', ['Grams', 'Kilograms', 'Pounds', 'Ounces']);
});

function setupConverter(type, units) {
    document.getElementById('converter-title').innerText = `Convert ${type}`;
    const unitFrom = document.getElementById('unit-from');
    const unitTo = document.getElementById('unit-to');
    unitFrom.innerHTML = '';
    unitTo.innerHTML = '';
    units.forEach(unit => {
        const optionFrom = document.createElement('option');
        optionFrom.value = unit;
        optionFrom.innerText = unit;
        unitFrom.appendChild(optionFrom);

        const optionTo = document.createElement('option');
        optionTo.value = unit;
        optionTo.innerText = unit;
        unitTo.appendChild(optionTo);
    });
    document.getElementById('converter').classList.remove('hidden');
}

document.getElementById('convert-btn').addEventListener('click', async () => {
    const value = parseFloat(document.getElementById('input-value').value);
    const fromUnit = document.getElementById('unit-from').value;
    const toUnit = document.getElementById('unit-to').value;

    const response = await fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            value: value,
            from_unit: fromUnit,
            to_unit: toUnit
        })
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('result').innerText = `Result: ${data.result} ${toUnit}`;
    } else {
        document.getElementById('result').innerText = 'Error converting units';
    }
});