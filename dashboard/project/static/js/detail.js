var Chart = (function(){
    var configDefaultHighchart = {
        chart: {
            renderTo: 'pep8',
            spacingTop: 0,
            spacingRight: 0,
            spacingBottom: 0,
            spacingLeft: 0,
            type: 'spline',
            margin: [0, 0, 0, 0]
        },
        tooltip: {
            enabled: false
        },
        credits : {
            enabled: false
        },
        title: {
            text: ''
        },
        legend: {
            enabled: false
        },
        xAxis: {
            gridLineColor: 'transparent',
            gridLineWidth: 0,
            lineColor: 'transparent',
            tickLength: 0,
            labels: {
                enabled: false
            },
            categories: []
        },
        yAxis: {
            gridLineColor: 'transparent',
            gridLineWidth: 0,
            lineWidth: 0,
            lineColor: 'transparent',
            tickLength: 0,
            labels: {
                enabled: false
            },
            title: {
                text: null
            }
        },
        plotOptions: {
            spline: {
                color: '#fff',
                shadow: false,
                lineWidth: 8,
                dataLabels : {
                    style: {
                        fontSize: '1.6rem',
                        fontFamily: '"Roboto", "Helvetica Neue", Helvetica, Arial, sans-serif',
                        fontWeight: '500',
                        color: '#222'
                    },
                    enabled : true,
                    formatter : function() {
                        return '<span class="data-value">' + this.y + '</span>' + '<span class="data-range">' + this.x + '</span>';
                    },
                    useHTML: true
                },
                marker: {
                    radius: 20,
                    lineWidth: 3,
                    lineColor: '#323c41'
                }
            },
            areaspline: {
                shadow: false,
                lineWidth: 1,
                color: 'rgba(255,255,255,.5)',
                fillOpacity: 0.25,
                enableMouseTracking: false,
                marker: {
                    enabled: false
                }
            }
        },
        series: [{
            name: 'Errors',
            data: []
        }]
    };

    var generate = function(selectorChart, categories, series, type) {
        var configHighchart = $.extend({}, configDefaultHighchart);
        configHighchart.chart.renderTo = selectorChart;
        configHighchart.chart.type = type;
        configHighchart.xAxis.categories = categories;
        configHighchart.series = [{
            'data': series
        }];

        if(type === 'spline') {
            configHighchart.chart.height = $("#charts").height();
        }

        Highcharts.setOptions({
            chart: {
                backgroundColor: 'transparent',
                borderWidth: 0,
                plotBackgroundColor: 'transparent',
                plotShadow: false,
                plotBorderWidth: 0
            }
        });

        var chart = new Highcharts.Chart(configHighchart);

        $.each(chart.series[0].data, function(i, point) {
            point.dataLabel.attr({y: point.dataLabel.y + 43});
        });
    };

    return generate;
}());


$(document).ready(function() {

    var metrics = [
        {
            'urlHistory': 'history/pep8.json',
            'numberOfElements': 10,
            'chartSelector': 'pep8',
            'type': 'spline'
        },
        {
            'urlHistory': 'history/pep8.json',
            'numberOfElements': 10,
            'chartSelector': 'pep8-mini',
            'type': 'areaspline'
        }

        // ,
        // {
        //     'urlHistory': 'history/pep8.json',
        //     'numberOfElements': 5,
        //     'chartSelector': 'pep8-chart',
        //     'chartTitle': 'Lasts Analysis of Pep8',
        //     'dataTitle': 'Pep8 Errors',
        //     'lineColor': '#DB843D'
        // },
        // {
        //     'urlHistory': 'history/pyflakes.json',
        //     'numberOfElements': 5,
        //     'chartSelector': 'pyflakes-chart',
        //     'chartTitle': 'Lasts Analysis of PyFlakes',
        //     'dataTitle': 'PyFlakes Errors',
        //     'lineColor': '#A47D7C'
        // },
        // {
        //     'urlHistory': 'history/clonedigger.json',
        //     'numberOfElements': 5,
        //     'chartSelector': 'clonedigger-chart',
        //     'chartTitle': 'Lasts Analysis of CloneDigger',
        //     'dataTitle': 'CloneDigger Errors',
        //     'lineColor': '#80699B'
        // },
        // {
        //     'urlHistory': 'history/jshint.json',
        //     'numberOfElements': 5,
        //     'chartSelector': 'jshint-chart',
        //     'chartTitle': 'Lasts Analysis of JsHint',
        //     'dataTitle': 'JsHint Errors',
        //     'lineColor': '#89A54E'
        // },
        // {
        //     'urlHistory': 'history/csslint.json',
        //     'numberOfElements': 5,
        //     'chartSelector': 'csslint-chart',
        //     'chartTitle': 'Lasts Analysis of CssLint',
        //     'dataTitle': 'CssLint Errors',
        //     'lineColor': '#AA4643'
        // }
    ];

    $(window).resize(function() {
        chart.setSize($("#charts").width(), $("#charts").height(), false);
    });

    $.each(metrics, function(index, metric) {
        $.getJSON(metric.urlHistory, {'numberOfElements': metric.numberOfElements}, function(data) {
            Chart(metric.chartSelector, data.dates, data.metric_analysis, metric.type);
        });
    });
});