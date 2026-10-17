"""Workspace isolation and verification for ProgravityBench."""
import os
import shutil
from pathlib import Path
from typing import Dict, Any

def create_isolated_workspace(base_repo: Path, target_dir: Path, config: str) -> Path:
    """Create a pristine copy of the repo configured for the target scenario."""
    if target_dir.exists():
        shutil.rmtree(target_dir)
    
    # Simple copy for now; in production use `git clone --local` or worktree
    shutil.copytree(base_repo, target_dir, ignore=shutil.ignore_patterns('.git', 'benchmarks/results'))
    
    # Apply configuration
    if config == "BASELINE" or config == "CLAUDE_REFERENCE":
        # Remove any Progravity skills or hooks to prevent contamination
        remove_progravity(target_dir)
    elif config == "PROGRAVITY_CORE":
        # Keep portable skill, remove native hooks
        remove_native_hooks(target_dir)
    elif config == "PROGRAVITY_NATIVE":
        # Keep everything
        pass
        
    return target_dir

def remove_progravity(workspace: Path):
    """Remove all Progravity traces from the workspace."""
    for path in ["skills/progravity", ".agents/skills/progravity", "plugins/progravity-antigravity", ".github/workflows/progravity.yml", "plugin.json"]:
        p = workspace / path
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()

def remove_native_hooks(workspace: Path):
    """Remove native hooks but keep portable skill."""
    for path in ["plugins/progravity-antigravity", "plugin.json"]:
        p = workspace / path
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()

def verify_isolation(workspace: Path, config: str) -> bool:
    """Verify that the workspace matches the expected isolation level."""
    progravity_exists = (workspace / "skills/progravity").exists() or (workspace / ".agents/skills/progravity").exists()
    native_exists = (workspace / "plugins/progravity-antigravity").exists() or (workspace / "plugin.json").exists()
    
    if config == "BASELINE" or config == "CLAUDE_REFERENCE":
        if progravity_exists or native_exists:
            return False
    elif config == "PROGRAVITY_CORE":
        if not progravity_exists or native_exists:
            return False
    elif config == "PROGRAVITY_NATIVE":
        if not progravity_exists or not native_exists:
            return False
            
    return True
