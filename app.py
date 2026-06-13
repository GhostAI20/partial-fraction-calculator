from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/calculate')
def calculate():
    try:
        r = request.args.get('r')
        if r is None:
            return jsonify({"error": "Parameter 'r' is required"}), 400
        
        r = int(r)
        if r == 1 or r == -3:
            return jsonify({"error": "Division by zero: r cannot be 1 or -3"}), 400
            
        result = 4 / ((r - 1) * (r + 3))
        return jsonify({"r": r, "f(r)": result})
        
    except ValueError:
        return jsonify({"error": "Parameter 'r' must be an integer"}), 400

if name == 'main':
    app.run(debug=True)
