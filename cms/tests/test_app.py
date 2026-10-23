
from cms.app import create_app
from cms.config import TestingConfig
from cms.app.posts import list_posts
from pathlib import Path

def test_dashboard_returns_success():
    app = create_app(TestingConfig)
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"THE_CONFIG_FILE" in response.data


def test_app_uses_testing_config():
    app = create_app(TestingConfig)

    assert app.config["TESTING"] is True
    assert app.config["SECRET_KEY"] == "Test-SK"


def test_posts_directory_is_configured():
    app = create_app(TestingConfig)

    posts_dir = app.config["POSTS_DIR"]

    assert posts_dir.name == "_posts"
    assert posts_dir.is_absolute()


def test_list_posts_returns_markdown_files(tmp_path):
    (tmp_path / "2026-10-20-articulo.md").write_text(
        "# Artículo de prueba",
        encoding="utf-8",
    )
    (tmp_path / "2026-10-21-otro.md").write_text(
        "# Otro artículo",
        encoding="utf-8",
    )
    (tmp_path / "imagen.png").write_bytes(b"imagen")

    posts = list_posts(tmp_path)

    assert len(posts) == 2
    assert all(post.suffix == ".md" for post in posts)


def test_list_posts_returns_empty_list_for_missing_directory(tmp_path):
    missing_dir = tmp_path / "no-existe"

    posts = list_posts(missing_dir)

    assert posts == []


def test_dashboard_shows_empty_state():
    app = create_app(TestingConfig)
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Todav" in response.data
    assert b"no hay articulos" in response.data
