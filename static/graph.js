const graph = document.getElementById("display_graph");
const ctx = graph.getContext("2d");
let rawData = graph.dataset.points;
console.log(rawData);
let parsedData = JSON.parse(rawData);
console.log(parsedData.cropBase);

let data = {
    labels: ["Crops", "Wines", "Preserves"],
    datasets: [
      {
      label: "Base Values",
      borderColor: 'rgb(255, 99, 132)',
      data: [parsedData.cropBase, parsedData.wineBase, parsedData.preserveBase],
      color: "#3ffd80",
      backgroundColor: "#3ffd80"
    },
      {
      label: "Silver Values",
      borderColor: 'rgb(255, 99, 132)',
      data: [parsedData.cropSilver, parsedData.wineSilver, parsedData.preserveSilver],
      color: "#bfe6f3",
      backgroundColor: "#bfe6f3"
    },
      {
      label: "Gold Values",
      borderColor: 'rgb(255, 99, 132)',
      data: [parsedData.cropGold, parsedData.wineGold, parsedData.preserveGold],
      color: "#fdd63f",
      backgroundColor: "#fdd63f"
    },
      {
      label: "Iridium Values",
      borderColor: 'rgb(255, 99, 132)',
      data: [parsedData.cropIridium, parsedData.wineIridium, parsedData.preserveIridium],
      color: "#c23ffd",
      backgroundColor: "#c23ffd"
    },
    ]};

const options = {
    title: {
      display: true,
      text: "Stardew Data"
    },
    showLines: true,
    aspectRatio: 1,
    layout: {
      padding: 0

    },
    scales: {
      y: {
        // min: 0,
        // max: 51,
        stacked: true,
        ticks: {
          stepSize: 25,
          display: true
        },
        grid: {
          drawTicks: true
        },
        title: {
          display: true,
          text: "Sell Value",
        }
      },
      x: {
        // min: 0,
        // max: 51,
        stacked: true,
        ticks: {
          stepSize: 25,
          display: true
        },
        grid: {
          drawTicks: true,
        },
        title: {
          display: true,
          text: "X Axis"
        }
      },
    },
    elements: {
      point: {
        radius: 5
      }
    }
};

const stackedBar = new Chart(ctx, {
  type: "bar",
  data: data,
  options: options
});