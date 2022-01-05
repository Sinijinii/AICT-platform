// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#FFFFFF';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}


var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['2017-09-17','2017-09-24','2017-10-01','2017-10-08','2017-10-15','2017-10-22','2017-10-29','2017-11-05','2017-11-12','2017-11-19','2017-11-26','2017-12-03','2017-12-10',
'2017-12-17','2017-12-24','2017-12-31','2018-01-07','2018-01-14','2018-01-21','2018-01-28','2018-02-04','2018-02-11','2018-02-18','2018-02-25','2018-03-04','2018-03-11','2018-03-18','2018-03-25',
'2018-04-01','2018-04-08','2018-04-15','2018-04-22','2018-04-29','2018-05-06','2018-05-13','2018-05-20','2018-05-27'],
    datasets: [{
      label: "생산량",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(78, 115, 223, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(78, 115, 223, 1)",
      pointBorderColor: "rgba(78, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: ['0.0', '0.0', '0.0', '0.0','0.0','0.0','0.0','0.0','3.6','5.66666666666667','7.0','6.66666666666667','6.33333333333333','5.5','5.0','0.0','0.0','0.0','4.0','5.0',
'4.83333333333333','5.416666666666665','6.0','7.0','7.6', '7.66666666666667','10.5','10.8333333333333','10.0','13.6','11.1666666666667','9.16666666666667','9.5','7.33333333333333','5.8',
'5.83333333333333','4.5'
],
    }],
  },
  options: {
    maintainAspectRatio: false,

    scales: {
      xAxes: [{

        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '$' + number_format(value);
          }
        },
        gridLines: {
          color: "rgb(0, 0, 0)",
          zeroLineColor: "rgb(0, 0, 0)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return number_format(tooltipItem.yLabel) + "℃";
        }
      }
    }
  }
});

//##########################################################################################################


var ctx = document.getElementById("myAreaChart2");
var myLineChart = new Chart(ctx, {
  data: {
      datasets: [{
      type: 'line',
      label: "생산량",
      data: ['0.0', '0.0', '0.0', '0.0','0.0','0.0','0.0','0.0','3.6','5.66666666666667','7.0','6.66666666666667','6.33333333333333','5.5','5.0','0.0','0.0','0.0','4.0','5.0',
      '4.83333333333333','5.416666666666665','6.0','7.0','7.6', '7.66666666666667','10.5','10.8333333333333','10.0','13.6','11.1666666666667','9.16666666666667','9.5','7.33333333333333','5.8',
      '5.83333333333333','4.5']
      }, {
      type: 'line',
      label: "생산량2",
      data: ['0.0', '0.0', '0.0', '0.0','0.0','0.0','0.0','0.0','3','5','7','0','0','0','5.5','5.0','0.0','0.0','0.0','4.0','5.0',
      '4','5','6.0','7.0','7.6', '7','10.5','0','10.0','13.6','11','9','9.5','7','5.8',
      '5','4.5'],
      }],
      labels: ['2017-09-17','2017-09-24','2017-10-01','2017-10-08','2017-10-15','2017-10-22','2017-10-29','2017-11-05','2017-11-12','2017-11-19','2017-11-26','2017-12-03','2017-12-10',
'2017-12-17','2017-12-24','2017-12-31','2018-01-07','2018-01-14','2018-01-21','2018-01-28','2018-02-04','2018-02-11','2018-02-18','2018-02-25','2018-03-04','2018-03-11','2018-03-18','2018-03-25',
'2018-04-01','2018-04-08','2018-04-15','2018-04-22','2018-04-29','2018-05-06','2018-05-13','2018-05-20','2018-05-27'],
},

  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },

        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return '$' + number_format(value);
          }
        },
        gridLines: {
          color: "rgb(0, 0, 0)",
          zeroLineColor: "rgb(0, 0, 0)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#000000",
      titleMarginBottom: 10,
      titleFontColor: '#000000',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return number_format(tooltipItem.yLabel) + "%";
        }
      }
    }
  }
});