
const ctx = document.getElementById('myChart').getContext('2d');
let data = document.getElementById('info').innerText;
data = JSON.parse(data)
console.log(data)
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: data.map(x=>x.fecha), 
        datasets: [{
            label: 'UDIS 2 pesos',
            data: data.map(x => x.dato),
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx2 = document.getElementById('myDollarChart').getContext('2d');
let data2 = document.getElementById('DollarInfo').innerText;
console.log(data2)
data2 = JSON.parse(data2)
console.log(data2)

const myDollarChart = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: data2.map(x=>x.fecha), 
        datasets: [{
            label: 'MX/USD',
            data: data2.map(x => x.dato),
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});