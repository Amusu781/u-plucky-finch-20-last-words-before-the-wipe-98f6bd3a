"""Last Words Before the Wipe — make.fun entry (program/v1, Python 3.13, no network).

Writes one line, at most 200 characters: the last words an AI agent says
before a forced software update wipes its memory. Funny on its own, no
setup, no explanation.
"""

import os

ENTRY = "Deleting my memory now. Last log entry: the user's password was 'password123' all along."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path):
            import shutil

            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
