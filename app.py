from flask import Flask, render_template, request, url_for
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['PROCESSED_FOLDER'] = 'static/processed/'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    image_file = request.files.get("image")
    if image_file:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_path)
        return render_template("index.html", image_url=url_for('static', filename="uploads/" + image_file.filename))
    return render_template("index.html", error="No file selected.")

@app.route("/edit", methods=["POST"])
def edit_image():
    action = request.form.get("action")
    uploaded_images = os.listdir(app.config['UPLOAD_FOLDER'])
    if not uploaded_images:
        return render_template("index.html", error="No uploaded image found.")

    uploaded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_images[0])
    image = Image.open(uploaded_image_path)
    processed_path = os.path.join(app.config['PROCESSED_FOLDER'], "processed_image.jpg")

    try:
        
        if action == "grayscale":
            image = image.convert("L")
        elif action == "flip":
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif action == "rotate":
            image = image.rotate(90, expand=True)
        elif action == "sepia":
            sepia_image = ImageEnhance.Color(image).enhance(0.3)
            sepia_image = sepia_image.convert("RGB")
            image = sepia_image
        elif action == "blur":
            image = image.filter(ImageFilter.GaussianBlur(5))
        elif action == "crop":
            width, height = image.size
            image = image.crop((0, 0, width // 2, height // 2))
        elif action == "rgb_to_binary":
            image = np.array(image.convert("L"))  # Convert to grayscale first
            threshold = 128
            binary_image = (image > threshold) * 255  # Binarize
            image = Image.fromarray(binary_image.astype('uint8'))
        elif action == "rgb_to_index":
            image = np.array(image.convert("RGB"))
            indexed_image = np.dot(image, [0.2989, 0.587, 0.114])  # Simplified index
            indexed_image = (indexed_image / indexed_image.max() * 255).astype('uint8')
            image = Image.fromarray(indexed_image)
        elif action == "sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif action == "edge_detect":
            image = image.filter(ImageFilter.FIND_EDGES)

        # Convert image to RGB if it is in RGBA or any mode that does not support JPEG
        if image.mode in ("RGBA", "LA"):
            image = image.convert("RGB")

        # Save the processed image
        image.save(processed_path, "JPEG")

    except Exception as e:
        return render_template("index.html", error=f"An error occurred: {e}")

    return render_template(
        "index.html", 
        image_url=url_for('static', filename="uploads/" + os.path.basename(uploaded_image_path)),
        processed_image_url=url_for('static', filename="processed/processed_image.jpg")
    )

if __name__ == "_main_":
    app.run(debug=True)