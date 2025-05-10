// Mensagens da "IA"
const messages = [
    "Olá! Estou aqui para ajudar você a começar. 😊",
    "Pronto para digitalizar seus projetos?",
    "Vamos colaborar e construir algo incrível juntos!"
];

// Selecionar o elemento do texto da IA
const aiTextElement = document.querySelector(".ai-text");

// Função para alternar mensagens
let messageIndex = 0;
function changeMessage() {
    aiTextElement.textContent = messages[messageIndex];
    messageIndex = (messageIndex + 1) % messages.length; // Alternar entre as mensagens
}

// Alterar a mensagem a cada 5 segundos
setInterval(changeMessage, 5000);