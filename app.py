from flask import Flask, request, jsonify

app = Flask(__name__)

def recommend_size(height, weight):
    if weight > 80:
        return "L"
    elif weight < 60:
        return "S"
    else:
        return "M"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    height = float(data['height'])
    weight = float(data['weight'])
    size = recommend_size(height, weight)
    return jsonify({'size': size})

if __name__ == '__main__':
    app.run(debug=True)