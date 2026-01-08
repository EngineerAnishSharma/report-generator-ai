import json
import re

def clean_llm_json(output: str):
    """
    Removes ```json ... ``` wrappers and returns a Python dict
    """
    if isinstance(output, dict):
        return output

    cleaned = re.sub(r"```json|```", "", output).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM did not return valid JSON: {e}")
