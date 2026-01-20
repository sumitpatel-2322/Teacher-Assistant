/* ================= DONUT CHART ================= */

const donutCtx = document.getElementById("completionDonut");

if (donutCtx) {
  new Chart(donutCtx, {
    type: "doughnut",
    data: {
      labels: ["Completed", "Remaining"],
      datasets: [{
        data: [70, 30],
        backgroundColor: [
          "#14B8A6",  // fresh teal (completed)
          "#E6FFFA"   // light aqua (remaining)
        ],
        hoverBackgroundColor: [
          "#0D9488",
          "#CCFBF1"
        ],
        borderWidth: 0
      }]
    },
    options: {
      cutout: "70%",
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: ctx => ctx.label + ": " + ctx.raw + "%"
          }
        }
      }
    }
  });
}
/* ================= HISTOGRAM CHART ================= */

const histCtx = document.getElementById("teacherHistogram");

if (histCtx) {
  new Chart(histCtx, {
    type: "bar",
    data: {
      labels: ["0–20%", "21–40%", "41–60%", "61–80%", "81–100%"],
      datasets: [{
        data: [5, 15, 30, 35, 15],
        backgroundColor: [
          "#E0F2FE", // light sky (low)
          "#7DD3FC", // soft blue
          "#38BDF8", // clear blue
          "#0cb3b3", // success green
          "#24cfa7"  // strong green (high)
        ],
        borderColor: "#134E4A",
        borderWidth: 1.2,
        borderRadius: 8,
        barThickness: 32
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: {
            color: "#134E4A",
            font: { size: 12, weight: "600" }
          }
        },
        y: {
          beginAtZero: true,
          max: 100,
          ticks: {
            stepSize: 20,
            callback: v => v + "%",
            color: "#134E4A"
          },
          grid: {
            color: "rgba(20,184,166,0.18)"
          }
        }
      }
    }
  });
}
