document.addEventListener("DOMContentLoaded", () => {

  // ------------------------------
  // Sidebar logic (UNCHANGED)
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
  // AI Response Selection Logic
  // ------------------------------

  let selectedSolutionId = null;

  function attachSolutionClickHandlers() {
    const responseButtons = document.querySelectorAll(".response-item");

    responseButtons.forEach(btn => {
      btn.addEventListener("click", () => {

        // Hide all other responses
        responseButtons.forEach(other => {
          if (other !== btn) {
            other.style.display = "none";
          }
        });

        // Highlight selected response
        btn.classList.add("active");

        // Save selected solution
        selectedSolutionId = btn.dataset.solutionId;

        console.log("Selected solution:", selectedSolutionId);
      });
    });
  }

  attachSolutionClickHandlers();

  // ------------------------------
  // Feedback Handling
  // ------------------------------

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
      .then(() => {
        if (worked) {
          alert("Have a nice teaching 😊");
        } else {
          alert("Thank you for your feedback!");
        }
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

  // ------------------------------
  // 🔥 CRITICAL FIX: Allow Multiple Queries
  // ------------------------------

  const askForm = document.querySelector("form[action='/teacher/ask']");

  if (askForm) {
    askForm.addEventListener("submit", () => {

      // Reset selected solution
      selectedSolutionId = null;

      

      // Clear feedback box
      const feedbackBox = document.getElementById("feedback");
      if (feedbackBox) feedbackBox.value = "";

      // Reset AI responses UI (safety reset)
      document.querySelectorAll(".response-item").forEach(btn => {
        btn.style.display = "block";
        btn.classList.remove("active");
      });

      console.log("New query submitted – form state reset");
    });
  }

});
