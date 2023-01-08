
// Read the CSV file
fetch('./truck_data/fuel/truck1_fuel.csv')
  .then(response => response.text())
  .then((data) => {
    // Split the data into rows
    const rows = data.split('\n');

    // Split each row into cells
    const cells = rows.map(row => row.split(','));
    console.log(cells)
    floats = cells.map(cell => {
        if (parseFloat(cell[1]) > 500) {
            cell[1] = 500
        }
        return [parseFloat(cell[0]), parseFloat(cell[1])]
    })
    console.log(floats)
    a(floats);
  });
//     // Do something with the float data


//   // Create the chart
//   const ctx = document.getElementById('myChart').getContext('2d');
//   const chart = new Chart(ctx, {
//     type: 'scatter',
//     data: {
//       datasets: [{
//         label: 'Mean',
//         data: floats
//       }]
//     },
//     options: {
//       scales: {
//         xAxes: [{
//           type: 'linear',
//           position: 'bottom',
//           ticks: {
//             max: 143,
//             min:0
//         }
//         }],
//         yAxes: [{
//             ticks: {
//                 max: 200,
//                 min:0
//             }
//         }]
//       }
//     }
//   });
//   });


  
// console.log("script loaded")


let a = (async function(data) {

  new Chart(
    document.getElementById('acquisitions'),
    {
      type: 'bar',
      data: {
        labels: data.map(row => row[0]),
        datasets: [
          {
            label: 'Average fuel usage per truck trip',
            data: data.map(row => row[1]),
            backgroundColor: "blue"
          }
        ]
      }
    }
  );
});
