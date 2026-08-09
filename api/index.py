"""api/index.py — Vercel entrypoint.

Vercel's Python runtime auto-detects a WSGI `app` object in the entrypoint
file it builds. This just re-exports the real Flask app from
app/admin_web/app.py (see that file's docstring for why) after putting app/
on sys.path so its sibling imports (admin_core, admin_html, store_postgres)
resolve the same way they do for the local server.
"""
import os, sys

_APP_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app')
if _APP_DIR not in sys.path:
    sys.path.insert(0, _APP_DIR)

from admin_web.app import app  # noqa: E402  (re-exported for Vercel's WSGI auto-detection)
