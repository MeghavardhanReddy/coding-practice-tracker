(function () {
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const form = document.querySelector("[data-login-transition-form]");
    const overlay = document.querySelector("[data-login-transition-overlay]");
    const submitButton = document.querySelector("[data-login-submit]");

    if (!form || reducedMotion) {
        return;
    }

    form.addEventListener("submit", function (event) {
        if (form.dataset.motionSubmitted === "true") {
            return;
        }

        event.preventDefault();
        form.dataset.motionSubmitted = "true";
        form.classList.add("is-initializing");

        if (submitButton) {
            submitButton.disabled = true;
            submitButton.classList.add("is-loading");
            submitButton.innerHTML = '<i class="bi bi-cpu"></i> Initializing...';
        }

        if (overlay) {
            overlay.classList.add("is-active");
            overlay.setAttribute("aria-hidden", "false");
        }

        window.setTimeout(function () {
            form.submit();
        }, 820);
    });
})();
