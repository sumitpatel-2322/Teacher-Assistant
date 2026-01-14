document.addEventListener("click", async (e) => {
  const btn = e.target.closest(".response-item");
  if (!btn) return;

  const solutionId = btn.dataset.solutionId;
  if (!solutionId) return;

  const detailsContainer = document.getElementById("solution-details");
  if (!detailsContainer) return;

  try {
    const res = await fetch(`/solution/details/${solutionId}`);
    const data = await res.json();

    if (!data.success) {
      detailsContainer.innerHTML = "<p>Unable to load solution details.</p>";
      return;
    }

    const steps = data.data.details.steps
      .map((s, i) => `<li>${i + 1}. ${s}</li>`)
      .join("");

    detailsContainer.innerHTML = `
      <h3>${data.data.title}</h3>
      <p><b>Objective:</b> ${data.data.details.objective}</p>
      <p><b>Time Required:</b> ${data.data.details.time_required_min} min</p>
      <ul>${steps}</ul>
    `;
  } catch (err) {
    console.error(err);
    detailsContainer.innerHTML = "<p>Error loading solution.</p>";
  }
});