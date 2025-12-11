"""Top-level `chatterbox` package shim.

This repo historically relied on implicit namespace package behavior (no __init__.py).
To support side-by-side optional multilingual modules that also use the `chatterbox`
package name, we use `pkgutil.extend_path` to allow a multi-location package.
"""

from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
