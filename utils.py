import json


def load_candidates_from_json(path):
    with open(path, mode="r", encoding="utf-8") as f:
        return json.load(f)


def get_candidate(candidates, candidate_id):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidates, candidate_name):
    result = []
    for item in candidates:
        if candidate_name.lower() in item["name"].lower():
            result.append(item)
    return result


def get_candidates_by_skill(candidates, skill_name):
    result = []
    for item in candidates:
        if skill_name.lower() in item["skills"].lower().split(', '):
            result.append(item)
    return result

