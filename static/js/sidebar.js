document.addEventListener("DOMContentLoaded", () => {
    const hamburgerBtn = document.getElementById("hamburgerBtn");
    const sidepanel = document.getElementById("mySidepanel");
    const closeBtn = document.getElementById("closeSidebar");
    const body = document.body;

    function openNav() {
        if(sidepanel) sidepanel.style.width = "250px";
        body.classList.add("sidepanel-open");
    }

    function closeNav() {
        if(sidepanel) sidepanel.style.width = "0";
        body.classList.remove("sidepanel-open");
    }

    if (hamburgerBtn) hamburgerBtn.addEventListener("click", openNav);
    if (closeBtn) closeBtn.addEventListener("click", closeNav);

    // Close on outside click (optional polish)
    document.addEventListener("click", (e) => {
        if (sidepanel && 
            sidepanel.style.width === "250px" && 
            !sidepanel.contains(e.target) && 
            e.target !== hamburgerBtn) {
            closeNav();
        }
    });
});