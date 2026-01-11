document.addEventListener("DOMContentLoaded", () => {

  const hamburgerBtn = document.getElementById("hamburgerBtn");
  const sidepanel = document.getElementById("mySidepanel");
  const closeBtn = document.querySelector(".sidebar-close");
  const links = document.querySelectorAll("#mySidepanel a");
  const dashboardLink = document.getElementById("dashboardLink");

  hamburgerBtn.addEventListener("click", () => {
    sidepanel.classList.toggle("open");
  });

  closeBtn.addEventListener("click", () => {
    sidepanel.classList.remove("open");
  });

  links.forEach(link => {
    link.addEventListener("click", () => {
      sidepanel.classList.remove("open");
    });
  });
});