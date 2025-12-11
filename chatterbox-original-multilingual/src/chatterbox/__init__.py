from pkgutil import extend_path

# Allow this package to be split across multiple locations (used by the Extended UI
# which also provides modules under the `chatterbox` package name).
__path__ = extend_path(__path__, __name__)

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