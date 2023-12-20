from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
multiplication_table = {}

# Define an endpoint to generate a multiplication table
@app.route('/m/<int:number>', methods=['GET'])
def generate_multiplication_table(number):
    table = []
    for i in range(1, 11):
        result = number * i
        table.append(result)
    multiplication_table[number] = table
    return jsonify({"number": number, "multiplication_table": table})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
