try:
    from importlib.metadata import version, PackageNotFoundError
except Exception:
    # Fallback for older environments
    try:
        from importlib_metadata import version, PackageNotFoundError  # type: ignore
    except Exception:
        version = None
        PackageNotFoundError = Exception

if version is not None:
    try:
        __version__ = version("chatterbox-tts")
    except PackageNotFoundError:
        __version__ = "0+local"
else:
    __version__ = "0+local"


from .tts import ChatterboxTTS
from .vc import ChatterboxVC
from .mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES