from flask import Flask, render_template
from utils import json_load, get_candidates_by_id, \
    get_candidates_by_name, get_candidate_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    """Главная страничка. Показывает список всех кандидатов."""

    candidates: list[dict] = json_load()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:uid>")
def show_candidate_by_key(uid: int) -> str:
    """Показывает кандидата на страничке /candidates/id по его id."""

    candidate: dict = get_candidates_by_id(uid)
    if not candidate:
        return f'<h1>Извините, у нас всего {len(json_load())} кандидатов</h1>'
    return render_template('card.html', candidate=candidate)


@app.route("/name/<name>")
def show_candidate_by_name(name: str) -> str:
    """Показывает кандидата на страничке /name/name по его имени."""

    candidates: list[dict] = get_candidates_by_name(name.lower())
    return render_template('search.html', candidates=candidates, name=name)


@app.route('/skills/<skill>')
def show_candidate_by_skill(skill: str) -> str:
    """Показывает кандидата на страничке /skills/skill по введённому навыку."""

    candidates: list[dict] = get_candidate_by_skill(skill.lower())
    return render_template('skill.html', candidates=candidates, skill=skill)


if __name__ == '__main__':
    app.run(debug=True)
###########################################################################
