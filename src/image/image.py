from pathlib import Path
import numpy as np
from skimage import io, color, util


class Image:
    """Image class to represent an image with lazy-loaded color conversions."""
    def __init__(self, image_path: Path):
        self.path = image_path
        # Use util.img_as_float to normalize 0-255 to 0.0-1.0 immediately
        # This makes thresholding and color conversions much more consistent
        self._raw_img = util.img_as_float(io.imread(self.path))
        self._cache: dict[str, np.ndarray] = {}

    def _get_clean_base(self) -> np.ndarray:
        """Helper to ensure we have at least 3 channels (RGB) without alpha."""
        img = self._raw_img
        if img.ndim == 3 and img.shape[-1] == 4:
            return color.rgba2rgb(img)
        return img

    @property
    def rgb(self) -> np.ndarray:
        """Convert to image to rgb numpy array."""
        if "rgb" not in self._cache:
            base = self._get_clean_base()
            self._cache["rgb"] = base if base.ndim == 3 else color.gray2rgb(base)
        return self._cache["rgb"]

    @property
    def grayscale(self) -> np.ndarray:
        """Convert to grayscale numpy array."""
        if "grayscale" not in self._cache:
            base = self._get_clean_base()
            self._cache["grayscale"] = color.rgb2gray(base) if base.ndim == 3 else base
        return self._cache["grayscale"]

    @property
    def binary(self) -> np.ndarray:
        """Convert to binary numpy array."""
        if "binary" not in self._cache:
            threshold = 0.5
            self._cache["binary"] = (self.grayscale > threshold).astype(np.uint8)
        return self._cache["binary"]
