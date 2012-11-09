var Chart = (function(){
    var configDefaultHighchart = {
        chart: {
            renderTo: 'pep8-chart',
            type: 'line',
            backgroundColor: '#f5f5f5',
            marginRight: 130,
            marginBottom: 25
        },
        credits : {
            enabled: false
        },
        colors: ['#DB843D'],
        title: {
            text: 'Lasts Analysis of Pep8',
            x: -20 //center
        },
        xAxis: {
            categories: []
        },
        yAxis: {
            title: {
                text: ''
            },
            gridLineColor: '#f5f5f5',
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            formatter: function() {
                    return '<b>'+ this.series.name +'</b><br/>'+
                    this.x +': '+ this.y +' errors';
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -10,
            y: 100,
            borderWidth: 0
        },
        series: [{
            name: 'Pep8 Errors',
            data: []
        }]
    };

    var generate = function(selectorChart, categories, series, title, lineTitle, lineColor) {
        var colors = [];
        colors.push(lineColor);

        var configHighchart = $.extend({}, configDefaultHighchart);
        configHighchart.chart.renderTo = selectorChart;
        configHighchart.colors = colors;
        configHighchart.title.text = title;
        configHighchart.xAxis.categories = categories;
        configHighchart.yAxis.title.text = lineTitle;
        configHighchart.series = [{
            'name': lineTitle,
            'data': series
        }];

        var chart = new Highcharts.Chart(configHighchart);
    };

    return generate;
}());


$(document).ready(function() {
    var metrics = [
        {
            'urlHistory': 'history/pep8.json',
            'numberOfElements': 10,
            'chartSelector': 'total-chart',
            'chartTitle': 'Lasts Analysis of Total Quality',
            'dataTitle': 'Total Average Quality',
            'lineColor': '#4572A7'
        },
        {
            'urlHistory': 'history/pep8.json',
            'numberOfElements': 5,
            'chartSelector': 'pep8-chart',
            'chartTitle': 'Lasts Analysis of Pep8',
            'dataTitle': 'Pep8 Errors',
            'lineColor': '#DB843D'
        },
        {
            'urlHistory': 'history/pyflakes.json',
            'numberOfElements': 5,
            'chartSelector': 'pyflakes-chart',
            'chartTitle': 'Lasts Analysis of PyFlakes',
            'dataTitle': 'PyFlakes Errors',
            'lineColor': '#A47D7C'
        },
        {
            'urlHistory': 'history/clonedigger.json',
            'numberOfElements': 5,
            'chartSelector': 'clonedigger-chart',
            'chartTitle': 'Lasts Analysis of CloneDigger',
            'dataTitle': 'CloneDigger Errors',
            'lineColor': '#80699B'
        },
        {
            'urlHistory': 'history/jshint.json',
            'numberOfElements': 5,
            'chartSelector': 'jshint-chart',
            'chartTitle': 'Lasts Analysis of JsHint',
            'dataTitle': 'JsHint Errors',
            'lineColor': '#89A54E'
        },
        {
            'urlHistory': 'history/csslint.json',
            'numberOfElements': 5,
            'chartSelector': 'csslint-chart',
            'chartTitle': 'Lasts Analysis of CssLint',
            'dataTitle': 'CssLint Errors',
            'lineColor': '#AA4643'
        }
    ];

    $.each(metrics, function(index, metric) {
        $.getJSON(metric.urlHistory, {'numberOfElements': metric.numberOfElements} ,function(data) {
            Chart(metric.chartSelector, data.dates, data.metric_analysis, metric.chartTitle, metric.dataTitle, metric.lineColor);
        });
    });
});