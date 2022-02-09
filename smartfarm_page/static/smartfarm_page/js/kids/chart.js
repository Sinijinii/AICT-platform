function get_time_config(label, data_labels, data_values) {
    // configurations for the chart
    return {
        type: 'line',
        data: {
            labels: data_labels,
            datasets: [{
            label: 'counts',
            data: data_values,
            backgroundColor: Array(56).fill('rgba(255, 99, 132, 0.5)'),
            borderColor: Array(data_values.length).fill('rgba(255, 99, 132, 1)'),
            borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: label + ' tweet creation date'
            },
            legend: {
                display: false,
                position: 'top',
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            }
        }
    }
}


function convertDates(elementCreation) {
    // convert date object to Year and Month
    const hatevalTime = [];
    elementCreation.forEach(function (item, index) {
        var d = new Date(item);
        var l = new Date();
        l.setFullYear(d.getFullYear(), d.getMonth());
        hatevalTime.push(l);
    });

    // add counts to occurences of dates
    var counts = {};
    for (var i = 0; i < hatevalTime.length; i++) {
        var num = hatevalTime[i].toISOString().slice(0,7).replace(/-/g,"/");
        counts[num] = counts[num] ? counts[num] + 1 : 1;
    }

    // provide correct formatting
    var dataValues = [];
    for (var key of Object.keys(counts)) {
        dataValues.push({'t': key, 'y': counts[key]})
    }

    return [Object.keys(counts), dataValues]
}


function returnChart(label, creation) {
    // return the chart
    const creation_time = document.getElementById('time').getContext('2d');
    const [creationLabels, creationValues] = convertDates(creation);
    const creation_time_config = get_time_config(label, creationLabels, creationValues);
    const creationTime = new Chart(creation_time, creation_time_config);

    return creationTime
}


function showChart(creationTime) {
    // display the chart
    window.myLine = creationTime;
}