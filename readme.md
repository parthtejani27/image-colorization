# Image Colorization Web Application

A Flask-based web application that colorizes black and white images using deep learning with a Caffe model.

## Features

- Convert black and white images to color using deep learning
- User authentication and profile management
- Image upload and gallery view
- Dashboard to view colorization results
- Share colorized images with other users

## Example Results

Before and After Colorization:

![Sample Output](https://github.com/user-attachments/assets/20c2efbd-4f4e-40d0-8940-ec291a923d01)

## Prerequisites

- Python 3.11 or higher
- Flask framework
- OpenCV (cv2)
- Caffe model and dependencies
- Additional Python packages listed in requirements.txt

## Installation

1. Clone the repository:

```bash
git clone https://github.com/parthtejani27/image-colorization.git
cd colorize-image-main
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Download the pre-trained Caffe model:

   - Download from: [Pre-trained Model](https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1)
   - Place the downloaded file in the `model` folder

4. Setup the project structure:

```
colorize-image-main/
├── my_project/
│   ├── model/
│   ├── static/
│   │   ├── input_pics/
│   │   └── output_pics/
│   ├── templates/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
├── requirements.txt
└── run.py
```

## Usage

1. Start the Flask application:

```bash
python run.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Register for an account or login if you already have one

4. Upload a black and white image through the web interface

5. View the colorized result in your dashboard

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- Database: SQLite
- Image Processing: OpenCV, Caffe Model
- Deep Learning Framework: Caffe

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- Based on the research paper "Colorful Image Colorization" by Zhang et al.
- Caffe model implementation inspired by various open source contributions
