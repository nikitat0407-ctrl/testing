from flask import Flask, request, jsonify

app = Flask(__name__)

# "База данных"
tasks = []

# Класс Task
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }

# Главная страница (принимает ВСЁ, чтобы не было ошибок)
@app.route("/", methods=["GET", "POST"])
def home():
    return "Tasks API работает"

# POST /tasks
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    task = Task(
        title=data["title"],
        completed=data.get("completed", False)
    )

    tasks.append(task)

    return jsonify(task.to_dict())

# GET /tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([t.to_dict() for t in tasks])

# запуск сервера
if __name__ == "__main__":
    app.run(debug=True)
