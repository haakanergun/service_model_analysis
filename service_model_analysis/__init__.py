"""Service model analysis utilities and demo web application."""

from .analysis import ServiceRecord, average_duration

# Flask app is optional; only import if available.
try:
    from .app import app
except Exception:  # pragma: no cover - app import failure is not critical
    app = None

__all__ = ["ServiceRecord", "average_duration", "app"]
