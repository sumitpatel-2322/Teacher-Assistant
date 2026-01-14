const data = {
  "Class 1": { "Drawing": ["Colors"], "Mathematic": ["Addition"], "English": ["Alphabets"] },
  "Class 2": { "Mathematic": ["Tables"], "English": ["Simple Sentences"] },
  "Class 3": { "Mathematics": ["Algebra"], "Science": ["Biology"] },
  "Class 4": { "Mathematics": ["Geometry"] },
  "Class 5": { "Mathematics": ["Algebra"], "Science": ["Physics"] },
  "Class 6": { "Mathematics": ["Algebra"], "Science": ["Biology"] },
  "Class 7": { "Mathematics": ["Geometry"], "Science": ["Physics"] },
  "Class 8": { "Mathematics": ["Algebra"], "Science": ["Biology"] },
  "Class 9": { "Mathematics": ["Trigonometry"], "Science": ["Motion"] },
  "Class 10": { "Mathematics": ["Calculus"], "Science": ["Optics"] }
};

document.addEventListener("DOMContentLoaded", () => {
    const classSelect = document.getElementById("classSelect");
    const subjectSelect = document.getElementById("subjectSelect");
    const topicSelect = document.getElementById("topicSelect");

    if (!classSelect || !subjectSelect) return;

    // Helper: Populate Subjects
    function populateSubjects(className, selectedSubject = "") {
        subjectSelect.innerHTML = '<option value="">Subject</option>';
        topicSelect.innerHTML = '<option value="">Topic</option>';
        
        if (!className || !data[className]) {
            subjectSelect.disabled = true;
            topicSelect.disabled = true;
            return;
        }

        subjectSelect.disabled = false;
        Object.keys(data[className]).forEach(subj => {
            const isSelected = (subj === selectedSubject) ? "selected" : "";
            subjectSelect.innerHTML += `<option value="${subj}" ${isSelected}>${subj}</option>`;
        });
    }

    // Event Listener
    classSelect.addEventListener("change", () => {
        populateSubjects(classSelect.value);
    });

    subjectSelect.addEventListener("change", () => {
        topicSelect.innerHTML = '<option value="">Topic</option>';
        const cls = classSelect.value;
        const sub = subjectSelect.value;

        if (cls && sub && data[cls][sub]) {
            topicSelect.disabled = false;
            data[cls][sub].forEach(topic => {
                topicSelect.innerHTML += `<option value="${topic}">${topic}</option>`;
            });
        } else {
            topicSelect.disabled = true;
        }
    });

    // ➤ AUTO-TRIGGER ON LOAD (The Prefill Fix)
    if (classSelect.value) {
        // If HTML has a value (from backend), load subjects immediately
        // We pass the current value of subjectSelect to keep it selected
        const currentSubject = subjectSelect.options[subjectSelect.selectedIndex]?.text || "";
        populateSubjects(classSelect.value, currentSubject);
    }
});