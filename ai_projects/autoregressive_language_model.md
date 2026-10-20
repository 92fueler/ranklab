# Small autoregressive language model

## Core project

Implement an autoregressive language model and train it on a Shakespeare text
dataset. The implementation must run end to end, from data loading through
training to generated text.

## Requirements to define

Choose and document the dataset version, tokenizer, model size, context length,
training budget, hardware, and train/validation split. These choices are not
fixed by the core project.

## Optional implementation directions

A small decoder-only Transformer is one possible implementation.

- Define tokenization and vocabulary construction.
- Construct batches with next-token targets.
- Use causal masking so predictions cannot attend to future tokens.
- Verify tensor shapes throughout embeddings, attention, and output projection.
- Explain residual connections, normalization, and positional information.
- Compare pre-normalization and post-normalization conceptually, or experimentally
  if the training budget supports a meaningful comparison.

Keep the model small enough for a reproducible end-to-end run on the selected
hardware rather than optimizing scale before correctness.

## Validation milestones

1. Run a small forward pass and verify the loss is finite.
2. Run a backward pass and confirm that intended parameters receive gradients.
3. Overfit a tiny batch to expose data, masking, or optimization bugs.
4. Train with a documented configuration and monitor validation loss separately.
5. Save and reload a checkpoint, then generate text.

Avoid train/validation leakage. Record the split, random seed, configuration,
and checkpoint format so another run can be compared fairly.

## Decoding questions

Implement a simple decoding method first. Additional methods are optional, but
explain how these differ:

- Greedy decoding.
- Beam search.
- Top-k sampling.
- Top-p sampling.

Distinguish search from sampling. Test generation independently of training,
including context-window handling, stopping conditions, and invalid decoding
parameters. If comparing methods, hold the model and prompts constant.

## Technical questions

- How does self-attention compute interactions between tokens?
- Why is causal masking necessary for next-token prediction?
- What role do positional embeddings or another positional scheme serve?
- How do pre-normalization and post-normalization change the computation?
- What do residual connections contribute?
- What can training and validation loss reveal that a few generated samples cannot?

## Deliverables

- A runnable implementation and documented data-loading procedure.
- A reproducible training configuration.
- Training and validation loss measurements.
- A saved checkpoint and a generation example.
- Tests or checks for batching, target alignment, tensor shapes, causal masking,
  checkpoint loading, and decoding.

## Related exercises

- [Technical communication and validation](../questions/technical_communication.md) covers separating design choices from measured evidence.
- [Code-review checklist](../questions/code_review_checklist.md) provides a systematic correctness and failure-mode review.
