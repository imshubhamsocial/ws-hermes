---
name: three-js-controls-implementation
description: "Three.js PointerLockControls fix. Import from examples/jsm."
---

# Three.js Controls Implementation Workflow

When working with Three.js, especially regarding movement or controls like `PointerLockControls`, ensure the required control class is correctly imported into your script. The `PointerLockControls` is not globally available; it must be imported from the specific module path within the Three.js examples directory.

## Procedure
1. **Locate Usage**: Search the relevant client JavaScript file (e.g., `main.js`) for the instantiation of `new PointerLockControls(...)`.
2. **Verify Dependency**: Check your existing imports to confirm that `PointerLockControls` is not already imported.
3. **Implement Correct Import**: Add the explicit ES module import at the top of the file:
   `import { PointerLockControls } from "three/examples/jsm/controls/PointerLockControls.js";`
4. **Apply Patch**: Use `write_file` or `patch` to inject the import statement and verify the fix using a targeted browser audit tool (like Playwright) to ensure the runtime error is resolved.

## Pitfalls
*   **Assuming Global Scope**: Never assume `PointerLockControls` is globally defined. In modern ES module setups, external components like this must be explicitly imported from their specific source path.
*   **Incorrect Path**: Do not try importing from the main `three` package. The control modules reside in `three/examples/jsm/controls/`.
