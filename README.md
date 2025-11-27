=> Real Estate Market Analysis Chatbot
  "AI-powered Property Insights for Pune (Django + React + Groq)"

This project is an AI-powered real-estate chatbot that helps users analyze property trends in Pune.
It supports:

✔ Single-area analysis — “Analyze Wakad”
✔ Multi-area comparison — “Compare Wakad and Aundh”
✔ Trend charts (Price & Demand over time)
✔ AI-generated market insights (Groq LLM)
✔ Downloadable Excel data tables
✔ Fully interactive chatbot-style UI in React

Features
🔍 1. Smart Query Handling
  The chatbot understands:
  “Analyze Wakad”
  “Show trend for Hinjewadi”
  “Compare Wakad and Aundh”
  “Compare Kothrud, Baner and Wakad”

📊 2. Dynamic Trend Charts
Trends include:
  Annual Price Change
  Annual Demand Change
Rendered using Recharts LineChart.

🤖 3. AI-Powered Summary (Groq LLM)
Generates a 5–7 sentence expert summary:
  Market growth
  Price stability / volatility
  Demand strength
  Investment recommendations

📥 4. Excel Download
Users can download the filtered data as:
filtered_data.xlsx

📁 5. Dataset
The project uses a cleaned dataset with columns:
area | year | price | demand | size

🏗️ Technologies Used
=> Backend (Django REST Framework)
  Python 3.x
  Django 5
  Django REST Framework
  Pandas
  Groq API (AI summaries)

=> Frontend (React)
  React
  Axios
  Recharts
  Custom UI components (ChatInput, TrendChart, DataTable)

📦 Folder Structure
RealEstateChatbot/
│
├── backend/
│   ├── api/
│   │   ├── views.py
│   │   ├── chatbot.py
│   │   ├── excel_loader.py
│   │   ├── urls.py
│   ├── realestate_backend/
│   ├── dataset.xlsx
│   ├── .env
│   ├── manage.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── api.js
│   │   ├── components/
│   │   │   ├── ChatInput.js
│   │   │   ├── TrendChart.js
│   │   │   ├── DataTable.js
│   ├── package.json
│
└── README.md

⚙️ Installation & Setup
1. Clone the Project
     git clone https://github.com/yourusername/real-estate-chatbot.git
     cd real-estate-chatbot
   
🖥️ Backend Setup (Django)
  1. Create Virtual Environment
     cd backend
     python -m venv venv
     venv\Scripts\activate   # On Windows

  2. Install Dependencies
     pip install -r requirements.txt

  3. Create .env
     Inside /backend/.env:
     GROQ_API_KEY=your_key_here
     GROQ_MODEL=llama-3.1-70b-versatile

  4. Run Server
     python manage.py runserver
     Backend runs at:
     http://127.0.0.1:8000/

🎨 Frontend Setup (React)
  1. Install Packages
     cd frontend
     npm install

  2. Run Frontend Dev Server
     npm start
     Frontend runs at:
     http://localhost:3000/

🧠 How It Works
=> User enters:
    Analyze Wakad

=> Backend:
    - Loads dataset
    - Filters rows where area == "wakad"
    - Computes:
      >avg_price
      >avg_demand
      >trend
    - Sends small dataset preview to Groq AI
    - Returns JSON

=> Frontend:
  - Displays AI summary
  - Plots trend chart
  - Shows data table
  - Enables Excel download
