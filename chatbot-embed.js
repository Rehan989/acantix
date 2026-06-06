(function () {
  'use strict';

  if (window.__acantixChatLoaded) return;
  window.__acantixChatLoaded = true;

  const API_BASE = 'https://restaurants-web-chatbot.onrender.com';

  /* ── Inject styles ── */
  const css = `
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    #acx-launcher {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 2147483646;
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: #0a0a0a;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 24px rgba(0,0,0,0.28), 0 1px 6px rgba(0,0,0,0.12);
      transition: transform 0.22s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.22s ease;
      outline: none;
      padding: 0;
    }
    #acx-launcher:hover {
      transform: scale(1.1);
      box-shadow: 0 8px 32px rgba(0,0,0,0.34), 0 2px 8px rgba(0,0,0,0.14);
    }
    #acx-launcher:active { transform: scale(0.94); }

    #acx-launcher .acx-icon-chat,
    #acx-launcher .acx-icon-close {
      position: absolute;
      transition: opacity 0.2s ease, transform 0.28s cubic-bezier(0.34,1.56,0.64,1);
    }
    #acx-launcher .acx-icon-close {
      opacity: 0;
      transform: scale(0.5) rotate(90deg);
    }
    #acx-launcher.acx-open .acx-icon-chat {
      opacity: 0;
      transform: scale(0.5) rotate(-90deg);
    }
    #acx-launcher.acx-open .acx-icon-close {
      opacity: 1;
      transform: scale(1) rotate(0deg);
    }

    #acx-panel {
      position: fixed;
      bottom: 92px;
      right: 24px;
      z-index: 2147483645;
      width: 380px;
      height: 580px;
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 24px 64px rgba(0,0,0,0.16), 0 4px 16px rgba(0,0,0,0.08);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: translateY(18px) scale(0.97);
      opacity: 0;
      pointer-events: none;
      transition: transform 0.32s cubic-bezier(0.34,1.2,0.64,1), opacity 0.22s ease;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    #acx-panel.acx-visible {
      transform: translateY(0) scale(1);
      opacity: 1;
      pointer-events: all;
    }

    .acx-header {
      background: #0a0a0a;
      padding: 16px 18px 15px;
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }
    .acx-header-avatar {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #1c1c1c;
      border: 1.5px solid rgba(245,230,66,0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      overflow: hidden;
    }
    .acx-header-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .acx-header-info { flex: 1; min-width: 0; }
    .acx-header-name {
      color: #fff;
      font-size: 13.5px;
      font-weight: 600;
      letter-spacing: -0.25px;
      line-height: 1.2;
      font-family: 'Inter', sans-serif;
    }
    .acx-header-status {
      display: flex;
      align-items: center;
      gap: 5px;
      margin-top: 2px;
    }
    .acx-status-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #22c55e;
      flex-shrink: 0;
      animation: acx-pulse 2.4s ease-in-out infinite;
    }
    @keyframes acx-pulse {
      0%, 100% { opacity: 1; }
      50%       { opacity: 0.45; }
    }
    .acx-header-status-text {
      color: rgba(255,255,255,0.45);
      font-size: 11px;
      font-weight: 400;
      font-family: 'Inter', sans-serif;
    }
    .acx-close-btn {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: rgba(255,255,255,0.08);
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(255,255,255,0.6);
      transition: background 0.15s ease, color 0.15s ease;
      flex-shrink: 0;
      padding: 0;
    }
    .acx-close-btn:hover {
      background: rgba(255,255,255,0.16);
      color: #fff;
    }

    .acx-messages {
      flex: 1;
      overflow-y: auto;
      padding: 18px 14px 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      scroll-behavior: smooth;
    }
    .acx-messages::-webkit-scrollbar { width: 4px; }
    .acx-messages::-webkit-scrollbar-track { background: transparent; }
    .acx-messages::-webkit-scrollbar-thumb { background: #e0e0e0; border-radius: 2px; }

    .acx-msg {
      display: flex;
      gap: 8px;
      animation: acx-msg-in 0.28s cubic-bezier(0.34,1.2,0.64,1) both;
    }
    @keyframes acx-msg-in {
      from { opacity: 0; transform: translateY(10px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .acx-msg.acx-msg-user { flex-direction: row-reverse; }

    .acx-msg-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #ebebeb;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 10px;
      font-weight: 800;
      color: #888;
      flex-shrink: 0;
      margin-top: 2px;
      font-family: 'Inter', sans-serif;
      overflow: hidden;
    }
    .acx-msg-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .acx-ai-avatar {
      background: #0a0a0a !important;
      color: #f5e642 !important;
      font-size: 9px !important;
      letter-spacing: -0.4px !important;
    }

    .acx-bubble {
      max-width: 80%;
      padding: 10px 14px;
      border-radius: 16px;
      font-size: 13.5px;
      line-height: 1.65;
      letter-spacing: -0.1px;
      word-break: break-word;
      font-family: 'Inter', sans-serif;
    }
    .acx-msg-ai .acx-bubble {
      background: #f2f2f2;
      color: #1a1a1a;
      border-bottom-left-radius: 4px;
    }
    .acx-msg-user .acx-bubble {
      background: #0a0a0a;
      color: #fff;
      border-bottom-right-radius: 4px;
    }

    .acx-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      padding-left: 36px;
      animation: acx-msg-in 0.32s cubic-bezier(0.34,1.2,0.64,1) 0.1s both;
    }
    .acx-chip {
      padding: 7px 14px;
      border-radius: 100px;
      border: 1.5px solid #d0d0d0;
      background: #fff;
      color: #1a1a1a;
      font-size: 12.5px;
      font-weight: 500;
      cursor: pointer;
      font-family: 'Inter', sans-serif;
      letter-spacing: -0.1px;
      transition: all 0.18s cubic-bezier(0.34,1.4,0.64,1);
      white-space: nowrap;
      line-height: 1;
    }
    .acx-chip:hover {
      background: #0a0a0a;
      color: #fff;
      border-color: #0a0a0a;
      transform: translateY(-1.5px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.14);
    }
    .acx-chip:active { transform: translateY(0); }

    .acx-typing-bubble {
      background: #f2f2f2;
      border-radius: 16px;
      border-bottom-left-radius: 4px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .acx-typing-bubble span {
      width: 6px;
      height: 6px;
      background: #bbb;
      border-radius: 50%;
      display: inline-block;
      animation: acx-dot 1.3s ease-in-out infinite;
    }
    .acx-typing-bubble span:nth-child(2) { animation-delay: 0.16s; }
    .acx-typing-bubble span:nth-child(3) { animation-delay: 0.32s; }
    @keyframes acx-dot {
      0%, 60%, 100% { transform: translateY(0); opacity: 0.45; }
      30%            { transform: translateY(-5px); opacity: 1; }
    }

    .acx-input-area {
      padding: 10px 12px 12px;
      border-top: 1px solid #f0f0f0;
      display: flex;
      align-items: flex-end;
      gap: 8px;
      flex-shrink: 0;
      background: #fff;
    }
    .acx-input {
      flex: 1;
      resize: none;
      border: 1.5px solid #e8e8e8;
      border-radius: 12px;
      padding: 9px 12px;
      font-size: 13.5px;
      font-family: 'Inter', sans-serif;
      color: #1a1a1a;
      line-height: 1.55;
      max-height: 100px;
      min-height: 38px;
      outline: none;
      transition: border-color 0.15s ease;
      background: #fafafa;
      letter-spacing: -0.1px;
      overflow-y: auto;
      box-sizing: border-box;
    }
    .acx-input:focus {
      border-color: #1a1a1a;
      background: #fff;
    }
    .acx-input::placeholder { color: #b8b8b8; }

    .acx-send-btn {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: #0a0a0a;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      flex-shrink: 0;
      transition: transform 0.18s cubic-bezier(0.34,1.4,0.64,1), background 0.15s ease;
      padding: 0;
    }
    .acx-send-btn:hover:not(:disabled) {
      background: #2c2c2c;
      transform: scale(1.1);
    }
    .acx-send-btn:active:not(:disabled) { transform: scale(0.93); }
    .acx-send-btn:disabled { opacity: 0.3; cursor: not-allowed; }

    .acx-footer {
      padding: 6px 16px 8px;
      text-align: center;
      font-size: 10px;
      color: #ccc;
      letter-spacing: 0.15px;
      background: #fff;
      border-top: 1px solid #f5f5f5;
      font-family: 'Inter', sans-serif;
    }
    .acx-footer a {
      color: #aaa;
      text-decoration: none;
      font-weight: 500;
    }
    .acx-footer a:hover { color: #0a0a0a; }

    @media (max-width: 480px) {
      #acx-panel {
        bottom: 0;
        right: 0;
        width: 100%;
        height: 100dvh;
        height: 100vh;
        border-radius: 0;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
      }
      #acx-launcher { bottom: 18px; right: 18px; }
    }
  `;

  const styleEl = document.createElement('style');
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  /* ── State ── */
  let threadId = null;
  let isOpen = false;
  let isLoading = false;

  /* ── Build DOM ── */
  function buildWidget() {
    const launcher = document.createElement('button');
    launcher.id = 'acx-launcher';
    launcher.setAttribute('aria-label', 'Chat with Referan');
    launcher.innerHTML = `
      <svg class="acx-icon-chat" width="22" height="22" viewBox="0 0 24 24" fill="none"
           stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
      </svg>
      <svg class="acx-icon-close" width="17" height="17" viewBox="0 0 24 24" fill="none"
           stroke="white" stroke-width="2.5" stroke-linecap="round">
        <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
      </svg>`;

    const panel = document.createElement('div');
    panel.id = 'acx-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Referan Chat');
    panel.innerHTML = `
      <div class="acx-header">
        <div class="acx-header-avatar"><img src="https://acantix.com/logo-chatbot.jpeg" alt="Referan"></div>
        <div class="acx-header-info">
          <div class="acx-header-name">Referan</div>
          <div class="acx-header-status">
            <div class="acx-status-dot"></div>
            <span class="acx-header-status-text">Online</span>
          </div>
        </div>
        <button class="acx-close-btn" aria-label="Close chat">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
            <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>
      <div class="acx-messages" id="acx-messages"></div>
      <div class="acx-input-area">
        <textarea class="acx-input" id="acx-input" placeholder="Type a message…" rows="1"></textarea>
        <button class="acx-send-btn" id="acx-send" aria-label="Send">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="22" y1="2" x2="11" y2="13"/>
            <polygon points="22 2 15 22 11 13 2 9 22 2"/>
          </svg>
        </button>
      </div>
      <div class="acx-footer">Powered by <a href="https://acantix.com" target="_blank" rel="noopener">Referan</a></div>`;

    document.body.appendChild(launcher);
    document.body.appendChild(panel);

    launcher.addEventListener('click', toggle);
    panel.querySelector('.acx-close-btn').addEventListener('click', closeChat);

    const input = panel.querySelector('#acx-input');
    const sendBtn = panel.querySelector('#acx-send');

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSend(); }
    });
    input.addEventListener('input', function () {
      input.style.height = 'auto';
      input.style.height = Math.min(input.scrollHeight, 100) + 'px';
    });
    sendBtn.addEventListener('click', handleSend);
  }

  /* ── Open / close ── */
  function toggle() { isOpen ? closeChat() : openChat(); }

  function openChat() {
    if (isOpen) return;
    isOpen = true;
    document.getElementById('acx-launcher').classList.add('acx-open');
    document.getElementById('acx-panel').classList.add('acx-visible');
    if (!threadId) initSession();
    setTimeout(function () {
      var inp = document.getElementById('acx-input');
      if (inp) inp.focus();
    }, 340);
  }

  function closeChat() {
    if (!isOpen) return;
    isOpen = false;
    document.getElementById('acx-launcher').classList.remove('acx-open');
    document.getElementById('acx-panel').classList.remove('acx-visible');
  }

  /* ── Session ── */
  async function initSession() {
    showWelcome();
    try {
      const res = await fetch(API_BASE + '/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
      });
      const data = await res.json();
      threadId = data.thread_id;
    } catch (e) {
      console.error('[Acantix Chat] Session start failed:', e);
    }
  }

  /* ── Welcome ── */
  function showWelcome() {
    var msgs = document.getElementById('acx-messages');
    if (!msgs || msgs.children.length > 0) return;

    msgs.appendChild(makeAIBubble('What are you trying to build or improve today?'));

    var chips = document.createElement('div');
    chips.className = 'acx-chips';
    chips.id = 'acx-chips';

    ['Build an AI product', 'Improve my tech stack', 'Scale my team', 'Book a consultation']
      .forEach(function (label) {
        var btn = document.createElement('button');
        btn.className = 'acx-chip';
        btn.textContent = label;
        btn.addEventListener('click', function () {
          var c = document.getElementById('acx-chips');
          if (c) c.remove();
          sendMessage(label);
        });
        chips.appendChild(btn);
      });

    msgs.appendChild(chips);
  }

  /* ── Bubble builders ── */
  function makeAIBubble(text) {
    var row = document.createElement('div');
    row.className = 'acx-msg acx-msg-ai';
    row.innerHTML =
      '<div class="acx-msg-avatar acx-ai-avatar"><img src="https://acantix.com/logo-chatbot.jpeg" alt=""></div>' +
      '<div class="acx-bubble">' + renderText(text) + '</div>';
    return row;
  }

  function makeUserBubble(text) {
    var row = document.createElement('div');
    row.className = 'acx-msg acx-msg-user';
    row.innerHTML = '<div class="acx-bubble">' + escHtml(text) + '</div>';
    return row;
  }

  function showTyping() {
    var msgs = document.getElementById('acx-messages');
    var row = document.createElement('div');
    row.className = 'acx-msg acx-msg-ai';
    row.id = 'acx-typing';
    row.innerHTML =
      '<div class="acx-msg-avatar acx-ai-avatar"><img src="https://acantix.com/logo-chatbot.jpeg" alt=""></div>' +
      '<div class="acx-typing-bubble"><span></span><span></span><span></span></div>';
    msgs.appendChild(row);
    scrollBottom();
  }

  function removeTyping() {
    var t = document.getElementById('acx-typing');
    if (t) t.remove();
  }

  function scrollBottom() {
    var msgs = document.getElementById('acx-messages');
    if (msgs) requestAnimationFrame(function () { msgs.scrollTop = msgs.scrollHeight; });
  }

  /* ── Send ── */
  function handleSend() {
    var input = document.getElementById('acx-input');
    if (!input || isLoading) return;
    var text = input.value.trim();
    if (!text) return;
    input.value = '';
    input.style.height = 'auto';
    var chips = document.getElementById('acx-chips');
    if (chips) chips.remove();
    sendMessage(text);
  }

  async function sendMessage(text) {
    if (isLoading) return;
    var msgs = document.getElementById('acx-messages');
    var sendBtn = document.getElementById('acx-send');
    var input = document.getElementById('acx-input');

    msgs.appendChild(makeUserBubble(text));
    scrollBottom();

    isLoading = true;
    if (sendBtn) sendBtn.disabled = true;
    if (input) input.disabled = true;
    showTyping();

    try {
      if (!threadId) await new Promise(function (r) { setTimeout(r, 1800); });
      if (!threadId) throw new Error('no session');

      var res = await fetch(API_BASE + '/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ thread_id: threadId, message: text })
      });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      var data = await res.json();

      removeTyping();
      msgs.appendChild(makeAIBubble(data.response));
      scrollBottom();
    } catch (e) {
      console.error('[Acantix Chat]', e);
      removeTyping();
      msgs.appendChild(makeAIBubble(
        'Sorry, I couldn\'t connect right now. Please try again or email us at hello@acantix.com.'
      ));
      scrollBottom();
    } finally {
      isLoading = false;
      if (sendBtn) sendBtn.disabled = false;
      if (input) { input.disabled = false; input.focus(); }
    }
  }

  /* ── Helpers ── */
  function escHtml(str) {
    var d = document.createElement('div');
    d.appendChild(document.createTextNode(str));
    return d.innerHTML;
  }

  function renderText(str) {
    return escHtml(str)
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br>');
  }

  /* ── Global API ── */
  window.acantixChat = { open: openChat, close: closeChat, toggle: toggle };

  /* ── Init ── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildWidget);
  } else {
    buildWidget();
  }
})();
