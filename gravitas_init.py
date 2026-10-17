"""Backward-compatibility shim forwarding to progravity_init."""
import progravity_init
from progravity_init import *

# Explicitly re-export private helpers that tests might import
_copy_tree = progravity_init._copy_tree
_merge_json = progravity_init._merge_json
_ensure_agents_block = progravity_init._ensure_agents_block
