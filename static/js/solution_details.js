document.addEventListener("click", async (e) => {
  const btn = e.target.closest(".response-item");
  if (!btn) return;

  const solutionId = btn.dataset.solutionId;
  if (!solutionId) return;

  const detailsContainer = document.getElementById("solution-details");
  if (!detailsContainer) return;

  try {
    // ✅ UPDATE: Use the global language variable
    const lang = window.currentLanguage || 'en';
    
    const res = await fetch(`/solution/details/${solutionId}?lang=${lang}`);
    const data = await res.json();

    if (!data.success) {
      detailsContainer.innerHTML = "<p>Unable to load solution details.</p>";
      return;
    }

    // Handle nested structure safely
    const stepSource = data.data.details?.steps || data.data.steps || [];
    const objective = data.data.details?.objective || data.data.objective || "Objective not available.";
    const title = data.data.preview?.title || data.data.title || "Solution";

    const steps = stepSource
      .map((s, i) => `<li>${i + 1}. ${s}</li>`)
      .join("");

    detailsContainer.innerHTML = `
      <h3>${title}</h3>
      <p><b>Objective:</b> ${objective}</p>
      <ul>${steps}</ul>
    `;
  } catch (err) {
    console.error(err);
    detailsContainer.innerHTML = "<p>Error loading solution.</p>";
  }
});