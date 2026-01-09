const hamburgerBtn = document.getElementById('hamburgerBtn');
const sidepanel = document.getElementById('mySidepanel');

hamburgerBtn.addEventListener('click', function () {
  if (document.body.classList.contains('sidepanel-open')) {
    sidepanel.style.width = "0";
    document.body.classList.remove('sidepanel-open');
  } else {
    sidepanel.style.width = "250px";
    document.body.classList.add('sidepanel-open');
  }
});

function openDashboard() {
  const role = localStorage.getItem("userRole"); 

  if (!role) {
    window.location.href = "/login";
    return;
  }

  if (role === "teacher") {
    window.location.href = "/teacher-dashboard";
  } else if (role === "crp") {
    window.location.href = "/CRP";
  } else if (role === "brp") {
    window.location.href = "/BRP";
  } else if (role === "arp") {
    window.location.href = "/ARP";
  } else {
    window.location.href = "/login";
  }
}
