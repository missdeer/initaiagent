# CLAUDE 

## Workflow

- **MUST** follow multi-agent-workflow
- carefully read and understand rules defined in `.claude/rules` directory and follow them strictly

---

## File editing on Windows (CRITICAL FIX)

**ALWAYS use RELATIVE paths** for Read and Edit tools:

✅ CORRECT:
- Read("src/components/Button.tsx")
- Edit("src/components/Button.tsx", ...)
- Read("config/settings.json")
- Edit("config/settings.json", ...)

❌ INCORRECT:
- Read("C:/Users/.../src/components/Button.tsx")
- Edit("C:/Users/.../src/components/Button.tsx", ...)

**Rules:**
1. Use paths relative to your working directory
2. Use the SAME exact path in Read and Edit
3. Avoid absolute paths with forward slashes

**If error persists:** Re-read with the SAME relative path.

---
