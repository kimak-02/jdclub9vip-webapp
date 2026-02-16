const tg = window.Telegram?.WebApp;

if (tg) {
  tg.ready();
  tg.expand();
}

// ✅ TUKAR LINK WEBSITE KAU KAT SINI
const WEBSITE_URL = "https://jdclub9vip.live/RF3760A863A"; // <-- tukar

const openLink = (url) => {
  if (tg) tg.openLink(url);
  else window.open(url, "_blank");
};

// Button REGISTER HERE (id="register")
const registerBtn = document.getElementById("register");
if (registerBtn) {
  registerBtn.addEventListener("click", () => {
    window.location.href = WEBSITE_URL;
  });
}

// Tiles/menu (data-action="promo" etc.)
document.querySelectorAll(".tile").forEach((btn) => {
  btn.addEventListener("click", () => {
    const action = btn.dataset.action;
    if (tg) tg.sendData(action);
    else alert("Action: " + action);
  });
});
