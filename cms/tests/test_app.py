
from cms.app import create_app
from cms.config import TestingConfig


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

