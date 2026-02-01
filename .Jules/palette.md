# Palette's Journal - Critical UX Learnings

## 2025-05-15 - [Semantic Buttons for Toggles]
**Learning:** In static HTML projects, interactive elements are often implemented using `div` or `span` with `cursor-pointer`. This breaks keyboard navigation and screen reader expectations.
**Action:** Always convert non-semantic interactive elements to `<button>` tags, especially for icon-only toggles, and ensure they have an explicit `type="button"` to avoid form submission.
