const form = document.querySelector("#chat-form");
const input = document.querySelector("#message");
const conversation = document.querySelector("#conversation");
const status = document.querySelector("#status");

function addMessage(text, role) {
  const message = document.createElement("div");
  message.className = `message ${role}`;
  message.textContent = text;
  conversation.appendChild(message);
  conversation.scrollTop = conversation.scrollHeight;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";
  input.disabled = true;
  status.textContent = "Thinking...";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "The request failed.");
    addMessage(data.response, "assistant");
    status.textContent = "Ready";
  } catch (error) {
    addMessage(`Sorry, I could not complete that request: ${error.message}`, "assistant");
    status.textContent = "Something went wrong";
  } finally {
    input.disabled = false;
    input.focus();
  }
});
