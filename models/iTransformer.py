"""
models/iTransformer.py
======================
Compatibility shim — re-exports the iTransformer model from models/itransformer.py
and adds the `Model` alias expected by itransformer_agent.py.

  from models.iTransformer import Model as iTransformer   ← agent uses this
"""

from .itransformer import (       # relative import — works regardless of sys.path
    iTransformer,
    iTransformerBlock,
    FeedForward,
    VariablePositionalEncoding,
)

# Alias so the agent's `from models.iTransformer import Model` works
Model = iTransformer

__all__ = ["Model", "iTransformer", "iTransformerBlock",
           "FeedForward", "VariablePositionalEncoding"]
