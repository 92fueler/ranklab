# Model architecture map

A practical map of the main neural-model families used for vision-language
learning, robot manipulation, and physical-world prediction. Learn the prediction target
first, then the network, objective, and inference loop. The families below are
representative, not an exhaustive catalogue or mutually exclusive categories.

## 1. What “architecture” means

A **neural architecture** specifies how representations and trainable modules
connect: image encoder, language backbone, fusion mechanism, memory, action head,
or dynamics model. A **training/serving platform** supplies data, distributed
execution, checkpoints, queues, deployment, and observability. Understanding the
second requires knowing what the first consumes and predicts.

Common building blocks recur:

- CNNs extract spatial features; vision transformers (ViTs) process image patches.
- Transformers mix token representations through attention. Causal attention
  restricts access to later positions; cross-attention connects different sequences.
- Recurrent networks and state-space modules can maintain evolving state.
- U-Nets and diffusion transformers are possible denoisers, not task definitions.

An architecture description should answer five independent questions:

1. **Representation:** pixels, patch embeddings, language tokens, robot state,
   action vectors, discrete codes, or spatial features?
2. **Fusion/history:** concatenation, cross-attention, compression, or memory?
3. **Target:** text, embedding, action, future image, or future latent state?
4. **Learning:** contrastive alignment, token prediction, regression, denoising,
   flow matching, prediction, or reward-driven optimization?
5. **Execution:** one pass, sequential decoding, iterative generation, or feedback control?

Thus an action-chunk policy can use a VLM backbone, cross-attention, diffusion,
and a high-level planner simultaneously. Behavior cloning and reinforcement
learning describe learning setups, not single network architectures.

This map emphasizes modern multimodal training and evaluation. Conventional
perception → state estimation → planning → control remains important, as does
model-free actor-critic reinforcement learning, especially in locomotion and
dexterity. These systems need not contain a VLM; this is not all of robotics.

## 2. Eleven families to recognize

For each family, separate **training** (targets and gradients) from **inference**
(available inputs and generated outputs). An example model is a reference point,
not a requirement to reproduce every implementation detail.

### A. Dual-encoder contrastive models

```text
image -> vision encoder -> image embedding
text  -> text encoder   -> text embedding -> similarity
```

**Examples:** [CLIP](https://arxiv.org/abs/2103.00020);
[SigLIP](https://arxiv.org/abs/2303.15343) uses a sigmoid pairwise alignment loss.

**Input/output:** An image or text becomes an embedding; paired embeddings receive
similarity scores, not generated captions.

**Training:** Align matching image-text examples while distinguishing mismatches.
CLIP uses a batchwise contrastive objective; not every dual encoder uses the same
negative sampling or loss normalization.

**Inference:** Encode a query and retrieve nearby items, or compare an image with
text descriptions of candidate classes. Candidate wording affects classification.

**Data/evaluation:** Image-text pairs; evaluate retrieval recall, ranking, and
zero-shot classification across meaningful slices. Similarity is not calibrated truth.

**Infrastructure:** Version both encoders, preprocessing, embedding dimensions,
and indexes together. Manage deduplication, batching, negative composition, and
large embedding caches. A changed encoder generally invalidates old embeddings.

### B. Vision encoder + projector + language decoder

```text
image -> vision encoder -> projector -> visual embeddings
                                      + prompt -> language decoder -> text
```

**Example:** [LLaVA](https://arxiv.org/abs/2304.08485).

**Input/output:** Images and a question or instruction produce language, including
captions, answers, or structured text.

**Training:** A learned projection bridges visual features and the language
model's embedding space. A common recipe first aligns the connector, then trains
on visual instruction-response examples. Which modules are frozen varies.
Supervised next-token loss usually scores the intended answer, not every input.

**Inference:** Encode the image, condition the decoder, and generate text
sequentially. More image crops or patches can increase context and compute.

**Data/evaluation:** Image-text pairs and instruction-response examples; test
answer correctness, grounding, hallucination, abstention, and resolution-sensitive tasks.

**Infrastructure:** Preserve image preprocessing, conversation templates, special
tokens, and response masks. Audit truncation: retaining the answer while dropping
its visual evidence creates a misleading training example.

### C. Learned resamplers and cross-attention fusion

```text
visual features -> learned queries/resampler -> compact visual sequence
text stream <-> visual cross-attention or visual-prefix interface -> text
```

**Examples:** [Flamingo](https://arxiv.org/abs/2204.14198) and
[BLIP-2](https://arxiv.org/abs/2301.12597) illustrate different connections.

**Input/output:** Images or video plus text produce language using a learned
interface between visual features and a language backbone.

**Training:** Learn the bridge while optionally freezing large pretrained modules.
BLIP-2 uses cross-attention inside its querying connector and supplies a visual
prefix to the language model. Flamingo inserts visual cross-attention into the
language stack. Their training stages and objectives also differ.

**Inference:** Learned queries can compress many visual features into fewer
representations; cross-attention lets language states consult visual features.
Compression may discard small objects or brief events.

**Data/evaluation:** Paired or interleaved visual-language examples, depending on
design. Evaluate multi-image association, grounding, temporal questions, and
quality against visual-token budget.

**Infrastructure:** Represent image boundaries and text-image correspondence
explicitly. Preserve packing rules and attention masks; benchmark connector
compute separately from decoder context length.

### D. Temporal video encoders and memory-augmented models

```text
frames + timestamps -> spatial/temporal encoder -> history representation
                                              -> task head or language decoder
```

**Example:** [Qwen2-VL](https://arxiv.org/abs/2409.12191) combines image/video
processing with temporal and spatial position information; streaming extensions
may add memory.

**Input/output:** Video becomes features, labels, answers, or a memory state.
Temporal attention, frame pooling, recurrent memory, and cached summaries are
alternative mechanisms, not equivalent forms of “remembering.”

**Training:** Depending on the model, use masked video reconstruction, temporal
labels, or language supervision. Pretraining a video encoder does not itself
create a conversational VLM.

**Inference:** Offline models may inspect the whole clip; streaming models must
update using only available observations. A decoder KV cache is not automatically
a durable semantic memory of everything observed.

**Data/evaluation:** Ordered clips and reliable timing; test event order, duration,
long-range dependencies, missed brief events, and streaming latency.

**Infrastructure:** Preserve timestamp mappings and stream resets. Measure
sampling, memory eviction, and compression policies alongside model quality.

### E. Behavior cloning with continuous action chunks

```text
images + robot state -> policy -> next H action vectors
```

**Example:** [ACT](https://tonyzhaozh.github.io/aloha/) combines a transformer
policy, action chunking, and a conditional variational formulation.

**Input/output:** Current observations predict a short sequence of continuous
commands, such as joint targets or end-effector deltas.

**Training:** Fit demonstrated actions. Simple policies use regression; ACT also
uses reconstruction and latent-regularization losses. Chunking means predicting multiple
steps, not necessarily predicting them autoregressively.

**Inference:** ACT removes its training-time latent encoder and fixes the latent
at the prior mean. Predict a chunk, execute a prefix, observe again, and replan.
Temporal aggregation of overlapping predictions is a separate choice.

**Data/evaluation:** Synchronized demonstrations with action units, coordinate
frames, control rate, and robot state. Evaluate offline action error and closed-loop
success, recovery, contact behavior, and timing.

**Infrastructure:** Make horizons and action semantics explicit. Normalize using
training statistics; mask padding and invalid dimensions. A low regression loss
can still produce an unsafe average of multiple valid behaviors.

### F. Autoregressive discrete-action VLAs

```text
image + instruction + optional state -> multimodal transformer
                           -> action tokens -> continuous commands
```

**Example:** [OpenVLA](https://arxiv.org/abs/2406.09246).

**Input/output:** Visual-language context produces robot actions represented as
discrete symbols, rather than an ordinary natural-language answer.

**Training:** Quantize action values and optimize action-token prediction, commonly
adapting a pretrained vision-language backbone on robot demonstrations.
Discretization and token ordering are part of the model contract.

**Inference:** Generate action symbols sequentially and decode them to commands.
This introduces quantization choices and sequential decoding costs. Neither
all VLAs nor all action-chunk policies use this representation.

**Data/evaluation:** Paired observations, instructions, and robot actions. Measure
closed-loop task success, generalization, latency, and sensitivity to quantization;
token accuracy alone cannot establish useful control.

**Infrastructure:** Version action vocabulary, normalization, embodiment-specific
mappings, and decode rules. Prevent text-token handling or special-token changes
from silently altering the robot interface.

### G. Conditional diffusion policies

```text
observations -> conditioning
noise action chunk -> repeated denoising -> continuous action chunk
```

**Example:** [Diffusion Policy](https://arxiv.org/abs/2303.04137).

**Input/output:** Observations condition a distribution over future continuous
actions, often an entire chunk.

**Training:** Corrupt demonstration actions at sampled noise levels and train a
network to predict noise, clean actions, or an equivalent target under the chosen
parameterization. This can represent multiple plausible behaviors more naturally
than a single deterministic regression output.

**Inference:** Iteratively refine a noisy action sample, execute a prefix, and
replan. Sampling steps, scheduling, and conditioning affect both latency and quality.

**Data/evaluation:** Robot demonstrations with aligned state and actions; compare
closed-loop success, robustness, action smoothness, and latency-quality trade-offs.
Sample diversity is not evidence of calibrated uncertainty or safety.

**Infrastructure:** Version noise schedules, parameterizations, random seeds, and
samplers. Report end-to-end control deadlines, not just neural-network forward-pass time.

### H. VLM backbone + continuous flow/diffusion action expert

```text
images + language -> VLM context ------------------+
robot state + noisy actions + time ----------------+
                                                   -> action expert -> chunk
```

**Example:** [GR00T N1](https://arxiv.org/abs/2503.14734) uses a flow-matching action expert.

**Input/output:** A semantic visual-language backbone conditions a specialized
continuous-action generator. The backbone and expert can interact through
attention rather than only a final pooled vector.

**Training:** Combine pretrained representations with robot-action supervision;
additional language or other objectives are recipe-dependent. Flow matching
learns a vector field transporting samples between distributions. It is related
to, but not synonymous with, diffusion denoising.

**Inference:** Numerically integrate the learned flow, or use the chosen diffusion
sampler, then execute actions under feedback. Do not assume ordinary next-token
text decoding determines control latency.

**Data/evaluation:** Mixed data can update different modules with different losses.
Evaluate semantic generalization and precise control separately, then together.

**Infrastructure:** Track per-source objective masks, module freezing, mixture
weights, action normalization, integration steps, and asynchronous control behavior.

### I. Hierarchical cognition and control

```text
observations + goal -> planner -> subgoal/skill
observations + subgoal -> low-level controller -> actions
```

**Example:** [π0.5](https://www.pi.website/blog/pi05) couples
semantic subtask prediction with continuous action generation.

**Input/output:** One component chooses what to accomplish; another executes it.
The boundary may be language, skill identifiers, waypoints, or latent commands.
A slow VLM/fast action expert need not produce explicit symbolic plans.

**Training:** Components can be trained separately or jointly using demonstrations,
subgoal labels, rewards, or combinations. Hierarchy describes decomposition, not
one mandatory loss or one particular company's architecture.

**Inference:** The controller runs frequently; planning and replanning may happen
less often or when completion/failure is detected.

**Data/evaluation:** Need supervision for the chosen interface or a defensible way
to learn it. Test subgoal feasibility, completion detection, recovery, and total task success.

**Infrastructure:** Version planner-controller interfaces and timing. Distinguish
planner failure, controller failure, and stale or unsupported commands.

### J. World models: generated observations versus predictive latent state

```text
history + optional actions -> dynamics model -> future frames or latent states
```

**Input/output:** Predict consequences, not necessarily which action to choose.
Action conditioning is a capability to verify, not implicit in “video model.”

**Two important branches:**

- **Generative video world models** generate future visual observations, often
  through diffusion or autoregressive latent-video generation. An
  [action-conditioned model](https://arxiv.org/abs/2501.03575) maps candidate
  actions to future observations. A different interface is instruction → future
  video → inverse dynamics → actions, as in
  [1XWM](https://www.1x.tech/discover/world-model-self-learning). Do not treat
  video-as-plan plus inverse dynamics as the same action-conditioned forward model.
- **Latent world models** predict a compact internal state. Dreamer-style models
  support [imagined policy learning](https://danijar.com/project/dreamerv3/);
  [V-JEPA 2](https://arxiv.org/abs/2506.09985) illustrates predictive feature
  learning and an action-conditioned extension. Not every latent
  predictor has actions, rewards, a decoder, or a policy.

**Inference:** Roll forward a proposed trajectory, supply imagined experience, or
support planning. A separate planner, policy, or inverse-dynamics module may be required.

**Training/data:** Use video generation or latent-prediction objectives;
action-conditioned models need aligned controls or state-derived actions.

**Evaluation:** Evaluate long-horizon drift, action responsiveness, geometry,
contact, and downstream decision usefulness. Compare teacher-forced prediction
with free-running rollouts; attractive video does not prove reliable physics.

**Infrastructure:** Version action interfaces, horizons, rollouts, policies, and
matched real-world cases. Separate unconditioned plausibility from controllable dynamics.

### K. Spatial and 3D representations

```text
images/depth/poses -> 3D encoder or reconstruction -> spatial representation
                                                   -> task-specific head
```

**Examples:** Point clouds, voxel features, occupancy fields,
[neural radiance fields](https://www.matthewtancik.com/nerf), and
[Gaussian splats](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) are
different representations, not one architecture. NeRF uses an implicit field;
Gaussian splatting uses explicit primitives.

**Input/output:** Produce or consume spatial structure to support reconstruction,
rendering, localization, planning, or manipulation.

**Training:** Objectives may involve geometry, photometric reconstruction,
occupancy, correspondence, or downstream actions. Some scene representations are
optimized per scene rather than produced by a general-purpose feed-forward model.

**Inference:** Render views, query occupied space, recover spatial features, or
condition another model. A static reconstruction is neither a dynamics model nor
a control policy merely because it is three-dimensional.

**Data/evaluation:** Calibrated multiview images, depth, poses, or other geometric
supervision as required. Test geometry, novel-view quality, and downstream task
utility separately; good rendering can hide incorrect geometry.

**Infrastructure:** Maintain coordinate conventions, scale, calibration, sensor
synchronization, and representation versions. Account for scene-update and query costs.

## 3. One five-second clip, three different learning problems

Suppose a robot camera records a gripper lifting a cup from 0–5 seconds. The
recording may also contain instructions, robot state, and timestamped commands.
At decision time **2 seconds**, only an observation prefix is available.

### Caption the clip with a VLM

**Input:** Sampled frames from the full 0–5-second clip and “Describe what happens.”
**Target:** A verified caption. **Loss:** Caption-token prediction; prompt, image,
and padding positions generally do not receive that answer loss.

The full clip is legitimate evidence for an offline description. It is not
legitimate input to a policy pretending to act at 2 seconds. Evaluation asks
whether the description matches visible events, not whether a robot can execute it.

### Choose robot actions with a VLA

**Input:** Instruction and observations available by 2 seconds, including sensor
latency constraints. **Target:** Demonstrated commands over the next horizon.
**Loss:** Regression, discrete-token prediction, diffusion, or flow matching,
depending on the action head.

Future actions are training targets, not extra observed history. A diffusion or
flow model's corrupted target chunk is a training construction, not future
information available to the deployed robot. Mask unavailable actions, invalid
dimensions, and padded steps; missing commands must not become zero commands.
Evaluate feedback control in the environment, not only demonstration imitation.

### Predict the next state with a world model

**Input:** The prefix through 2 seconds and, for action-conditioned prediction,
an explicitly supplied candidate action sequence. **Target:** Future images or
latent states after 2 seconds. **Loss:** The model's generative or predictive objective.

At training time, recorded future commands can supply the conditioning sequence;
at planning time, candidate commands must be supplied by the planner. Future
sensor measurements remain targets. Test free-running predictions and whether
changing proposed actions changes outcomes appropriately.

Human egocentric video can support captioning and some world-model objectives
without measured robot actions. It does not become robot behavior-cloning data
by adding timestamps. Inferred actions are separately labeled supervision with
an inference model and uncertainty, not recorded ground truth.

**Keep three masks distinct:** padding masks remove filler; attention/availability
masks control accessible evidence; loss masks select supervised targets.

## 4. Connect the model to the engineering work

A video codec compresses media bytes. Frame sampling chooses observations.
A visual encoder produces features; tokenization or resampling determines what
the downstream model receives. Codec keyframes are not semantic events, and
visual tokens need not be discrete vocabulary IDs.

Autoregression generates ordered outputs using previous outputs. Diffusion
iteratively denoises; flow matching learns transport dynamics. None alone tells
you whether the model reasons over time, represents 3D, or controls a robot.

Use the related guides in this order:

1. [Video sampling and visual tokens](video_sampling_and_visual_tokens.md): what evidence reaches the network.
2. [Video curation and sampling](../system_design/video_curation_and_sampling.md): which examples enter training.
3. [Multimodal dataset joins](../system_design/multimodal_dataset_join.md): causal alignment and action semantics.
4. [Annotation quality control](../system_design/annotation_quality_control.md): trustworthy supervision.
5. [Multimodal model training](../system_design/multimodal_model_training.md): objectives, masks, mixtures, and reproducibility.
6. [Evaluation metrics](evaluation_metrics.md), [world-model evaluation](../system_design/world_model_evaluation.md), and [VLM evaluation](../system_design/vlm_evaluation.md): evidence appropriate to the target.

For any new model, sketch its modules, one training example, loss-bearing targets,
and one deployed inference cycle. Then ask: **Which observed failure would a lower
training loss fail to catch?** That question connects model internals to useful
training infrastructure and evaluation work.
