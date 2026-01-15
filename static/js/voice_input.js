let mediaRecorder = null;
let audioChunks = [];
let isRecording = false;

const micButton = document.getElementById("micBtn");
const loader = document.getElementById("voiceLoader");

// Safety check
if (!micButton) {
    console.error("Mic button not found in DOM");
}

/**
 * Start recording audio
 */
async function startRecording() {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert("Microphone not supported in this browser");
        return;
    }

    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
            if (event.data && event.data.size > 0) {
                audioChunks.push(event.data);
            }
        };

        mediaRecorder.onstop = sendAudioToBackend;

        mediaRecorder.start();
        isRecording = true;

        // UI updates
        micButton.classList.add("recording");
        loader.innerText = "Listening...";
        loader.style.display = "inline";

    } catch (err) {
        console.error("Mic access error:", err);
        alert("Could not access microphone");
    }
}

/**
 * Stop recording audio
 */
function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;

        // UI updates
        micButton.classList.remove("recording");
        loader.innerText = "Processing...";
    }
}

/**
 * Send recorded audio to backend
 */
async function sendAudioToBackend() {
    if (!audioChunks.length) {
        loader.style.display = "none";
        return;
    }

    const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
    const formData = new FormData();
    formData.append("audio", audioBlob);

    try {
        const response = await fetch("/api/teacher/voice", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Voice request failed");
        }

        const data = await response.json();

        loader.style.display = "none";

        if (data.status === "success" && data.solutions) {
            if (window.renderSolutionButtons) {
                window.renderSolutionButtons(data.solutions, data.request_id);
            } else {
                console.error("renderSolutionButtons is not defined");
            }
        } else if (data.error) {
            alert(data.error);
        } else {
            alert("Could not process voice input");
        }

    } catch (err) {
        console.error("Voice processing error:", err);
        alert("Voice processing failed");
        loader.style.display = "none";
    } finally {
        micButton.classList.remove("recording");
    }
}

/**
 * Mic button click handler
 */
micButton.addEventListener("click", () => {
    if (!isRecording) {
        startRecording();
    } else {
        stopRecording();
    }
});