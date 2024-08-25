let buttons = document.querySelectorAll('.btn-outline-info');

buttons.forEach(button => {
    let text = button.textContent;
    button.innerHTML = "";

    for (let i = 0; i < text.length; i++) {
        let span = document.createElement('span');
        span.textContent = text[i] === ' ' ? '\u00A0' : text[i];
        button.appendChild(span);
    }

    let spans = button.querySelectorAll("span");

    button.addEventListener("mouseenter", () => {
        spans.forEach((span, index) => {
            setTimeout(() => {
                span.classList.add('hover');
            }, index * 50);
        });
    });

    button.addEventListener("mouseleave", () => {
        spans.forEach((span, index) => {
            setTimeout(() => {
                span.classList.remove('hover');
            }, index * 50);
        });
    });
});