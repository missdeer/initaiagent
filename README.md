# initaiagent

Initializes AI coding agent configuration files - CLAUDE.md/AGENTS.md/GEMINI.md.

## How to Use

```bash
git clone https://github.com/missdeer/initaiagent.git
alias initaiagent="$PWD/initaiagent/initaiagent.py"
cd /your/project/path
initaiagent
```

### Supported Commandline Options

```bash
$ initaiagent.py -h
usage: initaiagent.py [-h] [-d DIRECTORY] [-A] [-G] [-O]

Initialize CLAUDE.md, GEMINI.md, and AGENTS.md files

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Working directory path (default: current working directory)
  -A, --claude          Enable creating CLAUDE.md and insert template content
  -G, --gemini          Enable creating GEMINI.md and insert template content
  -O, --codex           Enable creating AGENTS.md and insert template content

Examples:
  initaiagent.py                           # Process all files in current directory
  initaiagent.py -d /path/to/dir            # Process all files in specified directory
  initaiagent.py -A                         # Only process CLAUDE.md
  initaiagent.py -G -O                      # Only process GEMINI.md and AGENTS.md
  initaiagent.py -A -G                      # Only process CLAUDE.md and GEMINI.md
  initaiagent.py -h                          # Show this help message and exit

Note:
  By default (no options specified), all three files (CLAUDE.md, GEMINI.md, AGENTS.md) are processed.
  If any specific flag (-A, -G, -O) is specified, only the specified files are processed.
```        


## What It Does

Inserts prompts from the `template` directory into your project's agent configuration files. If a configuration file (CLAUDE.md/AGENTS.md/GEMINI.md) doesn't exist in the working directory, it will skip copying content. Therefore, you need to run `/init` with `claude`/`codex`/`gemini` to ensure the configuration file exists before using this script.