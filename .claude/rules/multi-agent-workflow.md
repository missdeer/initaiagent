# Multi-Agent Workflow

Three cooperating agents via MCP:
- **Claude Code**: orchestrator and final implementer
- **Codex**: debugging, complex problem solving, code review (`sandbox="read-only"`)
- **Gemini**: web front-end (HTML/CSS/JS) prototypes, architecture review, knowledge advisor

---

## Context Retrieval (Available at Any Phase)

**Tool**: Augment Context Engine (`mcp__augment-context-engine-mcp__codebase-retrieval`)

Use whenever context is needed:
1. Natural-language semantic queries (What/Where/How)
2. Do not answer based on assumptions
3. Recursive retrieval until context is complete
4. Ask clarifying questions if requirements remain ambiguous

**Forbidden**: `grep` / keyword search for initial context gathering.

---

## Phase 1: Analysis & Planning

**Tools**: Codex AND Gemini (dual-model)

**Step 1: Workload Assessment**
- Claude Code evaluates task complexity and scope
- Small/simple tasks: ask the user to confirm whether skip Step 2 to proceed directly to implementation
- Large/complex tasks: proceed to Step 2

**Step 2: Proposal Draft**
- Claude Code drafts implementation proposal with pseudocode
- Include: approach, affected files, potential risks
- Write all things down into files in `.claude/drafts` directory for review in next step

**Step 3: Dual Review Loop**
1. Send proposal files in `.claude/drafts` directory to both Gemini and Codex for review
2. Gemini: architecture validation, design feedback
3. Codex: logic verification, edge case analysis
4. Synthesize feedback, revise proposal
5. **Repeat until consensus reached among all three agents**

**Step 4: User Confirmation**
- Present final proposal to user
- Proceed only after user approval

## Phase 2: Prototyping

**Role assignment:**

| Agent | Responsibility | Technologies |
|-------|----------------|--------------|
| **Gemini** | Web prototypes, architecture review, knowledge advisor | HTML, CSS, JavaScript |
| **Claude Code** | All other code implementation | Qt/QML, C++, Swift/SwiftUI, Kotlin/Compose, Go, Rust, Python, Node.js |
| **Codex** | Debugging, complex problem solving | All (advisory role) |

**Workflow:**
- Web Frontend (HTML/CSS/JS): Request prototype from Gemini, refine yourself
- All Other Code: Implement directly, consult Codex for difficult problems
- Codex output is reference only, not final implementation

**Universal constraint**: Request `Unified Diff Patch` output only.

## Phase 3: Implementation

**Executor**: Claude (self)

1. Refactor prototype logic into production-grade code
2. No comments/docs unless necessary
3. Changes must stay within requirement boundaries
4. Review for side effects, fix any regressions

**Testing Requirements (for Rust, Go, Python, Node.js):**
- New code: add corresponding test cases
- Modified code: add new test cases; only modify existing tests if business logic changed
- Run all tests after changes, ensure 100% pass before proceeding

**Static Analysis (for C++/Qt):**
- Config files: `.clang-tidy`, `.clazy` in project root
- clang-tidy: `clang-tidy -p cmake-build <source_files>`
- clazy: `clazy-standalone -p cmake-build <source_files>` (reads `.clazy` config automatically)
- All checks must pass before proceeding to code review

## Phase 4: Audit & Delivery

**Step 0: Test Verification (for Rust, Go, Python, Node.js)**
- Run full test suite before code review
- All tests must pass; fix failures before proceeding

**Step 1: Codex Review Loop**
1. Ask Codex to use `git diff HEAD` to get local changes for review
2. Codex identifies issues: bugs, edge cases, style violations
3. Claude Code evaluates findings and applies fixes
4. **Repeat until Codex finds no new issues**

**Step 2: Gemini Final Review**
1. After Codex loop completes, Ask Gemini to use `git diff HEAD` to get local changes for final review
2. If Gemini finds new issues:
   - Codex and Claude Code jointly evaluate whether fix is needed
   - If fix needed: return to Step 1 (Codex review loop)
   - If not needed: document reasoning, proceed to delivery
3. If no issues found: code is complete

**Delivery:**
- Always apply source code format when the modification is done
- Only deliver to user after both review stages pass
- Include summary of changes and review iterations if relevant

## Critical Principles

- Never blindly trust Codex/Gemini - think independently
- Prototypes are logical reference only; rewrite for production
- Targeted changes only - never affect existing functionality
