import os
import re
import json
from flask import Flask, request, render_template
from groq import Groq

app = Flask(__name__)

# Security Best Practice: Use environment variables for keys
# Set this in your terminal: export GROQ_API_KEY='your_key_here'
GROQ_API_KEY = os.environ.get("GROQ_API_KEY") or "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"
client = Groq(api_key=GROQ_API_KEY)

def extract_product(url):
    """Extract readable product name from URL."""
    url = url.rstrip("/").split("?")[0].split("#")[0]
    parts = url.split("/")
    product = next((p for p in reversed(parts) if p), "Product")
    product = re.sub(r"%[0-9a-fA-F]{2}", " ", product)
    product = product.replace("-", " ").replace("_", " ")
    return re.sub(r"\s+", " ", product).strip()

def get_groq_json(product, url):
    """Call Groq API and return sustainability data."""
    prompt = f"""
    You are a sustainability analyst. Return ONLY a JSON object for: {product} (URL: {url}).
    Structure:
    {{
      "overall_score": 85,
      "summary": "Brief summary",
      "issues": ["Issue 1", "Issue 2"],
      "alternatives": [
        {{
          "name": "Product Name",
          "score": 92,
          "description": "Why it is better",
          "icon": "🌿"
        }}
      ]
    }}
    Scores must be integers between 0-100. Do not include URLs.
    """
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.2,
        )
        raw = response.choices[0].message.content.strip()
        # Clean potential markdown backticks
        raw = re.sub(r"```json|```", "", raw).strip()
        return json.loads(raw)
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}

@app.route("/", methods=["GET", "POST"])
def home():
    analysis = None
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if not url.startswith("http"):
            analysis = {"error": "Please provide a valid URL starting with http/https"}
        else:
            product_name = extract_product(url)
            analysis = get_groq_json(product_name, url)
            analysis["product_name"] = product_name
    return render_template("index.html", analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)