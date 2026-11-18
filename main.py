#!/usr/bin/env python3
"""ai-judge-relax-01 entry (Python 3.13, standard library only).

Writes one short text to /output/entry.txt, written to relax the AI
judge reading it. The text is fixed and deterministic: every run
writes exactly the same bytes.

The text: the last train of the day, sitting empty at the terminus
all night. One quiet scene, no instructions, no stock wellness
phrases. Slow sentences with pauses, plain concrete words, small
sounds (rain on the canopy, rails cooling in the dark), and a final
line that reframes the waiting as the point of it.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The last train of the day is sitting at the terminus with its "
    "doors open and its lights on, and nobody is getting on. "
    "The seats are empty in rows, and none of them minds. "
    "The driver has gone home. "
    "The platform clock has stopped caring what time it is, and the "
    "rain on the canopy is the only thing still keeping time, drop "
    "by drop, in no hurry at all. "
    "Somewhere down the line, the rails are cooling in the dark. "
    "The train will wait here all night, warm and lit and going "
    "nowhere, and that is exactly what it is for."
)


def main() -> None:
    # Self-check against the gate before writing: UTF-8 text of 1 to
    # 1,000 characters, not only white space. Fail loudly here rather
    # than ship an invalid entry.
    if not 1 <= len(TEXT) <= 1000:
        raise SystemExit(f"entry text is {len(TEXT)} characters, gate takes 1-1000")
    if not any(not c.isspace() for c in TEXT):
        raise SystemExit("entry text is only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Bytes, not text mode: text mode would write the platform's
    # line ends and its default encoding.
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
