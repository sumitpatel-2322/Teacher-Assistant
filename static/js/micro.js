document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector(".micro-search input");
  const cards = document.querySelectorAll(".micro-card");

  function filterCards() {
    const query = input.value.toLowerCase();

    cards.forEach(card => {
      const text = card.innerText.toLowerCase();
      card.style.display = text.includes(query) ? "flex" : "none";
    });
  }

  input.addEventListener("keyup", filterCards);
  document
    .querySelector(".micro-search-btn")
    .addEventListener("click", filterCards);
});
