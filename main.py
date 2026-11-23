"""office-joke: write one office joke to /output/entry.txt.

Joke (90 characters):
"I put 'per my last email' in my will, so my family knows I already answered that question."

Construction: it leans on the universally recognised office phrase "per my last email"
(recognition) and lands its surprise in the will (the turn).
Deterministic: no network, no randomness and no secrets.
"""

import os

JOKE = "I put 'per my last email' in my will, so my family knows I already answered that question."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
