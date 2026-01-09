const hamburgerBtn = document.getElementById('hamburgerBtn');
const sidepanel = document.getElementById('mySidepanel');
const closeBtn = document.getElementById("closeSidebar");

hamburgerBtn.addEventListener('click', function () {
  if (document.body.classList.contains('sidepanel-open')) {
    sidepanel.style.width = "0";
    document.body.classList.remove('sidepanel-open');
  } else {
    sidepanel.style.width = "250px";
    document.body.classList.add('sidepanel-open');
  }
});

/* close button */
closeBtn.onclick = () => {
  sidepanel.style.width = "0";
  document.body.classList.remove('sidepanel-open');
};

/* role storage (login) */
const loginForm = document.querySelector("form");
const roleSelect = document.getElementById("role");

loginForm.addEventListener("submit", function () {
  const role = roleSelect.value;
  if (role) {
    localStorage.setItem("userRole", role);
  }
});
