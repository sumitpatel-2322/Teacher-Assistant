import random
from typing import List, Dict


def select_diverse_solutions(
    ranked: List[Dict],
    max_results: int,
    seed: str,
    primary_band: float = 0.2,
    secondary_band: float = 0.6,
) -> List[Dict]:
    """
    Deterministic diversity selector with two confidence bands.
    """

    if not ranked:
        return []

    random.seed(seed)

    max_score = ranked[0]["confidence"]

    primary = [
        s for s in ranked
        if (max_score - s["confidence"]) <= primary_band
    ]

    secondary = [
        s for s in ranked
        if primary_band < (max_score - s["confidence"]) <= secondary_band
    ]

    selected = []
    used_styles = set()

    # Always pick at least one from primary band
    random.shuffle(primary)
    for s in primary:
        style = s.get("response_style")
        selected.append(s)
        if style:
            used_styles.add(style)
        break

    # Fill remaining slots with style diversity
# Use top solution as relevance anchor
    anchor = selected[0]

    def is_context_compatible(candidate, anchor):
        return (
            candidate.get("subject") == anchor.get("subject")
            or candidate.get("topic_type") == anchor.get("topic_type")
            or candidate.get("class_range") == anchor.get("class_range")
        )

    combined = [
        s for s in (primary[1:] + secondary)
        if is_context_compatible(s, anchor)
    ]

    random.shuffle(combined)


    for s in combined:
        style = s.get("response_style")
        if style and style in used_styles:
            continue

        selected.append(s)
        if style:
            used_styles.add(style)

        if len(selected) == max_results:
            break

    # Final fill (if still short)
    for s in ranked:
        if s not in selected:
            selected.append(s)
        if len(selected) == max_results:
            break

    return selected