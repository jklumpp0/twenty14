function setupGraph() {
    var Graph = function() {
        var width = parseInt(d3.select('body').style('width'), 10);
        var height = 400;

        var yAccessor = function(d) {
            return d.value;
        };

        var xMax = data.length;
        var padding = 1;
        var barWidth = 10;
        var xTotalPadding = xMax * padding;
        var xScale = d3.scale.linear().domain([0, xMax * barWidth + (xTotalPadding)]).range([0, width]);
        var yScale = d3.scale.linear().domain([d3.max(data, yAccessor), 0]).range([height, 0]);

        var barTransform = function(d) {
            return "translate(" + (xScale(d.day * barWidth + padding * d.day)) + ", " + (height - yScale(d.value)) + ")";
        };

        var barStart = function(d) {
            return "translate(" + (xScale(d.day * barWidth + padding * d.day)) + ", " + height + ")";
        };

        var chart = d3.select("#history");
        chart.attr("width", width).attr("height", height);

        var bar = chart.selectAll("g")
                        .data(data)
                        .enter()
                        .append("g")
                        .attr("transform", barStart);
        bar.transition()
            .duration(3000)
                        .attr("transform", barTransform);
        var rect = bar.append("rect").attr("width", xScale(barWidth))
                        .attr("height", function(d) { return yScale(yAccessor(d)); });
    };
    console.log("HI");
    new Graph();
}

$(document).ready(function() {
    console.log("Loading bar charts...");
    setupGraph();
});
