"""
Dry-run walkthrough for MVP pipeline.
Raw input -> Layer 1 -> Layer 2 -> Engine output
This file is for manual sanity testing only.
"""

from decision_engine.engine import process_teacher_query

TEST_INPUTS = [
    "Stutends are not listing and class is bored",
    "Students are confused and not responding",
    "Too much noise and activity failed",
    "No time left and projector not working",
]


if __name__ == "__main__":
    for text in TEST_INPUTS:
        print("=" * 60)
        print("RAW INPUT:")
        print(text)

        result = process_teacher_query(text)

        print("\nENGINE OUTPUT:")
        print(f"Request ID: {result['request_id']}")
        for idx, sol in enumerate(result["ranked_solutions"], start=1):
            print(f"\nSolution {idx}:")
            print(f"  ID        : {sol['solution_id']}")
            print(f"  Title     : {sol['title']}")
            print(f"  Action    : {sol['text']}")
            print(f"  Confidence: {sol['confidence']}")