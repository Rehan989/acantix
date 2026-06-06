(function () {
  'use strict';

  const API_BASE = 'https://restaurants-web-chatbot.onrender.com';

  let threadId = null;
  let isOpen = false;
  let isLoading = false;

  /* ── DOM build ── */
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
        <div class="acx-header-avatar"><img src="logo-chatbot.jpeg" alt="Referan"></div>
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
      <div class="acx-footer">Powered by <strong>Referan</strong></div>`;

    document.body.appendChild(launcher);
    document.body.appendChild(panel);

    launcher.addEventListener('click', toggle);
    panel.querySelector('.acx-close-btn').addEventListener('click', closeChat);

    const input = panel.querySelector('#acx-input');
    const sendBtn = panel.querySelector('#acx-send');

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSend();
      }
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
      var input = document.getElementById('acx-input');
      if (input) input.focus();
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

  /* ── Welcome screen ── */
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

  /* ── Message builders ── */
  function makeAIBubble(text) {
    var row = document.createElement('div');
    row.className = 'acx-msg acx-msg-ai';
    row.innerHTML =
      '<div class="acx-msg-avatar acx-ai-avatar">AI</div>' +
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
      '<div class="acx-msg-avatar acx-ai-avatar">AI</div>' +
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

  /* ── Send flow ── */
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
      if (!threadId) {
        await new Promise(function (r) { setTimeout(r, 1800); });
      }
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
        "Sorry, I couldn't connect right now. Please try again or email us at hello@acantix.com."
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
