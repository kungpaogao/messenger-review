// https://bost.ocks.org/mike/bar/2/

data = [496, 286, 394];

// HTML bar chart
const scale = d3
  .scaleLinear()
  .domain([0, d3.max(data)])
  .range([0, 500]);

d3.select(".bar-html")
  .selectAll("div")
  .data(data)
  .enter()
  .append("div")
  .style("width", function(d) {
    return scale(d) + "px";
  })
  .text(function(d) {
    return d;
  });

// SVG bar chart
const width = 500,
  barHeight = 20;

const scaleSvg = d3
  .scaleLinear()
  .domain([0, d3.max(data)])
  .range([0, width]);

const barSvg = d3
  .select(".bar-svg")
  .attr("width", width)
  .attr("height", barHeight * data.length);

const bar = barSvg
  .selectAll("g")
  .data(data)
  .enter()
  .append("g")
  .attr("transform", function(d, i) {
    return "translate(0," + i * barHeight + ")";
  });

bar
  .append("rect")
  .attr("width", scaleSvg)
  .attr("height", barHeight - 1);

bar
  .append("text")
  .attr("x", function(d) {
    return scaleSvg(d) - 3;
  })
  .attr("y", barHeight / 2)
  .attr("dy", ".35em")
  .text(function(d) {
    return d;
  });

// using CSV data
// import "../../scripts/out/out0.csv";
const scaleCsv = d3.scaleLinear().range([0, width]);
const barCsv = d3.select(".bar-csv").attr("width", width);

d3.csv("proto.csv").then(function(data) {
  console.log(data);
  scaleCsv.domain([
    0,
    d3.max(data, function(d) {
      return d.count;
    })
  ]);

  barCsv.attr("height", barHeight * data.length);

  const bar = barCsv
    .selectAll("g")
    .data(data)
    .enter()
    .append("g")
    .attr("transform", function(d, i) {
      return "translate(0," + i * barHeight + ")";
    });

  bar
    .append("rect")
    .attr("width", function(d) {
      return scaleCsv(d.count);
    })
    .attr("height", barHeight - 1);

  bar
    .append("text")
    .attr("x", function(d) {
      return scaleCsv(d.count) - 3;
    })
    .attr("y", barHeight / 2)
    .attr("dy", ".35em")
    .text(function(d) {
      return d.count;
    });
});

function type(d) {
  d.value = +d.value; // coerce to number
  return d;
}
