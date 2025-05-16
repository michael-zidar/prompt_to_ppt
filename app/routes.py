from __future__ import annotations

import json
import tempfile
from pathlib import Path

from flask import Blueprint, render_template, request, send_file, abort
from werkzeug.utils import secure_filename

from .config import get_settings
from .style_extractor import extract_style
from .slide_generator import generate_slide_json
from .pptx_renderer import build_pptx

main = Blueprint("main", __name__)


@main.get("/")
def index():
    return render_template("index.html")


@main.post("/generate")
def generate():
    settings = get_settings()
    prompt = request.form.get("prompt", "")
    sample = request.files.get("sample")

    style = {}
    if sample:
        filename = secure_filename(sample.filename)
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(filename).suffix) as tmp:
            sample.save(tmp.name)
            style = extract_style(Path(tmp.name))
    slides = generate_slide_json(prompt, style)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as out:
        build_pptx(slides, style, Path(out.name))
        return send_file(out.name, as_attachment=True, download_name="result.pptx")
