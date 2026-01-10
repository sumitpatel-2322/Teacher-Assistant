const data = {
  "Class 1": {
    "Drawing": ["Colors", "Shapes"],
    "Mathematic": ["Addition","Subtraction","Multiplication","Division" ],
    "English": ["Alphabets", "Basic Words"],
    "Science": ["Plants", "Animals"],
    "Social Studies": ["My Family", "My School"],
    "Marathi": ["वर्णमाला", "साधे शब्द"]
  },
   "Class 2": {
    "Drawing": ["Colors", "Shapes"],
    "Mathematics": ["Tables", "Patterns"],
    "English": ["Simple Sentences", "Common Nouns"],
    "Science": ["Physics", "Biology"],
    "Social Studies": ["Community Helpers", "Festivals"],
    "Marathi": ["साधे वाक्य", "सामान्य नामे"]
  },
   "Class 3": {
    "Drawing": ["Colors", "Shapes"],
    "Social Studies": ["Maps", "History"],
    "English": ["Grammar", "Vocabulary"],
    "Marathi": ["व्याकरण", "शब्दसंग्रह"],
    "Science": ["Chemistry", "Biology"],
    "Mathematics": ["Algebra", "Geometry"],
  },
  "Class 4": {
    "Mathematics": ["Algebra", "Geometry"],

  },
   "Class 5": {
    "Mathematics": ["Algebra", "Geometry"],
    "Science": ["Physics", "Biology"]
  },
   "Class 6": {
    "Mathematics": ["Algebra", "Geometry"],
    "Science": ["Physics", "Biology"]
  },
   "Class 7": {
    "Mathematics": ["Algebra", "Geometry"],
    "Science": ["Physics", "Biology"]
  },
   "Class 8": {
    "Mathematics": ["Algebra", "Geometry"],
    "Science": ["Physics", "Biology"]
  },
  "Class 9": {
    "Mathematics": ["Integers", "Fractions"],
    "Science": ["Motion", "Heat"]
  },
  
  "Class 10": {
    "Mathematics": ["Integers", "Fractions"],
    "Science": ["Motion", "Heat"]
  }
};

const classSelect = document.getElementById("classSelect");
const subjectSelect = document.getElementById("subjectSelect");
const topicSelect = document.getElementById("topicSelect");

classSelect.addEventListener("change", () => {
  subjectSelect.innerHTML = '<option value="">Subject</option>';
  topicSelect.innerHTML = '<option value="">Topic</option>';
  subjectSelect.disabled = true;
  topicSelect.disabled = true;

  const cls = classSelect.value;
  if (!cls) return;

  Object.keys(data[cls]).forEach(subject => {
    subjectSelect.innerHTML += `<option value="${subject}">${subject}</option>`;
  });

  subjectSelect.disabled = false;
});

subjectSelect.addEventListener("change", () => {
  topicSelect.innerHTML = '<option value="">Topic</option>';
  topicSelect.disabled = true;

  const cls = classSelect.value;
  const sub = subjectSelect.value;
  if (!sub) return;

  data[cls][sub].forEach(topic => {
    topicSelect.innerHTML += `<option value="${topic}">${topic}</option>`;
  });

  topicSelect.disabled = false;
});
