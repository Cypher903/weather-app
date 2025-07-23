// Get data from HTML (assuming you have elements or data attributes with city names and temps)
const cities = JSON.parse(document.getElementById('cities-data').textContent);
const temps = JSON.parse(document.getElementById('temps-data').textContent);

const ctx = document.getElementById('myChart').getContext('2d');

const myChart = new Chart(ctx, {
    type: 'bar', // other options: 'bar', 'pie', 'doughnut', etc.
    data: {
        labels: cities, // x-axis labels
        datasets: [{
            label: "Temperature (°C)",
            data: temps, // y-axis values
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true,
            tension: 0.4
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
