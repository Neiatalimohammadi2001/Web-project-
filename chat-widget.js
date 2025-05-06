const API_KEY = "sk-98aa0314f691433eb4b08cd85454a194";
const chatContainer = document.getElementById("chatContainer");
const chatMessages = document.getElementById("chatMessages");
const chatInput = document.getElementById("chatInput");
const notificationBadge = document.getElementById("notificationBadge");

// Toggle chat visibility
function toggleChat() {
  chatContainer.classList.toggle("active");
  notificationBadge.style.display = "none";
  chatInput.focus();
}

// Send user message
async function sendMessage() {
  const message = chatInput.value.trim();
  if (!message) return;

  appendMessage("user", message);
  chatInput.value = "";

  // Show typing indicator
  const typingIndicator = document.createElement("div");
  typingIndicator.classList.add("message", "typing");
  typingIndicator.innerHTML = `
    <div class="message-content typing-indicator">
      <span></span><span></span><span></span>
    </div>`;
  chatMessages.appendChild(typingIndicator);
  chatMessages.scrollTop = chatMessages.scrollHeight;

  const response = await fetchDeepSeekReply(message);

  // Remove typing indicator
  typingIndicator.remove();

  // Append AI response
  appendMessage("bot", response);
}

// Add message to chat
function appendMessage(sender, text) {
  const messageEl = document.createElement("div");
  messageEl.classList.add("message", sender);
  messageEl.innerHTML = `
    <div class="message-content">${text}</div>
    <div class="message-time">${new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'})}</div>
  `;
  chatMessages.appendChild(messageEl);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Call DeepSeek R1 API
async function fetchDeepSeekReply(userMessage) {
  try {
    const response = await fetch("https://api.deepseek.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "deepseek-chat",
        messages: [
          { role: "system", content: "You are a helpful assistant who knows everything about Chinese culture, food, and travel." },
          { role: "user", content: userMessage }
        ]
      })
    });

    const data = await response.json();
    return data.choices?.[0]?.message?.content?.trim() || "Sorry, I couldn't process that.";
  } catch (err) {
    console.error(err);
    return "An error occurred. Please try again.";
  }
}
