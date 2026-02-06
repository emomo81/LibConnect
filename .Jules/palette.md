## 2025-05-14 - Interactive Elements using Divs
**Learning:** In this repository, interactive elements like password visibility toggles were implemented using `div` tags instead of `button` tags. This makes them inaccessible to keyboard users and screen readers, as they aren't focusable and lack semantic meaning.
**Action:** Always convert non-semantic interactive `div` or `span` elements to `<button>` elements and ensure they have descriptive `aria-label` attributes.
