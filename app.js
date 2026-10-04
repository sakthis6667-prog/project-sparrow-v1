const input = document.getElementById("input");
const send = document.getElementById("send");
const mic = document.getElementById("mic");
const chat = document.getElementById("chat");

function addMessage(who, text) {
  const div = document.createElement("div");
  div.className = `msg ${who === "You" ? "user" : "bot"}`;
  div.innerHTML = `${who}<div class="bubble"></div>`;
  div.querySelector(".bubble").textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function sendMessage() {
  const message = input.value.trim();
  if (!message) return;
  addMessage("You", message);
  input.value = "";

  try {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({message, language:"auto"})
    });
    const data = await res.json();
    addMessage("Sparrow", data.reply);
  } catch {
    addMessage("Sparrow", "Backend offline bro. First start the FastAPI server.");
  }
}

send.addEventListener("click", sendMessage);
input.addEventListener("keydown", e => { if (e.key === "Enter") sendMessage(); });

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (SpeechRecognition) {
  const recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = "en-IN";

  mic.addEventListener("click", () => {
    recognition.start();
    mic.textContent = "🔴";
  });

  recognition.onresult = e => {
    input.value = e.results[0][0].transcript;
    mic.textContent = "🎙";
    sendMessage();
  };
  recognition.onerror = () => mic.textContent = "🎙";
} else {
  mic.title = "Speech recognition is not supported in this browser.";
}
