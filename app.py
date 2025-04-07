from flask import Flask, request, jsonify

app = Flask(__name__)

data = [{
    "done": True,
    "label": "Sample Todo 1"
},{
    "done": True,
    "label": "Sample Todo 2"
}
]
@app.route('/')
def getTodo():
    return jsonify(data)
@app.route("/todo", methods=["POST"])
def addTodo():
    newData = request.get_json()
    data.append(newData)
    return jsonify(data), 201
@app.route("/todo/<int:todo_id>", methods=["DELETE"])
def deleteTodo(todo_id):
    if todo_id < len(data):
        data.pop(todo_id)
        return jsonify(data), 200
    else:
        return jsonify({"error": "Todo not found"}), 404
if __name__ == '__main__':
    app.run(debug=True , port=5000)