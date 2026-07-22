import json
import os
import uuid
import shutil

from bot_runtime import smoke_limit
from questions import BLUEPRINT, scope_files, target_scopes

def generate_scope_files():
    """
    Split all_questions.json into chunks of 25 questions and save them as separate files.
    Each file will be named with a UUID and contain 25 questions.
    """
    # Get the scope directory and remove stale chunks from prior projects/runs.
    scope_directory = os.environ.get('SCOPE_DIR', 'scope')
    if os.path.exists(scope_directory):
        shutil.rmtree(scope_directory)
    os.makedirs(scope_directory, exist_ok=True)

    try:
        # Hard Metric-only contamination guard.
        if BLUEPRINT.get("repo_name") != "metric" or BLUEPRINT.get("source_repo") != "incjanta/metric":
            raise RuntimeError(f"Non-Metric blueprint loaded: {BLUEPRINT.get('source_repo')} / {BLUEPRINT.get('repo_name')}")
        allowed_prefixes = ("metric-core/", "metric-periphery/", "smart-contracts-poc/")
        bad_files = [f for f in scope_files if not f.startswith(allowed_prefixes)]
        if bad_files:
            raise RuntimeError(f"Non-Metric scope files detected: {bad_files[:10]}")

        chunk_size = 25
        limit = smoke_limit()
        active_scope_files = scope_files[:limit] if limit else scope_files
        active_target_scopes = target_scopes[:1] if limit else target_scopes
        total_questions = len(active_scope_files)

        for target_scope in active_target_scopes:
            for i in range(0, total_questions, chunk_size):

                # Get a chunk of 25 questions
                chunk = active_scope_files[i:i + chunk_size]

                # Add target_scope mapping to each file in the chunk
                chunk_with_scope = []
                for file_path in chunk:
                    chunk_with_scope.append(f"'File Name: {file_path} -> Scope: {target_scope}'")

                # Generate a unique filename
                filename = f"{str(uuid.uuid4())}.json".replace("-", "")
                filepath = os.path.join(scope_directory, filename)

                # Save the chunk to a new file
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(chunk_with_scope, f, indent=2, ensure_ascii=False)

                print(f"Saved {len(chunk_with_scope)} questions to {filepath}")

            print(
                f"\nSuccessfully split {total_questions} questions into {((total_questions - 1) // chunk_size) + 1} files")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    generate_scope_files()


if __name__ == '__main__':
    main()
