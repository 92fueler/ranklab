# Video sampling and visual tokens

Separate media processing, dataset selection, and model representations.
State the task and architecture before claiming fewer tokens preserve information.

## 1. What does sampling discard?

A twelve-second video at 30 frames per second contains 360 frames. Sampling at
two frames per second retains 24 timestamps, not a guarantee that every action
remains visible. What if a contact event starts and ends between samples?

Compare uniform sampling, motion-based selection, scene-change detection, and
event-aware sampling. What reference annotations would measure missed events?
Could motion-based selection discard a meaningful stationary state, or select
irrelevant camera shake? How would a budget combine broad coverage with dense
sampling around suspected events?

Repeated frames can be redundant for object identity but essential for duration,
speed, causality, or evidence that a state persisted. Which task-dependent
definition of redundancy are you using?

## 2. Is a keyframe a key event?

No. A codec I-frame uses intra-frame coding; its placement is not a semantic
guarantee of an important action. Codec
dependencies and random-access behavior also vary by format and configuration.

How would seeking to convenient decoding points differ from selecting frames
that represent task-relevant events? Could a system decode from a suitable
access point but choose a different timestamp for the model?

Compare fixed-length, overlapping, scene-based, and action-based clips. Which
preserve preconditions and outcomes without leaking similar windows across
splits? Keep source-time mappings through clipping, resampling, and captioning.

## 3. What are patches, embeddings, and visual tokens?

A patch is a spatial subdivision of an image. An image encoder may transform
patches into feature vectors, or embeddings. A downstream model may consume
those vectors, projected or compressed representations, or discrete codes.
“Visual token” therefore needs an architecture-specific definition; it does not
necessarily mean an integer from a text tokenizer.

For a toy encoder with non-overlapping 14-by-14-pixel patches, a 224-by-224
image yields 256 patches. If each retained patch becomes one token, 24 frames
would supply 6,144 patch tokens before special tokens or other processing.
What changes with higher resolution, multiple crops, pooling, or a temporal
encoder? This arithmetic is a hypothetical budget, not a universal tokenizer.

Media decoding reconstructs image samples from an encoded file. Visual encoding
maps those samples into model representations. Neither is the same operation
as text tokenization. What artifact, datatype, and shape crosses each boundary?
Does the model ever generate images, or only text or actions?

## 4. Which reductions are safe enough?

Distinguish spatial token pruning, temporal token pruning, pooling, learned
compression, and deleting source frames during curation. Internal pruning may
be layer-dependent or conditioned on the task; deleting an asset is a separate
storage decision and does not reproduce that mechanism.

What happens when pruning removes a small object, a brief contact, an occluded
hand, or the history needed to distinguish two identical current images?
Can a causal policy select tokens without looking at future observations?

Compare unpruned and reduced inputs on the same examples. Measure event recall,
spatial grounding, temporal ordering, downstream task success, latency, memory,
and processed-token counts. Slice results by small objects, fast motion, long
history, and rare failures. Does the reduction actually save end-to-end cost
after selection overhead, or only reduce a nominal token count?

## 5. How do automated labels change the picture?

Treat generated captions and labels as proposals, not ground truth. Which
taxonomy and model versions produced them, which evidence supports them, and
which human audit catches omissions? A confident caption can still be wrong.

Sampling can hide failures that a labeler cannot recover from retained frames.
How would audits of original footage separate sampling
errors from labeler errors? Test jointly optimized sampling and labeling against
an independently reviewed reference set.

## Related exercises

- [Video curation and sampling](../system_design/video_curation_and_sampling.md)
- [Multimodal joins](../system_design/multimodal_dataset_join.md)
- [VLM evaluation](../system_design/vlm_evaluation.md)
