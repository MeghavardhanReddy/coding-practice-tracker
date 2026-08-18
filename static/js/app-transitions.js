(function () {
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const overlay = document.querySelector("[data-app-transition-overlay]");
    const overlayLabel = document.querySelector("[data-app-transition-label]");

    if (reducedMotion) {
        return;
    }

    window.addEventListener("pageshow", function () {
        document.body.classList.remove("page-is-leaving");
        if (overlay) {
            overlay.classList.remove("is-active", "is-exit");
            overlay.setAttribute("aria-hidden", "true");
        }
    });

    function isSkippableLink(link, event) {
        if (!link || event.defaultPrevented) {
            return true;
        }

        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) {
            return true;
        }

        if (link.target && link.target !== "_self") {
            return true;
        }

        if (link.hasAttribute("download") || link.hasAttribute("onclick") || link.dataset.noTransition === "true") {
            return true;
        }

        const href = link.getAttribute("href");
        if (!href || href.startsWith("#")) {
            return true;
        }

        if (/^(mailto:|tel:|javascript:)/i.test(href)) {
            return true;
        }

        const nextUrl = new URL(href, window.location.href);
        if (nextUrl.origin !== window.location.origin) {
            return true;
        }

        return nextUrl.pathname === window.location.pathname &&
            nextUrl.search === window.location.search &&
            nextUrl.hash;
    }

    function showExitOverlay(label) {
        if (!overlay) {
            return;
        }

        if (overlayLabel && label) {
            overlayLabel.textContent = label;
        }

        overlay.classList.add("is-active", "is-exit");
        overlay.setAttribute("aria-hidden", "false");
    }

    document.addEventListener("click", function (event) {
        const link = event.target.closest("a[href]");

        if (isSkippableLink(link, event)) {
            return;
        }

        if (link.classList.contains("js-logout-transition")) {
            event.preventDefault();
            showExitOverlay(link.dataset.transitionLabel || "SESSION CLOSING...");
            window.setTimeout(function () {
                window.location.href = link.href;
            }, 700);
            return;
        }

        event.preventDefault();
        document.body.classList.add("page-is-leaving");

        window.setTimeout(function () {
            window.location.href = link.href;
        }, 220);
    });
})();
