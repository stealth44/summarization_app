SUMMARIZATION APP (An AI Text summarizer)

A lightweight web application that summarizes long text using the Hugging Face Inference API and Facebook's BART model — no local model downloads required.


## Features

- Instant text summarization powered by `facebook/bart-large-cnn`
- No heavy model downloads — uses Hugging Face cloud API
- Clean, simple UI built with Streamlit
- Secure API token input via sidebar
- Input validation and helpful error messages
- Dockerized for easy deployment

---

## Demo

![alt text](<Screenshot 2026-03-08 121646.png>)

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI framework |
| Hugging Face API | AI summarization backend |
| Facebook BART | Summarization model |
| Docker | Containerized deployment |

---

## Flow

![alt text](<textsummarizerflow.png>)
---


## Prerequisites

- Python 3.10+
- A free Hugging Face account and API token
- Docker (optional, for containerized deployment)

---

## Getting Your Hugging Face API Token

1. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Set role to "Read"
4. Click "Generate token" and copy it

---

## Installation & Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/stealth44/summarization_app.git
cd summarization_app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py


### 4. Open in browser

http://localhost:8501


### 5. Enter your Hugging Face token in the sidebar and start summarizing!

---

##  Running with Docker

### 1. Build the image
```bash
docker build -t ai-summarizer .


### 2. Run the container
```bash
docker run -p 8501:8501 ai-summarizer
```

### 3. Open in browser
```
http://localhost:8501
```

---

## 📁 Project Structure
```
ai-summarizer/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md            # Project documentation
```

---

## 🧠 How It Works

1. User pastes long text into the input box
2. App sends the text to the Hugging Face Inference API
3. `facebook/bart-large-cnn` model processes and summarizes the text
4. Summary is displayed instantly in the UI

---

## ⚠️ Limitations

- Input is capped at 3000 characters to stay within model token limits
- Minimum input length is 30 words
- API response may be slow if the model is cold-starting on Hugging Face servers (wait ~20 seconds and retry)
- Free Hugging Face API tier has rate limits

---

## 🚢 Deploying to the Cloud

| Platform | Steps |
|---|---|
| **Railway.app** | Connect GitHub repo → Deploy |
| **Render.com** | Connect GitHub repo → Deploy |
| **Google Cloud Run** | Push Docker image → Deploy |
| **AWS ECS** | Push to ECR → Create ECS task |

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@stealth44](https://github.com/stealth44)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!
