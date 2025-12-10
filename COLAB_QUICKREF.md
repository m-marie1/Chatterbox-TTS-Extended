# Chatterbox-TTS-Extended Colab Quick Reference

## 🚦 Session Checklist

Before starting each Colab session:

- [ ] Enable GPU runtime (`Runtime` → `Change runtime type` → `GPU`)
- [ ] Run all setup cells in order (Steps 1-5)
- [ ] Wait for model downloads (first run only)
- [ ] Verify GPU is detected in Step 1
- [ ] Launch the Gradio interface (Step 6)

## ⚙️ Recommended Settings Quick Guide

### Artifact Reduction (Main Goal)
```
✅ Denoise with RNNoise (pyrnnoise)
✅ Use faster-whisper backend
✅ Candidates per chunk: 3+
✅ Max attempts: 3
✅ Post-process with Auto-Editor (optional)
```

### Memory-Friendly Settings (If OOM errors)
```
Whisper Model: tiny
Candidates: 1-2
Parallel workers: 1
Bypass Whisper: ❌ (keep enabled for quality)
```

### High-Quality Settings (More VRAM needed)
```
Whisper Model: small or medium
Candidates: 4-5
Parallel workers: 4-6
All cleanup options enabled
```

## 🎯 Common Use Cases

### Quick Test (Fast)
- Text: 1-2 sentences
- Whisper: tiny
- Candidates: 1
- Time: ~10 seconds

### High Quality (Best Results)
- Text: Any length
- Whisper: small/medium
- Candidates: 3-5
- RNNoise: ✅ Enabled
- Time: ~30s per paragraph

### Voice Conversion
- Use VC tab
- Upload input + reference voice
- Adjust pitch if needed
- Time: ~30s per minute of audio

## 🔧 Quick Fixes

### GPU Not Available
```python
# Check: Runtime → Change runtime type → GPU → Save
import torch
print(torch.cuda.is_available())  # Should be True
```

### Out of Memory
```python
# Clear memory
import torch, gc
torch.cuda.empty_cache()
gc.collect()
```

### Gradio Not Loading
```bash
# Check if process is running
!ps aux | grep Chatter

# Restart by re-running Step 6
```

### Audio Has Artifacts
```
1. Enable RNNoise denoising ✅
2. Increase candidates to 3-5
3. Use faster-whisper (not bypass)
4. Enable Auto-Editor
5. Check reference audio quality
```

## 📥 Download Files

```python
# Download all audio files
from google.colab import files
import os

for f in os.listdir('output'):
    if f.endswith(('.wav', '.mp3', '.flac')):
        files.download(f'output/{f}')
```

## ⏱️ Typical Generation Times (T4 GPU)

| Task | Settings | Time |
|------|----------|------|
| 1 sentence | Basic | ~10s |
| 1 sentence | 3 candidates + Whisper | ~20s |
| 1 paragraph | Quality mode | ~45s |
| 1 page | Batch + quality | ~3min |

*First generation adds 30-60s for model loading*

## 🎓 Learning Path

1. **Start Simple**: Generate 1 sentence with default settings
2. **Add Quality**: Enable RNNoise, increase candidates
3. **Fine-tune**: Adjust emotion, temperature, CFG
4. **Batch Process**: Upload text files, use batching
5. **Voice Clone**: Add reference audio for voice matching
6. **Convert Voices**: Try the VC tab

## 💾 Before Session Ends

```python
# List all outputs
!ls -lh output/

# Download important files
from google.colab import files
for f in ['file1.mp3', 'file2.wav']:  # Replace with your files
    files.download(f'output/{f}')
```

## 📊 GPU Memory Usage

| Setting | VRAM Usage | Safe for Free Tier? |
|---------|------------|---------------------|
| tiny Whisper, 1 candidate | ~3-4 GB | ✅ Yes |
| base Whisper, 2 candidates | ~4-6 GB | ✅ Yes |
| small Whisper, 3 candidates | ~6-8 GB | ✅ Usually |
| medium Whisper, 3 candidates | ~8-12 GB | ⚠️ Maybe |
| large Whisper, 5 candidates | ~12-15 GB | ❌ Pro only |

## 🆘 Emergency Commands

```bash
# Restart Python runtime (lose all variables)
# Runtime → Restart runtime

# Or from code (doesn't work in Colab, use menu)
# exit()  # This won't help, use menu

# Kill hung process
!pkill -f Chatter.py

# Check GPU status
!nvidia-smi

# Free disk space
!df -h
```

## 📚 More Help

- Full Guide: See [COLAB_GUIDE.md](COLAB_GUIDE.md)
- Notebook: See embedded help sections
- Issues: [GitHub Issues](https://github.com/m-marie1/Chatterbox-TTS-Extended/issues)

---

**Pro Tip**: Save your favorite settings as a JSON file and reload them each session using the "Load Settings" feature in the UI!
