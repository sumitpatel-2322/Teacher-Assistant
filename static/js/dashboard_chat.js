document.addEventListener("DOMContentLoaded", () => {
    const chatWindow = document.getElementById("chat-window");
    const userQuery = document.getElementById("userQuery");
    const sendBtn = document.getElementById("sendBtn");
    
    // ✅ 1. Initialize with Profile Preference (or default to 'en')
    // This variable is injected by Teacher_dashboard.html
    window.currentLanguage = window.userPreferredLanguage || "en";
    console.log("System Initialized with Language:", window.currentLanguage);

    // Auto-resize textarea
    userQuery.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    sendBtn.addEventListener("click", sendMessage);

    async function sendMessage() {
        const text = userQuery.value.trim();
        const className = document.getElementById("classSelect").value;
        const subject = document.getElementById("subjectSelect").value;
        const topic = document.getElementById("topicSelect").value;

        if (!text) return;

        // 1. UI: Append User Message
        appendMessage("user", text);
        userQuery.value = "";
        userQuery.style.height = "auto";
        
        // 2. UI: Show Loading
        const loadingId = appendLoading();

        try {
            // 3. API Call
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
                // Update language if backend detected/enforced something new
                if (data.detected_language) {
                    window.currentLanguage = data.detected_language;
                }
                
                // ✅ LOGIC UPDATE: Handle Hybrid Conversation
                
                // A. Show the Bot Message (If exists)
                // This covers "Chit-Chat" (Hello/Thanks) AND "Teaching" (Hybrid Header)
                if (data.bot_message) {
                    appendMessage("bot", data.bot_message);
                }

                // B. Render Solution Cards (ONLY if they exist)
                // Chit-chat responses won't have solutions, so we skip this block
                if (data.solutions && data.solutions.length > 0) {
                    window.renderSolutionButtons(data.solutions, data.request_id);
                } 
                
                // C. Fallback: If success but empty (Edge case)
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

    // GLOBAL FUNCTION: Fetch Details (Called by buttons)
    window.fetchDetails = async (solutionId, requestId, btnElement) => {
        const siblings = btnElement.parentElement.children;
        for (let btn of siblings) btn.classList.remove("selected");
        btnElement.classList.add("selected");

        try {
            // ✅ Pass the global language variable to the details API
            const lang = window.currentLanguage || 'en';
            console.log(`Fetching details for ${solutionId} in ${lang}`);
            
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
        // Handle structure variations
        const stepSource = details.details?.steps || details.steps || [];
        const objectiveSource = details.details?.objective || details.objective || "Follow the steps below.";
        
        // Handle list of steps safely
        const steps = Array.isArray(stepSource) 
            ? stepSource.map(s => `<li>${s}</li>`).join("")
            : `<li>${stepSource}</li>`;
        
        // Extract Title safely (Translated title comes from backend)
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

    // GLOBAL FUNCTION: Feedback
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

        parent.innerHTML = `<span style="font-size:13px; color:#379683; font-weight:600;">Thanks for your feedback!</span>`;
    };
});
    /* ================= NOTICE PANEL LOGIC ================= */

    const noticeBtn = document.querySelector(".notice-btn");
    const noticePanel = document.getElementById("notice-panel");
    const closeNotice = document.getElementById("closeNotice");

    if (noticeBtn && noticePanel) {
        noticeBtn.addEventListener("click", () => {
            noticePanel.style.display = "block";
        });
    }

    if (closeNotice) {
        closeNotice.addEventListener("click", () => {
            noticePanel.style.display = "none";
        });
    }


// ➤ GLOBAL FUNCTION EXPOSED TO WINDOW
window.renderSolutionButtons = function(solutions, requestId) {
    const chatWindow = document.getElementById("chat-window");
    const container = document.createElement("div");
    container.className = "message bot-msg";
    
    // 👇 The header text is now handled by the LLM 'bot_message' above.
    // We just render the grid of buttons here.
    let btns = `<div class="bubble" style="background:transparent; padding:0;">
                <div class="solution-grid">`;

    solutions.forEach(sol => {
        const id = sol.id || sol.solution_id;
        // Use the translated title if available, otherwise fallback to text
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