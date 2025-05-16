from app import create_app

app = create_app()


def test_index():
    with app.test_client() as client:
        resp = client.get("/")
        assert resp.status_code == 200


def test_generate(monkeypatch):
    from app import slide_generator
    monkeypatch.setattr(
        slide_generator,
        "generate_slide_json",
        lambda prompt, style: [{"layout": "Title Slide", "elements": {"title": "Test"}}],
    )
    with app.test_client() as client:
        resp = client.post("/generate", data={"prompt": "test"})
        assert resp.status_code == 200
        assert resp.mimetype == "application/vnd.openxmlformats-officedocument.presentationml.presentation"
