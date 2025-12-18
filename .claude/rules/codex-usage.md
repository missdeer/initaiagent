# Codex Tool Usage

The Codex MCP provides a `codex` tool for **debugging, complex problem solving, and code review**.

## Role

- Advisory only, not primary implementer
- Consult for difficult/complex problems across all technologies
- **Primary code reviewer** in Phase 5 audit loop
- Output is reference, Claude Code makes final implementation

## Rules

- Store returned `SESSION_ID` for conversation continuity
- Use `sandbox="read-only"` - Codex must NOT modify code directly
- Request unified diff patches only

## Strengths

- Debugging and issue localization in complex codebases
- Algorithm optimization and complex logic analysis
- Code review and edge case identification
