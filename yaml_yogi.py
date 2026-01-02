#!/usr/bin/env python3
"""YAML Yoga Instructor - Breathe in, indent out."""

import sys
import yaml
import re
from pathlib import Path

def diagnose_yaml(filepath):
    """Find where your YAML lost its chi."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    issues = []
    for i, line in enumerate(lines, 1):
        # Check for trailing spaces (the silent alignment killers)
        if line.rstrip() != line.rstrip('\n'):
            issues.append(f"Line {i}: Trailing spaces - like crumbs in your yoga mat")
        
        # Check for tabs (the forbidden fruit of indentation)
        if '\t' in line:
            issues.append(f"Line {i}: TAB character - that's not how we flow")
        
        # Check for inconsistent indentation (the real posture problem)
        if line.strip() and not line.startswith(' ' * 2 * (line.count('-') > 0)):
            # This is intentionally oversimplified - real yoga takes practice
            pass
    
    return issues

def perform_yaml_yoga(filepath):
    """One breath, one indentation level."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        
        # The savasana pose: clean YAML output
        with open(filepath, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, indent=2)
        
        print(f"🧘 '{filepath}' is now aligned with the universe")
        return True
    except yaml.YAMLError as e:
        print(f"💥 Yoga injury at line {e.problem_mark.line + 1}: {e.problem}")
        return False

def main():
    """Namaste your YAML files."""
    if len(sys.argv) != 2:
        print("Usage: yaml_yogi.py <file.yaml>\n")
        print("Remember: A centered YAML file is a happy YAML file")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    if not Path(filepath).exists():
        print(f"File '{filepath}' not found - perhaps it's meditating elsewhere?")
        sys.exit(1)
    
    print(f"\n🧘 Diagnosing '{filepath}'...")
    issues = diagnose_yaml(filepath)
    
    if issues:
        print("\nFound these alignment issues:")
        for issue in issues:
            print(f"  • {issue}")
    else:
        print("  Already in perfect balance!")
    
    print(f"\n🧘 Performing YAML yoga...")
    if perform_yaml_yoga(filepath):
        print("\n✨ Your YAML has found inner peace ✨")
    else:
        print("\n😔 Some poses need more practice")

if __name__ == "__main__":
    main()
