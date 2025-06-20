"""Batch processing helpers."""

from __future__ import annotations


def process_batch(images: list[str]) -> list[str]:
    """Process a batch of images and return their captions."""
    from .captioner import ImageCaptioner

    captioner = ImageCaptioner()
    return [captioner.caption(image) for image in images]
