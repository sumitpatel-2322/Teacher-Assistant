const data = {
  "Class 1": { "Drawing": ["Colors"], "Mathematic": ["Addition"], "English": ["Alphabets"],"EVS": ["Plants"] },
  "Class 2": { "Drawing": ["Shapes"], "Mathematic": ["Tables"], "English": ["Simple Sentences"],"EVS": ["Animals"] },
  "Class 3": { "Drawing": ["Shapes"], "Mathematics": ["Algebra"], "Science": ["Biology"], "EVS": ["Birds"] },
  "Class 4": { "Drawing": ["Shapes"], "Mathematics": ["Geometry"] , "Science": ["Chemistry"] , "EVS": ["Flowers"] },
  "Class 5": { "Drawing": ["Shapes"], "Mathematics": ["Algebra"], "Science": ["Physics"] , "EVS": ["Trees"] },
  "Class 6": { "Drawing": ["Shapes"], "Mathematics": ["Algebra"], "Science": ["Biology"] , "EVS": ["Insects"] },
  "Class 7": { "Drawing": ["Shapes"], "Mathematics": ["Geometry"], "Science": ["Physics"] , "EVS": ["Birds"] },
  "Class 8": { "Drawing": ["Shapes"], "Mathematics": ["Algebra"], "Science": ["Biology"], "EVS": ["Animals"] ,"Hindi": ["Grammar"] },
  "Class 9": { "Drawing": ["Shapes"], "Mathematics": ["Trigonometry"], "Science": ["Motion"], "EVS": ["Plants"],"Social Studies": ["History"], "Hindi": ["Literature"] },
  "Class 10": { "Drawing": ["Shapes"], "Mathematics": ["Calculus"], "Science": ["Optics"] , "EVS": ["Birds"] ,"Social Studies": ["Geography"], "Hindi": ["Poetry"] },
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