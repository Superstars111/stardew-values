const graph = document.getElementById("display_graph")
const ctx = graph.getContext("2d");
let rawData = graph.dataset.points;
let parsedData = JSON.parse(rawData);

let data = {
    labels: ["Crops", "Wines", "Preserves"],
    datasets: [
      {
      label: "Base Values",
      borderColor: 'rgb(255, 99, 132)',
      data: parsedData,
      color: "#878BB6"
    },
      {
      label: "Silver Values",
      borderColor: 'rgb(255, 99, 132)',
      data: parsedData,
      color: "#878BB6"
    },
      {
      label: "Gold Values",
      borderColor: 'rgb(255, 99, 132)',
      data: parsedData,
      color: "#878BB6"
    },
      {
      label: "Iridium Values",
      borderColor: 'rgb(255, 99, 132)',
      data: parsedData,
      color: "#878BB6"
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
          display: false
        },
        grid: {
          drawTicks: false
        },
        title: {
          display: true,
          text: "Y Axis",
        }
      },
      x: {
        // min: 0,
        // max: 51,
        stacked: true,
        ticks: {
          stepSize: 25,
          display: false
        },
        grid: {
          drawTicks: false,
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