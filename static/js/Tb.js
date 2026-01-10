document.addEventListener("DOMContentLoaded", function () {

  const sidepanel = document.getElementById("mySidepanel");
  const hamburgerBtn = document.getElementById("hamburgerBtn");
  const closeBtn = document.querySelector("#mySidepanel .sidebar-close");

  // Open panel
  hamburgerBtn.addEventListener("click", function () {
    sidepanel.style.width = "250px";
  });

  // Close panel (✕ button)
  closeBtn.addEventListener("click", function () {
    sidepanel.style.width = "0";
  });

});

