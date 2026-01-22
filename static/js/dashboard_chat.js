document.addEventListener("DOMContentLoaded", () => {
    const chatWindow = document.getElementById("chat-window");
    const userQuery = document.getElementById("userQuery");
    const sendBtn = document.getElementById("sendBtn");
    
    // FAB & Modal Elements
    const fabHelp = document.getElementById("fabHelp");
    const helpModal = document.getElementById("helpModal");
    const closeModal = document.querySelector(".close-modal");
    const submitEscalation = document.getElementById("submitEscalation");
    const escalateInput = document.getElementById("escalateInput");

    window.currentLanguage = window.userPreferredLanguage || "en";

    // Auto-resize textarea
    userQuery.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    sendBtn.addEventListener("click", sendMessage);

    // ➤ FAB LOGIC
    if(fabHelp && helpModal) {
        fabHelp.addEventListener("click", () => {
            helpModal.style.display = "block";
            escalateInput.focus();
        });
        
        closeModal.addEventListener("click", () => {
            helpModal.style.display = "none";
        });

        window.onclick = function(event) {
            if (event.target == helpModal) {
                helpModal.style.display = "none";
            }
        }
    }

    // ➤ ESCALATION SUBMIT
    if(submitEscalation) {
        submitEscalation.addEventListener("click", async () => {
            const text = escalateInput.value.trim();
            if(!text) {
                alert("Please describe your issue.");
                return;
            }

            // UI Feedback
            submitEscalation.innerText = "Sending...";
            submitEscalation.disabled = true;

            try {
                const response = await fetch("/api/teacher/escalate", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ query: text })
                });
                const data = await response.json();
                
                if(data.status === "success") {
                    alert("✅ Request sent to Expert!");
                    helpModal.style.display = "none";
                    escalateInput.value = "";
                } else {
                    alert("❌ Failed: " + data.message);
                }
            } catch(e) {
                console.error(e);
                alert("❌ Network error.");
            } finally {
                submitEscalation.innerText = "Send to CRP";
                submitEscalation.disabled = false;
            }
        });
    }

    async function sendMessage() {
        const text = userQuery.value.trim();
        const className = document.getElementById("classSelect").value;
        const subject = document.getElementById("subjectSelect").value;
        const topic = document.getElementById("topicSelect").value;

        if (!text) return;

        appendMessage("user", text);
        userQuery.value = "";
        userQuery.style.height = "auto";
        
        const loadingId = appendLoading();

        try {
            const response = await fetch("/api/teacher/ask", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    class_name: className,
                    subject: subject,
                    topic: topic,
                    question: text
                })
            });
            
            const data = await response.json();
            removeElement(loadingId);

            if (data.status === "success") {
                if (data.detected_language) {
                    window.currentLanguage = data.detected_language;
                }
                
                if (data.bot_message) {
                    appendMessage("bot", data.bot_message);
                }

                if (data.solutions && data.solutions.length > 0) {
                    window.renderSolutionButtons(data.solutions, data.request_id);
                } 
                
                if (!data.bot_message && (!data.solutions || data.solutions.length === 0)) {
                     appendMessage("bot", "I'm listening. Please ask your question.");
                }

            } else {
                appendMessage("bot", "I couldn't find a specific solution. Could you add more details?");
            }

        } catch (error) {
            console.error(error);
            removeElement(loadingId);
            appendMessage("bot", "Network error. Please try again.");
        }
    }

    function appendMessage(sender, text) {
        const div = document.createElement("div");
        div.className = `message ${sender}-msg`;
        div.innerHTML = `<div class="bubble">${text}</div>`;
        chatWindow.appendChild(div);
        scrollToBottom();
    }

    function appendLoading() {
        const id = "load-" + Date.now();
        const div = document.createElement("div");
        div.id = id;
        div.className = "message bot-msg";
        div.innerHTML = `<div class="bubble" style="font-style:italic; color:#777;">Thinking...</div>`;
        chatWindow.appendChild(div);
        scrollToBottom();
        return id;
    }

    function removeElement(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }

    function scrollToBottom() {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    window.fetchDetails = async (solutionId, requestId, btnElement) => {
        const siblings = btnElement.parentElement.children;
        for (let btn of siblings) btn.classList.remove("selected");
        btnElement.classList.add("selected");

        try {
            const lang = window.currentLanguage || 'en';
            const res = await fetch(`/solution/details/${solutionId}?lang=${lang}`);
            const data = await res.json();

            if (data.success) {
                renderDetailCard(data.data, requestId, solutionId);
            }
        } catch (err) {
            console.error(err);
            alert("Failed to load details.");
        }
    };

    function renderDetailCard(details, requestId, solutionId) {
        const stepSource = details.details?.steps || details.steps || [];
        const objectiveSource = details.details?.objective || details.objective || "Follow the steps below.";
        
        const steps = Array.isArray(stepSource) 
            ? stepSource.map(s => `<li>${s}</li>`).join("")
            : `<li>${stepSource}</li>`;
        
        const title = details.preview?.title || details.title || "Solution Details";

        const html = `
            <div class="bubble" style="width:100%; max-width:100%; background:transparent; padding:0;">
                <div class="detail-card">
                    <h3>${title}</h3>
                    <p><strong>Objective:</strong> ${objectiveSource}</p>
                    <ul>${steps}</ul>
                    
                    <div class="feedback-actions">
                        <button class="fb-btn fb-yes" onclick="sendFeedback('${requestId}', '${solutionId}', true, this)">✅ It Worked</button>
                        <button class="fb-btn fb-no" onclick="sendFeedback('${requestId}', '${solutionId}', false, this)">❌ Didn't Work</button>
                    </div>
                </div>
            </div>
        `;
        
        const div = document.createElement("div");
        div.className = "message bot-msg";
        div.innerHTML = html;
        chatWindow.appendChild(div);
        scrollToBottom();
    }

    window.sendFeedback = async (reqId, solId, worked, btn) => {
        const parent = btn.parentElement;
        parent.style.opacity = "0.5";
        parent.style.pointerEvents = "none";

        await fetch("/teacher/feedback", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                request_id: reqId,
                solution_id: solId,
                worked: worked
            })
        });

        if (worked) {
            parent.innerHTML = `<span style="font-size:13px; color:#379683; font-weight:600;">Thanks for your feedback!</span>`;
        } else {
            parent.innerHTML = `<span style="font-size:13px; color:#c0392b; font-weight:600;">Noted. We've alerted the CRP.</span>`;
        }
    };
});

window.renderSolutionButtons = function(solutions, requestId) {
    const chatWindow = document.getElementById("chat-window");
    const container = document.createElement("div");
    container.className = "message bot-msg";
    
    let btns = `<div class="bubble" style="background:transparent; padding:0;">
                <div class="solution-grid">`;

    solutions.forEach(sol => {
        const id = sol.id || sol.solution_id;
        const label = sol.title || sol.text;
        
        btns += `<button class="sol-btn" onclick="fetchDetails('${id}', '${requestId}', this)">
                    ${label} <span style="opacity:0.7; font-size:11px;">(${Math.round(sol.confidence * 100)}%)</span>
                 </button>`;
    });
    
    btns += `</div></div>`;
    container.innerHTML = btns;
    chatWindow.appendChild(container);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}