# 🌍 Multilingual Support Guide

This guide explains how to use the new multilingual features in Chatterbox-TTS-Extended to generate high-quality speech in multiple languages with clean, artifact-free output.

## Overview

Chatterbox-TTS-Extended now combines:
- ✅ **Clean artifact-free output** from the Extended version (RNNoise, Whisper validation, Auto-Editor)
- ✅ **Multilingual pronunciation** from the original Chatterbox by Resemble AI
- ✅ **23 language support** with authentic pronunciation using the real multilingual model

## Supported Languages

The multilingual model supports 23 languages with authentic pronunciation:

| Language | Code | Language | Code | Language | Code |
|----------|------|----------|------|----------|------|
| English | `en` | German | `de` | French | `fr` |
| Spanish | `es` | Italian | `it` | Portuguese | `pt` |
| Polish | `pl` | Turkish | `tr` | Russian | `ru` |
| Dutch | `nl` | Arabic | `ar` | Chinese | `zh` |
| Japanese | `ja` | Korean | `ko` | Hindi | `hi` |
| Danish | `da` | Greek | `el` | Finnish | `fi` |
| Hebrew | `he` | Malay | `ms` | Norwegian | `no` |
| Swedish | `sv` | Swahili | `sw` |  |  |

## How to Use

### Option 1: Using the Gradio UI

1. **Launch the UI**: Run `python Chatter.py` or use the Colab notebook
2. **Enable Multilingual**: Check the "Enable Multilingual Model" checkbox
3. **Select Language**: Choose your target language from the dropdown
4. **Generate**: Use all other features normally (artifact reduction, voice cloning, etc.)

**Note:** Switching between English and multilingual models will reload the model, which takes about 30-60 seconds.

### Option 2: Using the Colab Notebook

The notebook includes a "Language Learning Content Generation" cell that demonstrates:
- German-only dialogue (repeated for practice)
- German-English paired dialogue (translation practice)

To use it:
1. Open the notebook in Colab
2. Run all cells up to the Language Learning section
3. Run the language learning cell
4. Download the generated audio files

### Option 3: Programmatic Usage

```python
from chatterbox.src.chatterbox.tts import ChatterboxTTS
import torchaudio

# Load the multilingual model
model = ChatterboxTTS.from_pretrained(
    device="cuda",  # or "cpu"
    use_multilingual=True
)

# Generate German speech
wav_de = model.generate(
    "Guten Tag! Wie geht es Ihnen?",
    language_id="de",
    cfg_weight=0.5,
    exaggeration=0.5
)

# Generate French speech
wav_fr = model.generate(
    "Bonjour! Comment allez-vous?",
    language_id="fr",
    cfg_weight=0.5,
    exaggeration=0.5
)

# Save the audio
torchaudio.save("german.wav", wav_de, model.sr)
torchaudio.save("french.wav", wav_fr, model.sr)
```

## Voice Cloning Across Languages

You can use reference audio in any language to clone a voice:

```python
# Use German reference audio
wav = model.generate(
    "Hallo! Das ist ein Test.",
    language_id="de",
    audio_prompt_path="reference_german.wav"
)

# Use English reference with German text
wav = model.generate(
    "Guten Tag!",
    language_id="de",
    audio_prompt_path="reference_english.wav"
)
```

## Using Artifact Reduction Features

All artifact reduction features work with multilingual mode:

### RNNoise Denoising
- **In UI**: Check "Denoise with RNNoise" checkbox
- **Result**: Removes background noise and artifacts from all languages

### Whisper Validation
- **In UI**: Configure Whisper model and candidates per chunk
- **Result**: Validates pronunciation quality across languages

### Auto-Editor
- **In UI**: Check "Post-process with Auto-Editor"
- **Result**: Removes silences and stutters in any language

### Example with All Features

```python
from your_script import process_text_for_tts

# Generate German audio with full artifact reduction
output_files = process_text_for_tts(
    text="Guten Tag! Wie geht es Ihnen?",
    input_basename="german_test",
    audio_prompt_path_input=None,
    exaggeration_input=0.5,
    temperature_input=0.75,
    seed_num_input=42,
    cfgw_input=1.0,
    use_pyrnnoise=True,          # Enable RNNoise
    use_auto_editor=True,         # Enable Auto-Editor
    ae_threshold=0.06,
    ae_margin=0.2,
    export_formats=["wav", "mp3"],
    enable_batching=False,
    to_lowercase=True,
    normalize_spacing=True,
    fix_dot_letters=True,
    remove_reference_numbers=True,
    keep_original_wav=False,
    smart_batch_short_sentences=True,
    disable_watermark=True,
    num_generations=1,
    normalize_audio=False,
    normalize_method="ebu",
    normalize_level=-24,
    normalize_tp=-2,
    normalize_lra=7,
    num_candidates_per_chunk=3,   # Generate multiple candidates
    max_attempts_per_candidate=3,
    bypass_whisper_checking=False,
    whisper_model_name="medium",
    enable_parallel=True,
    num_parallel_workers=4,
    use_longest_transcript_on_fail=True,
    sound_words_field="",
    use_faster_whisper=True,
    language_id="de"              # Specify German
)
```

## Language Learning Use Case

Perfect for creating language learning materials:

```python
# Create dialogue practice material
dialogue = [
    {"german": "Wie heißt du?", "english": "What is your name?"},
    {"german": "Ich heiße Anna.", "english": "My name is Anna."},
]

for turn in dialogue:
    # German version
    wav_de = model.generate(turn["german"], language_id="de")
    
    # English version
    wav_en = model.generate(turn["english"], language_id="en")
    
    # Combine for practice: DE, EN, DE, EN
    # ... (see Colab notebook for full example)
```

## Troubleshooting

### Model Download Issues

**Problem:** First-time download takes a while
- **Solution:** The multilingual model is ~2-3GB. First download may take 5-10 minutes.

### Pronunciation Issues

**Problem:** Text not pronounced correctly in target language
- **Solution:** Ensure `language_id` parameter is set correctly (e.g., "de" not "german")

### Memory Issues

**Problem:** Out of VRAM/RAM
- **Solution:** 
  - Use smaller Whisper models (tiny/base)
  - Reduce candidates per chunk (2-3)
  - Reduce parallel workers (1-2)
  - On Colab, use T4 GPU with conservative settings

### Switching Between Models

**Problem:** Want to switch between English and multilingual
- **Solution:** In the UI, toggle the "Enable Multilingual Model" checkbox. The model will reload automatically (takes ~30-60 seconds).

## Performance Notes

- **Model Size:** Multilingual model is ~2-3GB (vs ~1.5GB for English-only)
- **Speed:** Similar performance to English-only model
- **VRAM:** Same requirements as English model
- **Quality:** Authentic pronunciation for each language

## Best Practices

1. **Use appropriate language IDs**: Always specify the language code that matches your text
2. **Enable artifact reduction**: RNNoise and Whisper validation significantly improve quality
3. **Test with candidates**: Use 3-5 candidates per chunk for best results
4. **Reference audio**: Upload clean reference audio for better voice consistency
5. **Batch processing**: For long texts, enable batching to improve flow

## Examples

See the Colab notebook "Language Learning Content Generation" cell for complete working examples of:
- German-only dialogue generation
- German-English paired dialogue
- Using reference audio across languages
- Artifact reduction with multilingual audio

## Technical Details

### Implementation

The multilingual support is implemented through:
1. **MTLTokenizer**: Full multilingual tokenizer with language-specific preprocessing (from original Chatterbox)
2. **T3 Model**: Uses multilingual T3 model with 2454 token vocabulary (vs 704 for English)
3. **Model files**: Loads `t3_mtl23ls_v2.safetensors`, `ve.pt`, `s3gen.pt`, and `grapheme_mtl_merged_expanded_v1.json`
4. **Language parameter**: Passes through entire generation pipeline with proper preprocessing
5. **Repository**: Downloads from `ResembleAI/chatterbox` with multilingual model files

### Compatibility

- ✅ Works with all artifact reduction features
- ✅ Compatible with voice conversion
- ✅ Supports batch processing
- ✅ Works with file uploads
- ✅ Settings persistence
- ✅ All export formats (WAV, MP3, FLAC)

## Support

For issues or questions:
1. Check the [README](README.md) for general usage
2. See [COLAB_GUIDE](COLAB_GUIDE.md) for Colab-specific tips
3. Open an issue on GitHub with:
   - Language you're trying to use
   - Error messages
   - Settings used

---

**Happy multilingual TTS generation! 🎉🌍**
