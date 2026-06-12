from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/')
def home():
    return jsonify({"message": "Day 13 API working", "status": "ok"})

@app.route('/calculate')
def calculate():
    try:
        r = float(request.args.get('r'))
        
        if r == 1 or r == -3:
            return jsonify({"error": "r cannot be 1 or -3"}), 400
        
        result = 1/(r-1) - 1/(r+3)
        
        return jsonify({
            "day": 13,
            "r": r,
            "f(r)": result,
            "formula": "4/((r-1)(r+3)) = 1/(r-1) - 1/(r+3)"
        })
        
    except:
        return jsonify({"error": "Invalid input"}), 400

if name == 'main':
    app.run(debug=True)
