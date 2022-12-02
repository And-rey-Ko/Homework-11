from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name


candidates_json ="candidates.json"
candidates = load_candidates_from_json(candidates_json)
app = Flask(__name__)


@app.route('/')
def get_all():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def get_by_id(idx):
    candidate = get_candidate(candidates, idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def get_by_name(candidate_name):
    candidates_by_name = get_candidates_by_name(candidates, candidate_name)
    if not candidates_by_name:
        return "Кандидат не найден"
    return render_template('search.html', candidates=candidates_by_name)


@app.route('/skills/<skill_name>')
def get_by_skill(skill_name):
    candidates_by_skill = get_candidates_by_skill(candidates, skill_name)
    return render_template('skill.html', candidates=candidates_by_skill, skill=skill_name)


if __name__ == "__main__":
    app.run(debug=True)
