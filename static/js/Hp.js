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

if (dashboardLink) {
  dashboardLink.addEventListener("click", () => {
    const isLoggedIn = localStorage.getItem("isLoggedIn");
    const role = localStorage.getItem("userRole");
    if (!isLoggedIn || !role) {
      window.location.href = "/login";
      return;
    }

    if (role === "teacher") {
      window.location.href = "/teacher";
    } else if (role === "student") {
      window.location.href = "/student";
    } else if (role === "admin") {
      window.location.href = "/admin";
    } else {
      window.location.href = "/login";
    }
  });
}
});
