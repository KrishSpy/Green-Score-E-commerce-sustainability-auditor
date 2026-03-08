🌱 Green Score: e-Commerce Sustainability Auditor

📌 Problem Statement
Many products on e-commerce websites claim to be eco-friendly or sustainable, but consumers often cannot verify these claims.
This leads to greenwashing, where companies market products as environmentally friendly without real proof.
Customers who want to make sustainable purchasing decisions struggle because:
Sustainability information is not clearly visible
Environmental impact is hard to measure
Comparing products based on sustainability is difficult
Our project aims to solve this problem by providing a simple sustainability scoring system for e-commerce products.

💡 Solution Approach
Green Score is an AI-powered tool that analyzes product descriptions and calculates a sustainability score.

How it works
User enters the product name or description.
The system sends the product data to an AI model.
The AI evaluates the product based on factors like:
Materials used
Packaging
Carbon footprint
Sustainability claims
The system generates:
Green Score (0–100)
Eco-friendly analysis
Recommended alternative products
This helps users quickly understand whether a product is truly green or not.

⚙️ Technologies Used
Frontend

HTML

CSS

JavaScript

Backend

Python

Flask

AI & APIs

Groq API (LLM model) for sustainability analysis

Data Handling

JSON

Regex for extracting structured information

🚀 Features

🌿 Sustainability Green Score (0–100)

📊 Simple eco impact analysis

🔍 Detects greenwashing claims

♻️ Suggests better eco-friendly alternatives

⚡ Fast AI analysis

🖥️ Project Workflow

1️⃣ User enters product name
2️⃣ Backend sends prompt to AI model
3️⃣ AI evaluates sustainability factors
4️⃣ System generates structured output
5️⃣ Frontend displays score + analysis

📂 Project Structure
GreenScore/
│
├── app.py                # Flask backend
├── templates/
│   └── index.html        # Main frontend page
│
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend logic
│
└── README.md
▶️ How to Run the Project
1️⃣ Install dependencies
pip install flask
pip install groq
2️⃣ Run the Flask server
python app.py
3️⃣ Open in browser
http://127.0.0.1:5000
🎯 Future Improvements

Integration with real e-commerce platforms

Automatic product scraping

More accurate sustainability datasets

Browser extension for Amazon/Flipkart product scoring

👥 Team

Hackathon Project – Green Score

Built to promote sustainable online shopping 🌍
