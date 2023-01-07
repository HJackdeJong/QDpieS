// Read the CSV file
fetch('tripFuelCons.csv')
  .then(response => response.text())
  .then((data) => {
    // Split the data into rows
    const rows = data.split('\n');
    console.table(rows)

    // Split each row into cells
    const cells = rows.map(row => row.split(','));

    // Convert the cell data to floats
    const floats = cells.map(cell => parseFloat(cell[1]));

    // Do something with the float data
    console.table(floats);


  // Create the chart
  const ctx = document.getElementById('myChart').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'scatter',
    data: {
      datasets: [{
        label: 'Mean',
        data: floats
      }]
    },
    options: {
      scales: {
        xAxes: [{
          type: 'linear',
          position: 'bottom'
        }]
      }
    }
  });
  });


  
console.log("script loaded")