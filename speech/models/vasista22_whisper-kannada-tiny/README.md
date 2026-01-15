---
language:
- kn
license: apache-2.0
tags:
- whisper-event
metrics:
- wer
model-index:
- name: Whisper Kannada Tiny - Vasista Sai Lodagala
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: kn_in
      split: test
    metrics:
    - type: wer
      value: 13.38
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Kannada Tiny

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the Kannada data available from multiple publicly available ASR corpuses.
It has been fine-tuned as a part of the Whisper fine-tuning sprint.

**NOTE:** The code used to train this model is available for re-use in the [whisper-finetune](https://github.com/vasistalodagala/whisper-finetune) repository.

## Usage

In order to evaluate this model on an entire dataset, the evaluation codes available in the [whisper-finetune](https://github.com/vasistalodagala/whisper-finetune) repository can be used.

The same repository also provides the scripts for faster inference using whisper-jax.

In order to infer a single audio file using this model, the following code snippet can be used:

```python
>>> import torch
>>> from transformers import pipeline

>>> # path to the audio file to be transcribed
>>> audio = "/path/to/audio.format"
>>> device = "cuda:0" if torch.cuda.is_available() else "cpu"

>>> transcribe = pipeline(task="automatic-speech-recognition", model="vasista22/whisper-kannada-tiny", chunk_length_s=30, device=device)
>>> transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="kn", task="transcribe")

>>> print('Transcription: ', transcribe(audio)["text"])
```

For faster inference of whisper models, the [whisper-jax](https://github.com/sanchit-gandhi/whisper-jax) library can be used. Please follow the necessary installation steps as mentioned [here](https://github.com/vasistalodagala/whisper-finetune#faster-evaluation-with-whisper-jax), before using the following code snippet:

```python
>>> import jax.numpy as jnp
>>> from whisper_jax import FlaxWhisperForConditionalGeneration, FlaxWhisperPipline

>>> # path to the audio file to be transcribed
>>> audio = "/path/to/audio.format"

>>> transcribe = FlaxWhisperPipline("vasista22/whisper-kannada-tiny", batch_size=16)
>>> transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="kn", task="transcribe")

>>> print('Transcription: ', transcribe(audio)["text"])
```

## Training and evaluation data

Training Data: 
  - [IISc-MILE Kannada ASR Corpus](https://www.openslr.org/126/)
  - [ULCA ASR Corpus](https://github.com/Open-Speech-EkStep/ULCA-asr-dataset-corpus#kannada-labelled-total-duration-is-60891-hours)
  - [Shrutilipi ASR Corpus](https://ai4bharat.org/shrutilipi)
  - [Google/Fleurs Train+Dev set](https://huggingface.co/datasets/google/fleurs)

Evaluation Data: 
  - [Google/Fleurs Test Set](https://huggingface.co/datasets/google/fleurs)
  - [IISc-MILE Test Set](https://www.openslr.org/126/)
  - [OpenSLR](https://www.openslr.org/79/)

## Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 88
- eval_batch_size: 88
- seed: 22
- optimizer: adamw_bnb_8bit
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10000
- training_steps: 15008 (terminated upon convergence. Initially set to 51570 steps)
- mixed_precision_training: True

## Acknowledgement
This work was done at [Speech Lab, IIT Madras](https://asr.iitm.ac.in/).

The compute resources for this work were funded by "Bhashini: National Language translation Mission" project of the Ministry of Electronics and Information Technology (MeitY), Government of India.
