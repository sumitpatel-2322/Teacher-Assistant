document.addEventListener("DOMContentLoaded", () => {

  // ------------------------------
  // Sidebar logic (unchanged)
  // ------------------------------
  const hamburgerBtn = document.getElementById("hamburgerBtn");
  const sidepanel = document.getElementById("mySidepanel");
  const closeBtn = document.querySelector(".sidebar-close");
  const links = document.querySelectorAll("#mySidepanel a");

  if (hamburgerBtn) {
    hamburgerBtn.addEventListener("click", () => {
      sidepanel.classList.toggle("open");
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      sidepanel.classList.remove("open");
    });
  }

  links.forEach(link => {
    link.addEventListener("click", () => {
      sidepanel.classList.remove("open");
    });
  });

  // ------------------------------
  // Decision Engine Feedback Wiring
  // ------------------------------

  let selectedSolutionId = null;

  function sendFeedback(worked) {
    if (!selectedSolutionId) {
      alert("Please select a solution first.");
      return;
    }

    const feedbackText = document.getElementById("feedback")?.value || "";
    const requestId = document.getElementById("request_id")?.value;

    fetch("/teacher/feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        request_id: requestId,
        solution_id: selectedSolutionId,
        worked: worked,
        feedback: feedbackText
      })
    })
      .then(res => res.json())
      .then(data => {
        console.log("Feedback response:", data);
        alert("Feedback recorded. Thank you!");
      })
      .catch(err => {
        console.error("Feedback error:", err);
        alert("Failed to send feedback.");
      });
  }

  const workedBtn = document.querySelector(".worked");
  const notWorkedBtn = document.querySelector(".not-worked");

  if (workedBtn) {
    workedBtn.addEventListener("click", () => sendFeedback(true));
  }

  if (notWorkedBtn) {
    notWorkedBtn.addEventListener("click", () => sendFeedback(false));
  }
});