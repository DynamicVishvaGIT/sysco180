function getChartColorsArray(r) {
	r = $(r).attr("data-colors");
	return (r = JSON.parse(r)).map(function(r) {
		r = r.replace(" ", "");
		if (-1 == r.indexOf("--")) return r;
		r = getComputedStyle(document.documentElement).getPropertyValue(r);
		return r || void 0
	})
}
var minichart1Colors = getChartColorsArray("#mini-chart1"),
	options = {
		series: [{
			data: [2, 10, 18, 22, 36, 15, 47, 75, 65, 19, 14, 2, 47, 42, 15]
		}],
		chart: {
			type: "line",
			height: 50,
			sparkline: {
				enabled: !0
			}
		},
		colors: minichart1Colors,
		stroke: {
			curve: "smooth",
			width: 2
		},
		tooltip: {
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(r) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	},
	chart = new ApexCharts(document.querySelector("#mini-chart1"), options);
chart.render();
var minichart2Colors = getChartColorsArray("#mini-chart2"),
	options = {
		series: [{
			data: [15, 42, 47, 2, 14, 19, 65, 75, 47, 15, 42, 47, 2, 14, 12]
		}],
		chart: {
			type: "line",
			height: 50,
			sparkline: {
				enabled: !0
			}
		},
		colors: minichart2Colors,
		stroke: {
			curve: "smooth",
			width: 2
		},
		tooltip: {
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(r) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
(chart = new ApexCharts(document.querySelector("#mini-chart2"), options)).render();
var minichart3Colors = getChartColorsArray("#mini-chart3"),
	options = {
		series: [{
			data: [47, 15, 2, 67, 22, 20, 36, 60, 60, 30, 50, 11, 12, 3, 8]
		}],
		chart: {
			type: "line",
			height: 50,
			sparkline: {
				enabled: !0
			}
		},
		colors: minichart3Colors,
		stroke: {
			curve: "smooth",
			width: 2
		},
		tooltip: {
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(r) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};
(chart = new ApexCharts(document.querySelector("#mini-chart3"), options)).render();
var minichart4Colors = getChartColorsArray("#mini-chart4"),
	options = {
		series: [{
			data: [12, 14, 2, 47, 42, 15, 47, 75, 65, 19, 14, 2, 47, 42, 15]
		}],
		chart: {
			type: "line",
			height: 50,
			sparkline: {
				enabled: !0
			}
		},
		colors: minichart4Colors,
		stroke: {
			curve: "smooth",
			width: 2
		},
		tooltip: {
			fixed: {
				enabled: !1
			},
			x: {
				show: !1
			},
			y: {
				title: {
					formatter: function(r) {
						return ""
					}
				}
			},
			marker: {
				show: !1
			}
		}
	};



 // Color utility function
        function getChartColorsArray(elementId) {
            var colors = ["#28a745", "#007bff", "#17a2b8", "#ffc107", "#dc3545", "#6c757d", "#343a40", "#fd7e14", "#6f42c1", "#20c997"];
            return colors;
        }

        // First Pie Chart - Zone Wise
        var pieChart1Colors = getChartColorsArray("#pie-chart-1");
        var options1 = {
            series: [45, 30, 25, 20],
            chart: {
                width: 250,
                height: 250,
                type: "pie"
            },
            labels: ["East Zone", "West Zone", "South Zone", "North Zone"],
            colors: ["#28a745", "#007bff", "#17a2b8", "#ffc107"],
            stroke: {
                width: 0
            },
            legend: {
                show: false
            },
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    return Math.round(val) + "%"
                }
            },
            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    }
                }
            }]
        };

        // Second Pie Chart - State Wise
        var pieChart2Colors = getChartColorsArray("#pie-chart-2");
        var options2 = {
            series: [40, 35, 25, 10, 12, 30, 40, 65, 80, 70],
            chart: {
                width: 250,
                height: 250,
                type: "pie"
            },
            labels: ["Maharashtra", "Kerala", "Rajasthan", "Gujarat", "Tamil Nadu", "Himachal Pradesh", "Uttarakhand", "Uttar Pradesh", "Madhya Pradesh", "Delhi"],
            colors: ["#28a745", "#007bff", "#17a2b8", "#ffc107", "#dc3545", "#6c757d", "#343a40", "#fd7e14", "#6f42c1", "#20c997"],
            stroke: {
                width: 0
            },
            legend: {
                show: false
            },
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    return Math.round(val) + "%"
                }
            },
            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    }
                }
            }]
        };

        // Third Pie Chart - Product Wise
        var pieChart3Colors = getChartColorsArray("#pie-chart-3");
        var options3 = {
            series: [40, 35, 25, 25, 25],
            chart: {
                width: 250,
                height: 250,
                type: "pie"
            },
            labels: ["Entice", "Engalze", "Engem", "Tripper", "RCCB"],
            colors: ["#28a745", "#007bff", "#17a2b8", "#ffc107", "#dc3545"],
            stroke: {
                width: 0
            },
            legend: {
                show: false
            },
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    return Math.round(val) + "%"
                }
            },
            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 200
                    }
                }
            }]
        };

        // Render all three charts
        document.addEventListener('DOMContentLoaded', function() {
            // Chart 1
            var element1 = document.querySelector("#pie-chart-1");
            if (element1) {
                var chart1 = new ApexCharts(element1, options1);
                chart1.render().catch(function(error) {
                    console.error('Error rendering chart 1:', error);
                });
            } else {
                console.error('Element #pie-chart-1 not found');
            }

            // Chart 2
            var element2 = document.querySelector("#pie-chart-2");
            if (element2) {
                var chart2 = new ApexCharts(element2, options2);
                chart2.render().catch(function(error) {
                    console.error('Error rendering chart 2:', error);
                });
            } else {
                console.error('Element #pie-chart-2 not found');
            }

            // Chart 3
            var element3 = document.querySelector("#pie-chart-3");
            if (element3) {
                var chart3 = new ApexCharts(element3, options3);
                chart3.render().catch(function(error) {
                    console.error('Error rendering chart 3:', error);
                });
            } else {
                console.error('Element #pie-chart-3 not found');
            }
        });


    



(chart = new ApexCharts(document.querySelector("#invested-overview"), options)).render();
var barchartColors = getChartColorsArray("#market-overview"),
	options = {
		series: [{
			name: "Profit",
			data: [12.45, 16.2, 8.9, 11.42, 12.6, 18.1, 18.2, 14.16, 11.1, 8.09, 16.34, 12.88]
		}, {
			name: "Loss",
			data: [-11.45, -15.42, -7.9, -12.42, -12.6, -18.1, -18.2, -14.16, -11.1, -7.09, -15.34, -11.88]
		}],
		chart: {
			type: "bar",
			height: 400,
			stacked: !0,
			toolbar: {
				show: !1
			}
		},
		plotOptions: {
			bar: {
				columnWidth: "20%"
			}
		},
		colors: barchartColors,
		fill: {
			opacity: 1
		},
		dataLabels: {
			enabled: !1
		},
		legend: {
			show: !1
		},
		yaxis: {
			labels: {
				formatter: function(r) {
					return r.toFixed(0) + "%"
				}
			}
		},
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			labels: {
				rotate: -90
			}
		}
	};
(chart = new ApexCharts(document.querySelector("#market-overview"), options)).render();
var vectormapColors = getChartColorsArray("#sales-by-locations");
$("#sales-by-locations").vectorMap({
	map: "world_mill_en",
	normalizeFunction: "polynomial",
	hoverOpacity: .7,
	hoverColor: !1,
	regionStyle: {
		initial: {
			fill: "#e9e9ef"
		}
	},
	markerStyle: {
		initial: {
			r: 9,
			fill: vectormapColors,
			"fill-opacity": .9,
			stroke: "#fff",
			"stroke-width": 7,
			"stroke-opacity": .4
		},
		hover: {
			stroke: "#fff",
			"fill-opacity": 1,
			"stroke-width": 1.5
		}
	},
	backgroundColor: "transparent",
	markers: [{
		latLng: [41.9, 12.45],
		name: "USA"
	}, {
		latLng: [12.05, -61.75],
		name: "Russia"
	}, {
		latLng: [1.3, 103.8],
		name: "Australia"
	}]
});

(chart = new ApexCharts(document.querySelector("#column_chart_datalabel"), options)).render();
var barColors = getChartColorsArray("#activebar_chart"),
	options = {
		chart: {
			height: 350,
			type: "bar",
			toolbar: {
				show: !1
			}
		},
		plotOptions: {
			bar: {
				horizontal: !0
			}
		},
		dataLabels: {
			enabled: !1
		},
		series: [{
			data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
		}],
		colors: barColors,
		grid: {
			borderColor: "#f1f1f1"
		},
		xaxis: {
			categories: ["Maharashtra", "Kerla", "Rajastan", "Utter Pradesh", "Madhya Pradesh", "Tamil nadu", "Panjab", "Delhi", "Kolkata", "Himchal Pradesh"],
		}
	};
(chart = new ApexCharts(document.querySelector("#activebar_chart"), options)).render();
var mixedColors = getChartColorsArray("#mixed_chart"),
	options = {
		chart: {
			height: 350,
			type: "line",
			stacked: !1,
			toolbar: {
				show: !1
			}
		},
		stroke: {
			width: [0, 2, 4],
			curve: "smooth"
		},
		plotOptions: {
			bar: {
				columnWidth: "50%"
			}
		},
		colors: mixedColors,
		series: [{
			name: "Team A",
			type: "column",
			data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30]
		}, {
			name: "Team B",
			type: "area",
			data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43]
		}, {
			name: "Team C",
			type: "line",
			data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39]
		}],
		fill: {
			opacity: [.85, .25, 1],
			gradient: {
				inverseColors: !1,
				shade: "light",
				type: "vertical",
				opacityFrom: .85,
				opacityTo: .55,
				stops: [0, 100, 100, 100]
			}
		},
		labels: ["01/01/2003", "02/01/2003", "03/01/2003", "04/01/2003", "05/01/2003", "06/01/2003", "07/01/2003", "08/01/2003", "09/01/2003", "10/01/2003", "11/01/2003"],
		markers: {
			size: 0
		},
		xaxis: {
			type: "datetime"
		},
		yaxis: {
			title: {
				text: "Points"
			}
		},
		tooltip: {
			shared: !0,
			intersect: !1,
			y: {
				formatter: function(e) {
					return void 0 !== e ? e.toFixed(0) + " points" : e
				}
			}
		},
		grid: {
			borderColor: "#f1f1f1"
		}
	};


    


    function getChartColorsArray(selector) {
            // Sample colors array; replace or modify as needed
            return ['#556ee6', '#34c38f', '#f46a6a', '#f1b44c', '#50a5f1', '#e83e8c', '#6f42c1', '#343a40', '#f8f9fa', '#5bc0de'];
        }

        const separateBarColors = getChartColorsArray("#separate_bar_chart");

        const separateBarChartOptions = {
            chart: {
                height: 350,
                type: "bar",
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: "Population",
                data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
            }],
            colors: separateBarColors,
            grid: {
                borderColor: "#f1f1f1"
            },
            xaxis: {
                categories: [
                    "Maharashtra", "Kerala", "Rajasthan", "Uttar Pradesh",
                    "Madhya Pradesh", "Tamil Nadu", "Punjab",
                    "Delhi", "Kolkata", "Himachal Pradesh"
                ]
            }
        };
        new ApexCharts(document.querySelector("#separate_bar_chart"), separateBarChartOptions).render();


         function getSecondChartColorsArray(selector) {
            // Custom color set for second chart
            return ['#ff6b6b', '#6bc5ff', '#ffd93d', '#6effbf', '#d3a4ff', '#ffa07a', '#90ee90', '#add8e6', '#ffb6c1', '#87ceeb'];
        }

        const secondBarColors = getSecondChartColorsArray("#active_electrician_bar_chart");

        const secondBarChartOptions = {
            chart: {
                height: 350,
                type: "bar",
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: "Population",
                data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
            }],
            colors: secondBarColors,
            grid: {
                borderColor: "#f1f1f1"
            },
            xaxis: {
                categories: [
                    "Maharashtra", "Kerala", "Rajasthan", "Uttar Pradesh",
                    "Madhya Pradesh", "Tamil Nadu", "Punjab",
                    "Delhi", "Kolkata", "Himachal Pradesh"
                ]
            }
        };

        new ApexCharts(document.querySelector("#active_electrician_bar_chart"), secondBarChartOptions).render();




  // Third Bar Chart Colors and Configuration
        function getThirdChartColorsArray(selector) {
            // Custom color set for bar chart
            return ['#3fe2ff', '#6bc5ff', '#ffd93d', '#6effbf', '#d3a4ff', '#ffa07a', '#90ee90', '#add8e6', '#ffb6c1', '#87ceeb'];
        }

        const thirdBarColors = getThirdChartColorsArray("#third_bar_chart");

        const thirdBarChartOptions = {
            chart: {
                height: 350,
                type: "bar",
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: "Population",
                data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
            }],
            colors: thirdBarColors,
            grid: {
                borderColor: "#f1f1f1"
            },
            xaxis: {
                categories: [
                    "Maharashtra", "Kerala", "Rajasthan", "Uttar Pradesh",
                    "Madhya Pradesh", "Tamil Nadu", "Punjab",
                    "Delhi", "Kolkata", "Himachal Pradesh"
                ]
            }
        };

        // Render bar chart
        document.addEventListener('DOMContentLoaded', function() {
            var barElement = document.querySelector("#third_bar_chart");
            if (barElement) {
                new ApexCharts(barElement, thirdBarChartOptions).render().catch(function(error) {
                    console.error('Error rendering bar chart:', error);
                });
            } else {
                console.error('Element #third_bar_chart not found');
            }
        });


    
// Function to get chart colors from data attribute
        function getChartColorsArray(elementId) {
            const element = document.querySelector(elementId);
            if (element) {
                const colors = element.getAttribute('data-colors');
                if (colors) {
                    return JSON.parse(colors);
                }
            }
            return ["#2ab57d", "#5156be", "#fd625e"]; // Default colors
        }

        // Get colors for the column chart
        var columnColors = getChartColorsArray("#column_chart");

        // Chart options
        var options = {
            chart: {
                height: 350,
                type: "bar",
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: "45%",
                    endingShape: "rounded"
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                show: true,
                width: 2,
                colors: ["transparent"]
            },
            series: [{
                name: "Net Profit",
                data: [46, 57, 59, 54, 62, 58, 64, 60, 66]
            }, {
                name: "Revenue", 
                data: [74, 83, 102, 97, 86, 106, 93, 114, 94]
            }, {
                name: "Free Cash Flow",
                data: [37, 42, 38, 26, 47, 50, 54, 55, 43]
            }],
            colors: columnColors,
            xaxis: {
                categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
                title: {
                    text: "Months",
                    style: {
                        fontWeight: "500"
                    }
                }
            },
            yaxis: {
                title: {
                    text: "$ (thousands)",
                    style: {
                        fontWeight: "500"
                    }
                }
            },
            grid: {
                borderColor: "#f1f1f1"
            },
            fill: {
                opacity: 1
            },
            tooltip: {
                y: {
                    formatter: function(value) {
                        return "$ " + value + " thousands";
                    }
                }
            },
            legend: {
                position: 'top',
                horizontalAlign: 'center'
            }
        };

        // Create and render the chart
        var chart = new ApexCharts(document.querySelector("#column_chart"), options);
        chart.render();




        // four Bar Chart Colors and Configuration
        function getfourChartColorsArray(selector) {
            // Custom color set for bar chart
            return ['#3fe2ff', '#6bc5ff', '#ffd93d', '#6effbf', '#d3a4ff', '#ffa07a', '#90ee90', '#add8e6', '#ffb6c1', '#87ceeb'];
        }

        const fourBarColors = getfourChartColorsArray("#four_bar_chart");

        const fourBarChartOptions = {
            chart: {
                height: 350,
                type: "bar",
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: "Population",
                data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
            }],
            colors: thirdBarColors,
            grid: {
                borderColor: "#f1f1f1"
            },
            xaxis: {
                categories: [
                    "Maharashtra", "Kerala", "Rajasthan", "Uttar Pradesh",
                    "Madhya Pradesh", "Tamil Nadu", "Punjab",
                    "Delhi", "Kolkata", "Himachal Pradesh"
                ]
            }
        };

        // Render bar chart
        document.addEventListener('DOMContentLoaded', function() {
            var barElement = document.querySelector("#four_bar_chart");
            if (barElement) {
                new ApexCharts(barElement, fourBarChartOptions).render().catch(function(error) {
                    console.error('Error rendering bar chart:', error);
                });
            } else {
                console.error('Element #four_bar_chart not found');
            }
        });



                // five Bar Chart Colors and Configuration
        function getfiveChartColorsArray(selector) {
            // Custom color set for bar chart
            return ['#d3a4ff', '#6bc5ff', '#ffd93d', '#6effbf', '#d3a4ff', '#ffa07a', '#90ee90', '#add8e6', '#ffb6c1', '#87ceeb'];
        }

        const fiveBarColors = getfiveChartColorsArray("#five_bar_chart");

        const fiveBarChartOptions = {
            chart: {
                height: 350,
                type: "bar",
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: "Population",
                data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
            }],
            colors: thirdBarColors,
            grid: {
                borderColor: "#f1f1f1"
            },
            xaxis: {
                categories: [
                    "Maharashtra", "Kerala", "Rajasthan", "Uttar Pradesh",
                    "Madhya Pradesh", "Tamil Nadu", "Punjab",
                    "Delhi", "Kolkata", "Himachal Pradesh"
                ]
            }
        };

        // Render bar chart
        document.addEventListener('DOMContentLoaded', function() {
            var barElement = document.querySelector("#five_bar_chart");
            if (barElement) {
                new ApexCharts(barElement, fiveBarChartOptions).render().catch(function(error) {
                    console.error('Error rendering bar chart:', error);
                });
            } else {
                console.error('Element #five_bar_chart not found');
            }
        });


    // Six Bar Chart Colors and Configuration
        function getsixChartColorsArray(selector) {
            // Custom color set for bar chart
            return ['#ffa07a', '#6bc5ff', '#ffd93d', '#6effbf', '#d3a4ff', '#ffa07a', '#90ee90', '#add8e6', '#ffb6c1', '#87ceeb'];
        }

        const sixBarColors = getsixChartColorsArray("#six_bar_chart");

        const sixBarChartOptions = {
            chart: {
                height: 350,
                type: "bar",
                toolbar: {
                    show: false
                }
            },
            plotOptions: {
                bar: {
                    horizontal: true
                }
            },
            dataLabels: {
                enabled: false
            },
            series: [{
                name: "Population",
                data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365]
            }],
            colors: thirdBarColors,
            grid: {
                borderColor: "#f1f1f1"
            },
            xaxis: {
                categories: [
                    "Maharashtra", "Kerala", "Rajasthan", "Uttar Pradesh",
                    "Madhya Pradesh", "Tamil Nadu", "Punjab",
                    "Delhi", "Kolkata", "Himachal Pradesh"
                ]
            }
        };

        // Render bar chart
        document.addEventListener('DOMContentLoaded', function() {
            var barElement = document.querySelector("#six_bar_chart");
            if (barElement) {
                new ApexCharts(barElement, sixBarChartOptions).render().catch(function(error) {
                    console.error('Error rendering bar chart:', error);
                });
            } else {
                console.error('Element #six_bar_chart not found');
            }
        });