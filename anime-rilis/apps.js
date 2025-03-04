function toggleMode() {
    const body = document.body;
    body.classList.toggle("dark");
    body.classList.toggle("light");
    document.querySelectorAll(".container, h2, .toggle-btn").forEach(el => {
        el.classList.toggle("dark");
        el.classList.toggle("light");
    });
    const btn = document.getElementById("toggleButton");
    if (body.classList.contains("dark")) {
        btn.innerHTML = '🌙 Mode Malam';
    } else {
        btn.innerHTML = '☀️ Mode Siang';
    }
}