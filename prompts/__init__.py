"""
Prompts package.
"""

from prompts.rag_prompt import build_rag_prompt
from prompts.wiki_prompt import build_wiki_prompt
from prompts.direct_prompt import build_direct_prompt

__all__ = [
    "build_rag_prompt",
    "build_wiki_prompt",
    "build_direct_prompt",
]
