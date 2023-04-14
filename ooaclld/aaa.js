/**
  * @param d3           - d3js object to interact with
  * @param id           - wrapper element id where you can create SVG or CANVAS
  * @param width        - area width
  * @param height       - area height
  * @param data         - data to work with (a result of an elastic search aggregation)
  * @param applyFilter  - a function to filter data (filterParams: Array<{ type: string, value: string }>, widgetFilters: Record<string, any> = {}) => void
  *                         applyFilter([{ type: 'markers', value: marker.id }])    - to apply a marker filter
  *                         applyFilter([{ type: 'markers', value: undefined }])    - to clear a marker filter
  *                         applyFilter([{ type: 'field', value: 'some_value' }])   - to apply a field filter
  *                         applyFilter([{ type: 'field', value: undefined }])      - to clear a field filter
  * @param extensions   - a map of extensions
  *                         topojson - added 2021.10.20
  *                         printJS
  * @param ctx          - context
  *                         docs - an array of document (the current page)
  *                         widgetFilter            - Record < string, any >
  *                         applyFilter             - (filterParams: Array<{ type: string, value: string }>, widgetFilters: Record<string, any> = {}) => void
  *                         updateDoc               - (id: string, field: string, value: any) => void
  *                         storeValue              - (field: string, value: any) => void
  *                         retrieveStoredValue     - (field: string) => any
  *                         retrieveFilterValue     - (field: string) => any
  *                         inputParams             - Record < string, any >
  */
const legendData = {};

const prepareData = (data) => {
    const result = [];
    let columns = {};
    for (let statBucket of data.WEEKLY_STATS.buckets) {

        const period = {
            week: ""
            //period_data = {} //TODO: sepparate data from week key
        };

        const { key_as_string, key, TRANSFER_TARGET, doc_count } = statBucket;
        console.log('Zendesk transfer target stack bar statBucket:', statBucket);
        console.log('Zendesk transfer target stack bar TRANSFER_TARGET.buckets:', TRANSFER_TARGET.buckets);
        period.week = key_as_string;

        period["Succès Voicebot"] = TRANSFER_TARGET.doc_count;

        console.log('Zendesk transfer target stack bar period:', period);
        result.push(period);

        var newResult = result.slice(-7);
        newResult.columns = Object.keys(newResult[0]);

    }
    return newResult;
};



const handler = (d3, id, inputWidth, inputHeight, inputData, applyFilter) => {
    /* data object is a result of your aggregation
    should you want to see its structure, do the following:
    - add console.log(data) statement
    - open the browser's console and run a test
    It'll be sufficient to understand what kind of data you're going to get
    though it is okay to use console.log statements during testing, please at least comment them out when in production
    */

    console.log("Zendesk transfer target stack bar inputData: ", inputData);

    const _data = prepareData(inputData);
    console.log("Zendesk transfer target stack bar _data: ", _data);

    d3.select(id).selectAll("*").remove();

    const margin = {
        top: 10,
        right: 45,
        bottom: 20,
        left: 40
    },
        width = inputWidth - margin.left - margin.right,
        height = inputHeight - margin.top - margin.bottom;

    // append the svg object to the body of the page
    const svg = d3
        .select(id)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom),
        g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

    /*
    var data =
    [
    {
    "week": "w01",
    "confirmed_self_served_calls": "12",
    "product_info_hangups": "1",
    "hangups_customer_not_calling_again": "13"
    },
    {
    "week": "w02",
    "confirmed_self_served_calls": "6",
    "product_info_hangups": "6",
    "hangups_customer_not_calling_again": "33"
    },
    {
    "week": "w03",
    "confirmed_self_served_calls": "11",
    "product_info_hangups": "28",
    "hangups_customer_not_calling_again": "12"
    },
    {
    "week": "w04",
    "confirmed_self_served_calls": "19",
    "product_info_hangups": "6",
    "hangups_customer_not_calling_again": "1"
    },
    ];

    data.columns = [
    "week",
    "confirmed_self_served_calls",
    "product_info_hangups",
    "hangups_customer_not_calling_again"
    ];
    */


    data = _data;

   const subgroups = data.columns.slice(1);
    //console.log('Zendesk transfer target stack bar subgroups.slice().reverse():', subgroups.slice().reverse());

    // List of groups = weeks
    const groups = data.map((d) => d.week);

    // Add X axis
    const x = d3.scaleBand().domain(groups).range([0, width]).padding([0.2]);
    svg
        .append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(d3.axisBottom(x).tickSizeOuter(0));

    // Add Y axis
    const y = d3.scaleLinear().domain([0, 20]).range([height, 0]);
    g.append("g").call(d3.axisLeft(y).tickFormat((d) => d + " %"));

    // color palette = one color per subgroup
  	//const colorPalette = ["#00437d", "#0055a0", "#0068c3", "#007be6", "#0a8dff", "#2d9dff", "#50adff", "#73beff", "#96ceff", "#b9deff", "#c7e5ff", "#e3f2ff", "#e98c38", "#F95355", "#FADE89", "#B0D894", "#4C6472"];
	const colorPalette = ["#e41a1c", "#377eb8", "#4daf4a", "#0F3579", "#59BC64", "#E6981C", "#EC5D1D", "#AF4114", "#A19568", "#3C5244", "#111C21", "#BD3546", "#463A2C"];//http://colormind.io/
    //const colorPalette = ["#845EC2", "#D65DB1", "#FF6F91", "#FF9671", "#FFC75F", "#F9F871", "#2C73D2", "#0081CF", "#0089BA", "#008E9B", "#008F7A", "#FBEAFF", "#C4FCEF"];//http://colormind.io/
    //console.log('Zendesk transfer target stack bar subgroups:', subgroups);
    const color = d3
        .scaleOrdinal()
        .domain(subgroups)
        .range(colorPalette);

    //console.log('Zendesk transfer target stack bar color:', color);

    //stack the data? --> stack per subgroup
    const stackedData = d3.stack().keys(subgroups)(data);
    console.log('Zendesk transfer target stack bar stackedData:', stackedData);

    // Show the bars
    /*let bars = svg
    .append("g")
    .selectAll("g")
    .data(stackedData, (d) => d);

    bars.join(
    (enter) => {
    // don't forget to return the enter selection after appending
    return enter
    .append("g")
    .attr("fill", (d) => color(d.key))
    .selectAll("rect")
    .data((d) => d)
    // don't forget to join 'rect'
    .join("rect")
    .attr("x", (d) => x(d.data.week))
    .attr("y", (d) => y(d[1]))
    .attr("height", (d) => y(d[0]) - y(d[1]))
    .attr("width", x.bandwidth());
    //.on("mouseover", mouseover)
    //.on("mousemove", mousemove)
    //.on("mouseleave", mouseleave);
    },
    (update) => update,
    (exit) => exit.remove()
    );*/

    var tooltip = d3.select(id)
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("position", "absolute")

    // Three function that change the tooltip when user hover / move / leave a cell
    var mouseover = function (d) {
        //console.log('Zendesk transfer target stack bar mouseover d:', d);
        var subgroupName = d3.select(this.parentNode).datum().key;

        //console.log('Zendesk transfer target stack bar mouseover parentNode datum:', d3.select(this.parentNode).datum());
        //console.log('Zendesk transfer target stack bar mouseover subgroupName:', subgroupName);
        //console.log('Zendesk transfer target stack bar mouseover d.target.__data__.data:', d.target.__data__.data);
        var subgroupValue = d.target.__data__.data[subgroupName]; //d.data[subgroupName];
        tooltip
            .html("subgroup: " + subgroupName + "<br>" + "Value: " + subgroupValue)
            .style("opacity", 1)
    }
    var mousemove = function (d) {
        tooltip
            .style("left", 50) //(d3.pointer(d)[0]+90) + "px") // It is important to put the +90: other wise the tooltip is exactly where the point is an it creates a weird effect
            .style("top", 50) //(d3.pointer(d)[1]) + "px")
    }
    var mouseleave = function (d) {
        tooltip
            .style("opacity", 0)
    }

    svg.append("g")
        .selectAll("g")
        // Enter in the stack data = loop key per key = group per group
        .data(stackedData)
        .enter().append("g")
        .attr("fill", function (d) { return color(d.key); })
        .selectAll("rect")
        // enter a second time = loop subgroup per subgroup to add all rectangles
        .data(function (d) { return d; })
        .enter().append("rect")
        .attr("x", function (d) { return x(d.data.week); })
        .attr("y", function (d) { return y(d[1]); })
        .attr("height", function (d) { return y(d[0]) - y(d[1]); })
        .attr("width", x.bandwidth())
        .attr("stroke", "grey")
        .on("mouseover", mouseover)
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave)

    var z = d3.scaleOrdinal()
        .range(colorPalette);

    let legend = g.append("g")
        .attr("font-family", "sans-serif")
        .attr("font-size", 10)
        .attr("text-anchor", "start")
        .selectAll("g")
        .data(subgroups.slice())
        .enter().append("g")
        .attr("transform", function (d, i) { return "translate(0," + i * 20 + ")"; });

    legend.append("rect")
        .attr("x", width - 19)
        .attr("width", 19)
        .attr("height", 19)
        .attr("fill", z);

    legend.append("text")
        .attr("x", width + 10)
        .attr("y", 9.5)
        .attr("dy", "0.32em")
        .text(function (d) {
            //console.log("Legend:", d);
            return legendData[d] || d;
        });

    //});
}