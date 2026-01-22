/* ================= CRP DASHBOARD LOGIC ================= */

let donutChart = null;
let histChart = null;

document.addEventListener("DOMContentLoaded", () => {
    // 1. Initial Load (All Schools)
    fetchStats("");

    // 2. Dropdown Listener
    const schoolSelect = document.getElementById("teacherDropdown");
    if (schoolSelect) {
        schoolSelect.addEventListener("change", (e) => {
            const schoolId = e.target.value;
            fetchStats(schoolId);
        });
    }
});

async function fetchStats(schoolId) {
    try {
        let url = "/api/crp/stats";
        if (schoolId) url += `?school_id=${encodeURIComponent(schoolId)}`;

        const res = await fetch(url);
        const data = await res.json();

        updateDonut(data.pie_data);
        updateHistogram(data.hist_labels, data.hist_data);

    } catch (err) {
        console.error("Error fetching stats:", err);
    }
}

/* ================= DONUT CHART (Success Rate) ================= */
function updateDonut(dataArray) {
    const ctx = document.getElementById("completionDonut");
    if (!ctx) return;

    // dataArray = [Success, Failed, Unrated]
    
    if (donutChart) {
        donutChart.data.datasets[0].data = dataArray;
        donutChart.update();
    } else {
        donutChart = new Chart(ctx, {
            type: "doughnut",
            data: {
                labels: ["Solved", "Issues (Didn't Work)", "Unrated"],
                datasets: [{
                    data: dataArray,
                    backgroundColor: ["#14B8A6", "#EF4444", "#CBD5E1"], // Teal, Red, Gray
                    hoverBackgroundColor: ["#0D9488", "#DC2626", "#94A3B8"],
                    borderWidth: 0
                }]
            },
            options: {
                cutout: "70%",
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: { position: 'bottom', labels: { boxWidth: 10 } },
                    title: { display: true, text: 'Query Resolution Status' }
                }
            }
        });
    }
}

/* ================= HISTOGRAM (Problem Areas) ================= */
function updateHistogram(labels, dataValues) {
    const ctx = document.getElementById("teacherHistogram");
    if (!ctx) return;

    if (histChart) {
        histChart.data.labels = labels;
        histChart.data.datasets[0].data = dataValues;
        histChart.update();
    } else {
        histChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: labels, // e.g. ["Classroom Mgmt", "Math", "Attention"]
                datasets: [{
                    label: "Failed Queries",
                    data: dataValues,
                    backgroundColor: "#EF4444", // Red for problems
                    borderRadius: 4,
                    barThickness: 40
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    title: { display: true, text: 'Top Problem Areas (Failed Queries)' }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { stepSize: 1 }
                    }
                }
            }
        });
    }
}