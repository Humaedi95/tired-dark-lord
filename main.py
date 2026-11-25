"""The Tired Dark Lord — a 100-word villain monologue.

Writes one monologue to /output/entry.txt. Deterministic, self-contained,
no network access. The villain is specific, scheming, and secretly very
tired — the tiredness lives in the rhythm and the small deflections, never
in a plain statement of it.
"""

import os

MONOLOGUE = (
    "Come in. Mind the third step\u2014it bites. I cursed it myself, back when "
    "spite still felt like fun. Sit. Not there. That chair keeps the last "
    "hero. Young. Loud. Sure. I put him under the rose beds. They bloom well "
    "now. The plan\u2014yes, still a plan. The crown, the eclipse, the seven "
    "seals, all of it. I have the maps, the keys. I have waited three hundred "
    "years, and I would honestly rather be in bed. But the eclipse comes "
    "once. So. Shall we begin? One more time. After you\u2014no, after me. "
    "Someone has to lead."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")


if __name__ == "__main__":
    main()
