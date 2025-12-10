# 🚀 Google Colab Guide for Chatterbox-TTS-Extended

This guide provides detailed information about using Chatterbox-TTS-Extended on Google Colab.

## Quick Start

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/m-marie1/Chatterbox-TTS-Extended/blob/main/Chatterbox_TTS_Extended_Colab.ipynb)

Click the badge above to open the notebook directly in Google Colab.

## Why Use Google Colab?

If you don't have a capable GPU or powerful CPU for running TTS models, Google Colab is the perfect solution:

- ✅ **Free GPU Access**: Use NVIDIA T4 GPUs for free (A100/V100 with Pro)
- ✅ **No Installation Required**: Everything runs in the cloud
- ✅ **Pre-configured Environment**: All dependencies handled automatically
- ✅ **Artifact Reduction**: Full support for RNNoise denoising and quality validation
- ✅ **Easy Sharing**: Share your generated audio files directly from Colab

## Features Available in Colab

All features of Chatterbox-TTS-Extended work on Colab:

### TTS Features
- Multi-candidate generation for best quality
- Whisper validation to reduce artifacts
- RNNoise denoising for clean audio
- Auto-editor for silence removal
- Batch processing support
- Multiple export formats (WAV, MP3, FLAC)

### Voice Conversion
- Voice-to-voice conversion
- Pitch adjustment
- Long audio support with automatic chunking

## Recommended Settings for Colab

### Free Tier (T4 GPU, ~15GB VRAM)
```
Whisper Model: tiny or base
Use faster-whisper: ✅ Enabled
Candidates per chunk: 2-3
Parallel workers: 2-3
Enable RNNoise: ✅ Enabled
```

### Pro/Pro+ (A100/V100, more VRAM)
```
Whisper Model: small or medium
Use faster-whisper: ✅ Enabled
Candidates per chunk: 3-5
Parallel workers: 4-6
Enable RNNoise: ✅ Enabled
```

## How to Use

1. **Open the Notebook**: Click the "Open in Colab" badge
2. **Enable GPU**: 
   - Go to `Runtime` → `Change runtime type`
   - Select `GPU` as Hardware accelerator
   - Choose `T4` GPU (or better)
   - Click `Save`
3. **Run Setup Cells**: Execute cells in order (use Shift+Enter)
4. **Launch Interface**: Wait for Gradio to start
5. **Generate Audio**: Use the web interface to create TTS

## Tips for Best Results

### Reducing Artifacts (Main Goal!)

The Extended version was created specifically to reduce artifacts and noise. To get the best results:

1. **Enable RNNoise Denoising** ✅ (Most important!)
2. Use **3+ candidates per chunk** with Whisper validation
3. Enable **Auto-Editor** for additional cleanup
4. Use **faster-whisper** backend for efficient validation
5. Set **Max Attempts to 3** to retry failed chunks

### Memory Management

If you encounter CUDA out of memory errors:

```python
# Option 1: Reduce settings
# - Use smaller Whisper model (tiny/base)
# - Reduce candidates to 1-2
# - Set parallel workers to 1

# Option 2: Clear GPU memory manually
import torch
import gc
torch.cuda.empty_cache()
gc.collect()

# Option 3: Restart runtime
# Runtime → Restart runtime
```

### Saving Your Work

Generated files are in the `output/` directory. Download them before your session ends:

```python
from google.colab import files
import os

# Download all audio files
for file in os.listdir('output'):
    if file.endswith(('.wav', '.mp3', '.flac')):
        files.download(f'output/{file}')
```

## Troubleshooting

### "No GPU detected" Warning

**Solution**: Enable GPU runtime
1. `Runtime` → `Change runtime type`
2. Select `GPU` as Hardware accelerator
3. Click `Save`
4. Re-run all cells

### Slow Performance

**Check GPU is being used**:
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU: {torch.cuda.get_device_name(0)}")
```

### Session Timeout

Colab free tier has session time limits:
- Download your audio files regularly
- Consider upgrading to Colab Pro for longer sessions
- Pro: 24-hour sessions
- Pro+: Up to 48-hour sessions

### Installation Errors

If packages fail to install:
1. Restart runtime (`Runtime` → `Restart runtime`)
2. Run cells again in order
3. Check error messages for specific issues

### CUDA Out of Memory

Try these solutions in order:
1. Use smaller Whisper model (tiny instead of medium)
2. Reduce candidates per chunk to 1-2
3. Set parallel workers to 1
4. Restart runtime to clear memory
5. Upgrade to Colab Pro for more VRAM

### FFmpeg Not Found

FFmpeg should be pre-installed in Colab. If you get errors:
```bash
!apt-get install --reinstall -y ffmpeg
```

## Colab-Specific Optimizations

The notebook includes several Colab-specific optimizations:

1. **PyTorch CUDA version**: Uses cu121 (compatible with Colab's CUDA 12.x)
2. **Dependency versions**: Tested and verified on Colab environment
3. **Memory management**: Automatic VRAM cleanup after Whisper validation
4. **Installation order**: Optimized to avoid conflicts with pre-installed packages
5. **Gradio sharing**: Enabled by default for easy access

## Comparison: Original Chatterbox vs Extended

| Feature | Original Chatterbox | Chatterbox-TTS-Extended |
|---------|---------------------|-------------------------|
| Basic TTS | ✅ | ✅ |
| Voice Cloning | ✅ | ✅ |
| Artifact Reduction | ❌ | ✅ RNNoise |
| Quality Validation | ❌ | ✅ Whisper |
| Auto Cleanup | ❌ | ✅ Auto-Editor |
| Batch Processing | Limited | ✅ Full Support |
| Multiple Candidates | ❌ | ✅ |
| Noise/Artifacts | Common | Minimal |

## Performance Benchmarks

Approximate generation times on Google Colab (T4 GPU):

| Text Length | Settings | Time |
|-------------|----------|------|
| 1 sentence | 1 candidate, no validation | ~5-10s |
| 1 sentence | 3 candidates, Whisper | ~15-25s |
| 1 paragraph | 3 candidates, Whisper, RNNoise | ~30-60s |
| 1 page | Batch mode, 3 candidates | ~2-5 min |

*Times include model loading on first run (add 30-60s)*

## Limitations

### Free Tier
- Session time limit (~12 hours idle, may disconnect)
- May be slower during peak hours
- Limited to T4 GPU

### All Tiers
- Internet required
- Files deleted when runtime is reset
- No persistent storage (download files regularly)

## Upgrading to Pro

Consider Colab Pro if you need:
- Longer sessions (24-48 hours)
- Better GPUs (A100, V100)
- More VRAM (up to 40GB)
- Priority access during peak hours
- Background execution

## Additional Resources

- **Notebook**: [Chatterbox_TTS_Extended_Colab.ipynb](Chatterbox_TTS_Extended_Colab.ipynb)
- **GitHub**: [Chatterbox-TTS-Extended Repository](https://github.com/m-marie1/Chatterbox-TTS-Extended)
- **Issues**: [Report Problems](https://github.com/m-marie1/Chatterbox-TTS-Extended/issues)
- **Original Chatterbox**: [Resemble AI](https://github.com/resemble-ai/chatterbox)

## Support

If you encounter issues:

1. Check this guide's Troubleshooting section
2. Review error messages carefully
3. Search existing GitHub issues
4. Create a new issue with:
   - Error message
   - Steps to reproduce
   - Colab GPU type
   - Settings used

## Credits

- **Chatterbox-TTS-Extended**: Enhanced version with artifact reduction
- **Original Chatterbox**: Resemble AI
- **RNNoise**: Xiph.Org Foundation
- **Whisper**: OpenAI
- **Google Colab**: Google Research

---

**Enjoy artifact-free speech synthesis on Google Colab! 🎉**
