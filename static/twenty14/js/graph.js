function setupGraph() {
    var Graph = function() {
        var width = 800;
        var height = 400;
        var xAccessor = function(d) {
            return d.day;
        };

        var yAccessor = function(d) {
            return d.value;
        };

        var xMax = d3.max(data, xAccessor);
        var padding = 0.1;
        var barWidth = 10;
        var xTotalPadding = xMax * padding;
        var xScale = d3.scale.linear().domain([0, xMax * barWidth + (xTotalPadding)]).range([0, width]);
        var yScale = d3.scale.linear().domain([d3.max(data, yAccessor), 0]).range([height, 0]);

        var barTransform = function(d) {
            return "translate(" + (xScale(d.day * barWidth + padding)) + ", " + (height - yScale(d.value)) + ")";
        };

        var chart = d3.select("#history");
        chart.attr("width", width).attr("height", height);

        var bar = chart.selectAll("g")
                        .data(data)
                        .enter()
                        .append("g")
                        .attr("transform", barTransform);
        bar.append("rect").attr("width", function(d) { return xScale(barWidth); }).attr("height", function(d) { return yScale(yAccessor(d)); });
    };
    console.log("HI");
    new Graph();
}

$(document).ready(function() {
    console.log("Loading bar charts...");
    setupGraph();
});
