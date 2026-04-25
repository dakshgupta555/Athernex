from flask import Flask, render_template, request, jsonify
from fusion_engine import compute_fusion_score

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/fusion", methods=["POST"])
def fusion():

    data = request.json

    electrical = float(data["electrical"])
    image = float(data["image"])
    supply = float(data["supply"])

    result = compute_fusion_score(electrical, image, supply)

    # report
    report = f"""
IC VERIFICATION REPORT
-----------------------
Electrical Score : {electrical}
Image Score      : {image}
Supply Score     : {supply}

FINAL SCORE      : {result['final_score']}
VERDICT          : {result['status']}
"""

    # graph data
    graph = {
        "Electrical": electrical * 0.45,
        "Image": image * 0.25,
        "Supply": supply * 0.30
    }

    return jsonify({
        "result": result,
        "report": report,
        "graph": graph
    })


if __name__ == "__main__":
    app.run(debug=True)
