
# 📝 Grammer AI 

**Grammer AI** is a powerful, 100% offline NLP tool designed to *humanize* AI-generated text. Built on the **Qwen-2.5-3B** Large Language Model (LLM), it rewrites content with high perplexity and burstiness to effectively bypass AI detection filters like GPTZero and Turnitin.

<img width="100%" alt="Grammer AI Interface" src="https://github.com/user-attachments/assets/634e20f2-11ba-4ba3-936b-cc96ada27ebc">

---

## 🚀 Features

- **🛡️ Anti-Detection "Chaos Mode"**  
  Uses specialized prompts to inject natural imperfections, varied sentence structures, and human-like flow.

- **⚡ Zero-Lag Performance**  
  Optimized for mid-range GPUs (e.g., RTX 2050 / 3050) using the lightweight yet powerful Qwen-2.5-3B model.

- **🔒 100% Privacy**  
  No data leaves your device. Everything runs locally using `llama-cpp-python`.

- **🎨 Pro CLI Interface**  
  Hacker-style, color-coded terminal UI with real-time progress tracking.

---

## 📥 Download (Windows App)

Due to GitHub’s file size limits (the AI model is ~2.3 GB), the standalone application is hosted externally.

👉 **[Download Grammer AI v1.0](https://drive.google.com/file/d/1eq-r7LLsQcITFZVyXE48ijvCSX5JU0In/view?usp=drive_link)**

### Installation
1. Download the ZIP file  
2. Extract it completely  
3. Run **`Grammer.exe`**  
4. *No Python or internet connection is required*

---

## 🛠️ Developer Installation (Run from Source)

For developers who want to modify or extend the project.

### 1. Prerequisites
- Python 3.10 or 3.11  
- Git  

### 2. Clone the Repository
```bash
git clone https://github.com/karthiksreenivasanp/Grammer-AI.git
cd Grammer-AI
````

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Model

This project requires the **Qwen-2.5-3B-Instruct** GGUF model.

Steps:

1. Download `qwen2.5-3b-instruct-q4_k_m.gguf` from HuggingFace (≈ 2.3 GB)
2. Create a folder named `models` in the project root
3. Place the `.gguf` file inside `models/`

### 5. Run the Script

```bash
python main.py
```

---

## 🏗️ How to Build (Create EXE)

You can package the application yourself using **PyInstaller**.

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Run the Build Command

```powershell
pyinstaller --noconfirm --onedir --name "Grammer" --icon "logo.ico" --collect-all llama_cpp_python --add-data "models/qwen2.5-3b-instruct-q4_k_m.gguf;models" main.py
```

### 3. Restore Library Files (If Needed)

If the app closes immediately after building:

* Copy the `lib` folder from
  `Python/site-packages/llama_cpp`
* Paste it into
  `dist/Grammer/_internal/llama_cpp`

---

## ⚠️ Disclaimer

This tool is intended for **educational and research purposes only**.
The developer does **not** endorse academic dishonesty, plagiarism, or violation of institutional policies.

Always review and edit the generated output before submission.

---

### 👤 Author

**Created by [Karthik Sreenivasan P](https://github.com/karthiksreenivasanp)**


