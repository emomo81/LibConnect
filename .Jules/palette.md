## 2024-07-25 - Functional Accessibility for Toggles

**Learning:** A UI control, like a password visibility toggle, is only truly implemented when it's functional and accessible. The presence of an icon is not enough. The implementation must include the JavaScript logic to alter the state and, critically, an update to the ARIA label to reflect that state change for screen reader users. The label should describe the *action* the button will perform (e.g., "Show password"), not its current state.

**Action:** When implementing any toggle-like UI element, always ensure there is corresponding JavaScript that updates both the visual state (icon, text) and the ARIA label to clearly communicate the result of the user's next interaction.