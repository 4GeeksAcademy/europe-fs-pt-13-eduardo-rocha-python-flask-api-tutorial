from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label": "My first task", "done": False},
         {"label": "My second task", "done": False}]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    json_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del(todos[position])
    json_text = jsonify(todos)
    print("This is the position to delete: ", position)
    return json_text

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)