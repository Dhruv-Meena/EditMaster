# EditMaster: Interactive Image Enhancement Tool

EditMaster is a web-based image editing application that enables real-time enhancement of images with simple, intuitive controls. Built using **Flask (Python)** and **HTML/CSS/JS**, it supports various image processing features like filters, cropping, transformations, and effects.

---

## 🚀 Features

- Upload and preview images in real-time  
- Apply various filters:
  - Grayscale
  - Sepia
  - Flip (horizontal)
  - Rotate (90°)
  - Blur
  - Crop
  - RGB to Binary
  - RGB to Indexed
  - Sharpen
  - Edge Detection
- Download the processed image
- Intuitive, responsive UI
- Works directly from the browser

---

## 🧠 Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Libraries:** PIL (Pillow), NumPy

---

## 📁 Project Structure

EditMaster/
├── app.py # Flask backend
├── templates/
│ └── index.html # Main HTML page
├── static/
│ ├── uploads/ # Uploaded images
│ ├── processed/ # Output images
│ ├── style.css # CSS file
│ └── script.js # JS for interactivity

## 🔧 Installation & Run Locally

1. Clone the repository:
   git clone https://github.com/your-username/EditMaster.git
   cd EditMaster

2. Set up the virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install required libraries:
  pip install -r requirements.txt

4.Run the app:
  python app.py

5.Visit in Browser:
   http://127.0.0.1:5000
