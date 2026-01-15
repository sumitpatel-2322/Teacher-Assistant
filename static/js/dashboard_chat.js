document.addEventListener("DOMContentLoaded", () => {
    const chatWindow = document.getElementById("chat-window");
    const userQuery = document.getElementById("userQuery");
    const sendBtn = document.getElementById("sendBtn");
    
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

            if (data.status === "success" && data.solutions.length > 0) {
                window.renderSolutionButtons(data.solutions, data.request_id);
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
            const res = await fetch(`/solution/details/${solutionId}`);
            const data = await res.json();

            if (data.success) {
                renderDetailCard(data.data, requestId, solutionId);
            }
        } catch (err) {
            alert("Failed to load details.");
        }
    };

    function renderDetailCard(details, requestId, solutionId) {
        const steps = details.details.steps.map(s => `<li>${s}</li>`).join("");
        
        const html = `
            <div class="bubble" style="width:100%; max-width:100%; background:transparent; padding:0;">
                <div class="detail-card">
                    <h3>${details.title}</h3>
                    <p><strong>Objective:</strong> ${details.details.objective}</p>
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

// ➤ GLOBAL FUNCTION EXPOSED TO WINDOW
window.renderSolutionButtons = function(solutions, requestId) {
    const chatWindow = document.getElementById("chat-window");
    const container = document.createElement("div");
    container.className = "message bot-msg";
    
    let btns = `<div class="bubble" style="background:transparent; padding:0;">
                <p style="margin-bottom:8px; font-size:13px; color:#555;">Found ${solutions.length} suggestions:</p>
                <div class="solution-grid">`;

    solutions.forEach(sol => {
        const id = sol.id || sol.solution_id;
        btns += `<button class="sol-btn" onclick="fetchDetails('${id}', '${requestId}', this)">
                    ${sol.text} <span style="opacity:0.7; font-size:11px;">(${Math.round(sol.confidence * 100)}%)</span>
                 </button>`;
    });
    
    btns += `</div></div>`;
    container.innerHTML = btns;
    chatWindow.appendChild(container);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}