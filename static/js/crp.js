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
          "#2F5D50", // deep forest
          "#BFD6DA"  // mist light
        ],
        hoverBackgroundColor: [
          "#1E3A32",
          "#8FB8A8"
        ],
        borderWidth: 0
      }]
    },
    options: {
      cutout: "70%",
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
          "#6F9E8F", // soft green
          "#5F7F8C", // mist blue
          "#2F5D50", // deep forest
          "#8FB8A8", // light teal
          "#f1f5f6"  // mist light
        ],
        borderColor: "#1E3A32",
        borderWidth: 1.5,
        borderRadius: 6,
        barThickness: 30
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
            color: "#1E3A32",
            font: { size: 12, weight: "600" }
          }
        },
        y: {
          beginAtZero: true,
          max: 100,
          ticks: {
            stepSize: 20,
            callback: v => v + "%",
            color: "#1E3A32"
          },
          grid: {
            color: "rgba(30,58,50,0.12)"
          }
        }
      }
    }
  });
}
/* ================= UPLOAD GUIDANCE ================= */

const uploadBtn = document.querySelector(".actions button:nth-child(2)");
const uploadModal = document.getElementById("uploadModal");
const closeUpload = document.getElementById("closeUpload");

if (uploadBtn) {
  uploadBtn.addEventListener("click", () => {
    uploadModal.style.display = "flex";
  });
}

if (closeUpload) {
  closeUpload.addEventListener("click", () => {
    uploadModal.style.display = "none";
  });
}
/* ================= SCHEDULE VISIT ================= */

const visitBtn = document.querySelector(".actions button:nth-child(3)");
const visitModal = document.getElementById("visitModal");
const closeVisit = document.getElementById("closeVisit");

if (visitBtn) {
  visitBtn.addEventListener("click", () => {
    visitModal.style.display = "flex";
  });
}

if (closeVisit) {
  closeVisit.addEventListener("click", () => {
    visitModal.style.display = "none";
  });
}
