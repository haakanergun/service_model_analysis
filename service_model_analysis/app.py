from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Home page for demo."""
    return render_template_string(
        """
        <h1>Service Model Analysis Demo</h1>
        <p>Use /analyze to view a sample analysis.</p>
        """
    )

@app.route('/analyze')
def analyze():
    """Return a placeholder analysis result."""
    result = {
        "root_cause": "Sample Root Cause",
        "affected_components": ["ServiceA", "ServiceB"],
        "summary": "Demo analysis of service model issue."
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
