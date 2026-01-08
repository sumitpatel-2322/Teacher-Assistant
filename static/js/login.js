const hamburgerBtn = document.getElementById('hamburgerBtn');
    const sidepanel = document.getElementById('mySidepanel');

    hamburgerBtn.addEventListener('click', function() {
      if (document.body.classList.contains('sidepanel-open')) {
        sidepanel.style.width = "0";
        document.body.classList.remove('sidepanel-open');
      } else {
        sidepanel.style.width = "250px";
        document.body.classList.add('sidepanel-open');
      }
    });
  const hamburger = document.getElementById("hamburgerBtn");
  const closeBtn = document.getElementById("closeSidebar");

  hamburger.onclick = () => {
    sidepanel.classList.add("open");
  };

  closeBtn.onclick = () => {
    sidepanel.classList.remove("open");
  };