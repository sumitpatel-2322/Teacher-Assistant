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
    const topicSelect = document.getElementById("topicSelect"); // Can be null on Profile page

    if (!classSelect || !subjectSelect) return;

    // Helper: Populate Subjects
    function populateSubjects(className, selectedSubject = "") {
        subjectSelect.innerHTML = '<option value="">Subject</option>';
        
        // ✅ SAFETY CHECK: Only clear topic if it exists
        if (topicSelect) {
            topicSelect.innerHTML = '<option value="">Topic</option>';
            topicSelect.disabled = true;
        }
        
        if (!className || !data[className]) {
            subjectSelect.disabled = true;
            return;
        }

        subjectSelect.disabled = false;
        Object.keys(data[className]).forEach(subj => {
            // Check if this option matches the pre-selected value
            const isSelected = (subj === selectedSubject) ? "selected" : "";
            subjectSelect.innerHTML += `<option value="${subj}" ${isSelected}>${subj}</option>`;
        });
    }

    // Event Listener: Class Change
    classSelect.addEventListener("change", () => {
        populateSubjects(classSelect.value);
    });

    // Event Listener: Subject Change (Only if topic exists)
    subjectSelect.addEventListener("change", () => {
        const cls = classSelect.value;
        const sub = subjectSelect.value;
        
        // ✅ SAFETY CHECK: Only populate topics if the element exists
        if (topicSelect) {
            topicSelect.innerHTML = '<option value="">Topic</option>';
            
            if (cls && sub && data[cls][sub]) {
                topicSelect.disabled = false;
                data[cls][sub].forEach(topic => {
                    topicSelect.innerHTML += `<option value="${topic}">${topic}</option>`;
                });
            } else {
                topicSelect.disabled = true;
            }
        }
    });

    // ➤ AUTO-TRIGGER ON LOAD (The Prefill Fix)
    if (classSelect.value) {
        // We pass the currently rendered text in subjectSelect to keep it selected
        const currentSubject = subjectSelect.options[subjectSelect.selectedIndex]?.text || "";
        // Clean up text (in case Jinja left spaces)
        populateSubjects(classSelect.value, currentSubject.trim());
    }
});