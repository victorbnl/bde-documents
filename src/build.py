from pathlib import Path
import shutil


SRC_DIR = Path(__file__).parent
ROOT_DIR = SRC_DIR.parent

DIST_DIR = ROOT_DIR / "dist"
DOCS_DIR = ROOT_DIR / "docs"


def create_folder():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()


def copy_docs():
    shutil.copytree(DOCS_DIR, DIST_DIR / DOCS_DIR.name)


def gen_dir_list(dir):
    items = []

    for file in filter(Path.is_file, dir.iterdir()):
        items.append(f"<li><a href=''>{file.name}</a></li>")

    for subdir in filter(Path.is_dir, dir.iterdir()):
        items.append(f"<li>{subdir.name}<ul>{gen_dir_list(subdir)}</ul></li>")

    return "<ul>" + "".join(items) + "</ul>"


def gen_page():
    blocks = []

    for subdir in filter(Path.is_dir, DOCS_DIR.iterdir()):
        blocks.append(f"<h2>{subdir.name}</h2>")
        blocks.append(gen_dir_list(subdir))

    return "".join(blocks)


if __name__ == "__main__":
    create_folder()
    copy_docs()

    with (SRC_DIR / "index.html").open("r") as file:
        template = file.read()

    with (DIST_DIR / "index.html").open("w") as file:
        file.write(template.replace("<!-- LIST -->", gen_page()))
