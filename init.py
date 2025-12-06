#!/usr/bin/env python3
"""
Initialize AI agent configuration files (CLAUDE.md, GEMINI.md, AGENTS.md).

This script checks if the AI agent markdown files exist in the specified or current
working directory. If they exist, it inserts template content from the template/
directory at the front of each file.

Usage:
    python3 init.py                    # Process all files in current directory
    python3 init.py -d /path/to/dir    # Process all files in specified directory
    python3 init.py -A                 # Only process CLAUDE.md
    python3 init.py -G -O              # Only process GEMINI.md and AGENTS.md
"""

import argparse  # Command-line argument parsing
import os        # Operating system interface for path operations
import sys       # System-specific parameters and functions

def remove_first_h1_and_paragraphs(content):
    """
    Remove content before the first H2 heading (## title) from markdown content.
    
    This function finds the first level-2 heading (starting with '##') and removes
    all content before it, including the first H1 heading and any paragraphs.
    
    Args:
        content (str): The markdown content to process
    
    Returns:
        str: The content with everything before the first H2 removed
    """
    if not content:
        return content
    
    lines = content.split('\n')
    
    # Find the first line that starts with '##'
    for i, line in enumerate(lines):
        if line.startswith('##'):
            # Return all content from the first H2 onwards
            return '\n'.join(lines[i:])
    
    # If no H2 found, return empty string
    return ''

def insert_template_content(target_file, template_file):
    """
    Insert template content at the front of target file.
    
    This function reads the template file from the template/ directory and prepends
    its content to the target file. Before insertion, it removes the first H1 heading
    and its paragraph content from the target file (if it exists), since the template
    will provide the H1 heading and content. If the target file already has remaining
    content after removal, a separator (---) is added between the template content
    and existing content.
    
    Args:
        target_file (str): Path to the target file where template content will be inserted
        template_file (str): Name of the template file in the template/ directory
                             (e.g., "CLAUDE.md", "GEMINI.md", "AGENTS.md")
    
    Returns:
        None: The function modifies the target file in place
    
    Note:
        - If the template file doesn't exist, a warning is printed and the function returns
        - If the target file doesn't exist, only template content is written
        - The first H1 heading and its paragraphs are removed from existing content before insertion
        - If both exist, template content is prepended with a separator
    """
    # Get the directory where this script is located
    # This allows the script to find the template/ directory regardless of where
    # the script is called from
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the template file
    template_path = os.path.join(script_dir, "template", template_file)
    
    # Check if the template file exists before proceeding
    if not os.path.exists(template_path):
        print(f"Warning: Template file {template_path} not found, skipping insertion.", file=sys.stderr)
        return
    
    try:
        # Read the template content from the template file
        # Using UTF-8 encoding to handle international characters
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Read existing content from the target file if it exists
        # Initialize as empty string if file doesn't exist yet
        existing_content = ""
        if os.path.exists(target_file):
            with open(target_file, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            # Remove the first H1 heading and its paragraph content
            # since the template will provide the H1 and content
            existing_content = remove_first_h1_and_paragraphs(existing_content)
            # Strip leading/trailing whitespace after removal
            existing_content = existing_content.strip()
        
        # Combine template content with existing content
        # Start with template content
        combined_content = template_content
        if existing_content:
            # If there's existing content, add a separator between template and existing
            # Ensure template content ends with a newline before adding separator
            if not template_content.endswith('\n'):
                combined_content += '\n'
            # Add a markdown horizontal rule as separator for visual clarity
            combined_content += '\n---\n\n'
            # Append the existing content after the separator
            combined_content += existing_content
        
        # Write the combined content back to the target file
        # This overwrites the file with template content at the front
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(combined_content)
        
        # Print success message with just the filename (not full path) for cleaner output
        print(f"Template content inserted into {os.path.basename(target_file)}")
    except Exception as e:
        # Catch any errors during file operations (permission errors, disk full, etc.)
        print(f"Error inserting template content: {e}", file=sys.stderr)

def ensure_claude_md(work_dir=None):
    """
    Check if CLAUDE.md exists in specified directory.
    
    This function checks if CLAUDE.md exists in the target directory. If it exists,
    it inserts template content from template/CLAUDE.md at the front of the file.
    
    Args:
        work_dir (str, optional): Directory path where CLAUDE.md should be checked.
                                 If None, uses the current working directory.
                                 Defaults to None.
    
    Returns:
        None: The function modifies files in the specified directory
    """
    # Determine the working directory to use
    # If work_dir is provided, convert it to absolute path
    # Otherwise, use the current working directory
    cwd = os.path.abspath(work_dir) if work_dir else os.getcwd()
    # Construct the full path to CLAUDE.md in the target directory
    claude_md_path = os.path.join(cwd, "CLAUDE.md")
    
    # Check if CLAUDE.md exists in the target directory
    if not os.path.exists(claude_md_path):
        # File doesn't exist, just print a message
        print(f"CLAUDE.md not found in {cwd}")
        return
    
    # Insert template content at the front of the file
    if os.path.exists(claude_md_path):
        insert_template_content(claude_md_path, "CLAUDE.md")

def ensure_gemini_md(work_dir=None):
    """
    Check if GEMINI.md exists in specified directory.
    
    This function checks if GEMINI.md exists in the target directory. If it exists,
    it inserts template content from template/GEMINI.md at the front of the file.
    
    Args:
        work_dir (str, optional): Directory path where GEMINI.md should be checked.
                                 If None, uses the current working directory.
                                 Defaults to None.
    
    Returns:
        None: The function modifies files in the specified directory
    """
    # Determine the working directory to use
    # If work_dir is provided, convert it to absolute path
    # Otherwise, use the current working directory
    cwd = os.path.abspath(work_dir) if work_dir else os.getcwd()
    # Construct the full path to GEMINI.md in the target directory
    gemini_md_path = os.path.join(cwd, "GEMINI.md")
    
    # Check if GEMINI.md exists in the target directory
    if not os.path.exists(gemini_md_path):
        # File doesn't exist, just print a message
        print(f"GEMINI.md not found in {cwd}")
        return
    
    # Insert template content at the front of the file
    if os.path.exists(gemini_md_path):
        insert_template_content(gemini_md_path, "GEMINI.md")

def ensure_agent_md(work_dir=None):
    """
    Check if AGENTS.md exists in specified directory.
    
    This function checks if AGENTS.md exists in the target directory. If it exists,
    it inserts template content from template/AGENTS.md at the front of the file.
    
    Args:
        work_dir (str, optional): Directory path where AGENTS.md should be checked.
                                 If None, uses the current working directory.
                                 Defaults to None.
    
    Returns:
        None: The function modifies files in the specified directory
    """
    # Determine the working directory to use
    # If work_dir is provided, convert it to absolute path
    # Otherwise, use the current working directory
    cwd = os.path.abspath(work_dir) if work_dir else os.getcwd()
    # Construct the full path to AGENTS.md in the target directory
    agent_md_path = os.path.join(cwd, "AGENTS.md")
    
    # Check if AGENTS.md exists in the target directory
    if not os.path.exists(agent_md_path):
        # File doesn't exist, just print a message
        print(f"AGENTS.md not found in {cwd}")
        return
    
    # Insert template content at the front of the file
    if os.path.exists(agent_md_path):
        insert_template_content(agent_md_path, "AGENTS.md")

def main():
    """
    Main entry point for the script.
    
    Parses command-line arguments and orchestrates the creation and template insertion
    for the AI agent configuration files based on user options.
    
    Command-line options:
        -d, --directory: Specify working directory (default: current directory)
        -A, --claude: Enable processing CLAUDE.md
        -G, --gemini: Enable processing GEMINI.md
        -O, --codex: Enable processing AGENTS.md
    
    Behavior:
        - If no specific option (-A, -G, -O) is specified, all files are processed (default)
        - If any specific option is specified, only the specified files are processed
    
    Returns:
        None: The function calls other functions to perform file operations
    
    Raises:
        SystemExit: Exits with code 1 if the specified directory doesn't exist
    """
    # Create argument parser with description and help information
    # add_help=True enables -h/--help option (this is the default)
    # epilog provides additional information shown after the argument descriptions
    # formatter_class=RawDescriptionHelpFormatter preserves formatting in epilog
    parser = argparse.ArgumentParser(
        description="Initialize CLAUDE.md, GEMINI.md, and AGENTS.md files",
        epilog="""
Examples:
  %(prog)s                           # Process all files in current directory
  %(prog)s -d /path/to/dir            # Process all files in specified directory
  %(prog)s -A                         # Only process CLAUDE.md
  %(prog)s -G -O                      # Only process GEMINI.md and AGENTS.md
  %(prog)s -A -G                      # Only process CLAUDE.md and GEMINI.md
  %(prog)s -h                          # Show this help message and exit

Note:
  By default (no options specified), all three files (CLAUDE.md, GEMINI.md, AGENTS.md) are processed.
  If any specific flag (-A, -G, -O) is specified, only the specified files are processed.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=True  # Explicitly enable -h/--help option (default is True)
    )
    # Note: argparse automatically provides -h/--help option when add_help=True
    # The help option displays the description, all argument help texts, and the epilog
    
    # Add command-line argument for specifying working directory
    # -d and --directory are aliases for the same option
    parser.add_argument(
        "-d", "--directory",
        type=str,
        default=None,
        help="Working directory path (default: current working directory)"
    )
    
    # Add command-line argument for enabling CLAUDE.md processing
    # -A and --claude are aliases for the same option
    # action="store_true" means the flag is False by default, True when specified
    parser.add_argument(
        "-A", "--claude",
        action="store_true",
        help="Enable creating CLAUDE.md and insert template content"
    )
    
    # Add command-line argument for enabling GEMINI.md processing
    # -G and --gemini are aliases for the same option
    parser.add_argument(
        "-G", "--gemini",
        action="store_true",
        help="Enable creating GEMINI.md and insert template content"
    )
    
    # Add command-line argument for enabling AGENTS.md processing
    # -O and --codex are aliases for the same option
    parser.add_argument(
        "-O", "--codex",
        action="store_true",
        help="Enable creating AGENTS.md and insert template content"
    )
    
    # Parse command-line arguments into a namespace object
    args = parser.parse_args()
    
    # Extract the working directory from parsed arguments
    work_dir = args.directory
    # Validate that the directory exists if one was specified
    if work_dir and not os.path.isdir(work_dir):
        print(f"Error: Directory '{work_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    # Determine which files to process based on command-line options
    # Logic:
    #   - If any specific option (-A, -G, -O) is specified, only process those files
    #   - If no specific option is specified, process all files (default behavior)
    has_specific_options = args.claude or args.gemini or args.codex
    
    if has_specific_options:
        # Only process files specified by command-line options
        if args.claude:
            ensure_claude_md(work_dir)
        if args.gemini:
            ensure_gemini_md(work_dir)
        if args.codex:
            ensure_agent_md(work_dir)
    else:
        # No specific options specified, process all files (default behavior)
        ensure_claude_md(work_dir)
        ensure_gemini_md(work_dir)
        ensure_agent_md(work_dir)

# Entry point: Only run main() if this script is executed directly
# This allows the script to be imported as a module without executing main()
# When imported, __name__ will be the module name, not "__main__"
if __name__ == "__main__":
    main()
