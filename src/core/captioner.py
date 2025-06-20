"""Image captioning utilities."""

from __future__ import annotations


class ImageCaptioner:
    """Placeholder captioner that returns a fixed caption."""

    def caption(self, image_path: str) -> str:
        """Return a caption for the supplied image path."""
        # Real implementation would feed the image into a captioning model.
        return f"Caption for {image_path}"
