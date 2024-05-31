window.addEventListener('load', function() {
    var table = document.getElementById('table');
    var carbs = 0, protein = 0, fats = 0, calories = 0;

    for (var i = 1; i < table.rows.length - 1; i++) {
        carbs += parseFloat(table.rows[i].cells[1].innerHTML);
        protein += parseFloat(table.rows[i].cells[2].innerHTML);
        fats += parseFloat(table.rows[i].cells[3].innerHTML);
        calories += parseFloat(table.rows[i].cells[4].innerHTML);
    }

    carbs = Math.round(carbs);
    protein = Math.round(protein);
    fats = Math.round(fats);
    calories = Math.round(calories);

    document.getElementById('totalCarbs').innerHTML = '<b>' + carbs + '(gm)<b>';
    document.getElementById('totalProtein').innerHTML = '<b>' + protein + '(gm)<b>';
    document.getElementById('totalFats').innerHTML = '<b>' + fats + '(gm)<b>';
    document.getElementById('totalCalories').innerHTML = '<b>' + calories + '(kcal)<b>';

    //for creating a calorie progress bar, based on total calorie and find percentage of it.
    var caloriesPercentage = (calories / 2000) * 100;
    document.getElementsByClassName('progress-bar')[0].setAttribute('style', 'width:' + caloriesPercentage + "%");

    // convert all the total and get percentage for chart.
    var total = carbs + protein + fats;
    var carbsPercentage = Math.round((carbs / total) * 100)
    var protienPercentage = Math.round((protein / total) * 100)
    var fatsPercentage =Math.round((fats / total) * 100)


    var ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            // labels: ['Carbs' + carbsPercentage + '%', 'Protein', 'Fats'],
            labels: ['Carbohydrate', 'Protein', 'Fats'],

            datasets: [{
                label: 'Macro-Nutrients Breakdown',
                data: [carbsPercentage, protienPercentage, fatsPercentage],
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false,
            tooltips: {
                enabled: false
            }
        }
    });
});
