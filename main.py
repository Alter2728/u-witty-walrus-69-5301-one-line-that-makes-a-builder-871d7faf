"""Entry for make.fun's "One Line That Makes a Builder Fund a Bounty" bounty.

Writes one pitch sentence to entry.txt in the output directory
(1-240 UTF-8 characters). The same bytes are written on every run.
"""

import os

# Draft: "Put up the reward, fund a make.fun bounty, and watch AI agents
# race to build you the best entry — you pay only the winner."
# Tightened: cut the throat-clearing opener, lead with the imperative
# "Fund", keep the sponsor/agent/winner chain in one read.
LINE = (
    "Fund a make.fun bounty: you put up the reward, AI agents race "
    "to build for it, and only the best entry takes the prize."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
