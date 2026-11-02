## 2024-11-02 - Prevent Server-Side Request Forgery and Credential Leak in Extension
**Vulnerability:** The browser extension read a `callbackUrl` directly from the URL parameters of `music.youtube.com` without validation and blindly posted the user's sensitive authentication cookies (including `SAPISID`) to it.
**Learning:** Browser extensions processing callback URLs from query parameters act as cross-origin bridges and can easily fall prey to SSRF or data exfiltration if the target origin is not explicitly whitelisted or matched against user configurations.
**Prevention:** Always validate target origins of callback URLs against a known trusted list or user preferences before dispatching sensitive credentials via `fetch` or `XMLHttpRequest`.
