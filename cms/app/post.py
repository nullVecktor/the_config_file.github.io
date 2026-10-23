
from pathlib import Path

#esta funcion devuelve los archivos Markdown de la carpeta de publicaciones.
def list_posts(posts_dir: Path) -> list[Path]:
    
    if not posts_dir.is_dir():
        return []

    return sorted(
        posts_dir.glob("*.md"),
        key=lambda post: post.name.lower(),
    )
