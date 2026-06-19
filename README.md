1 AI Image or Text Recognition

This project is a simple Project 4 implementation for **Image or Text Recognition (Basic)**.

The application takes an image as input, cleans the image using basic OpenCV pre-processing, runs OCR using Tesseract through `pytesseract`, and saves the recognized text clearly in the `outputs` folder.

2 Project Goal

Implement a basic image or text recognition task using available AI/computer vision libraries.

3 Features

- Accepts an image path from the user
- Uses a default sample image if no path is entered
- Converts image to grayscale
- Reduces noise with Gaussian blur
- Applies adaptive thresholding
- Extracts text using OCR
- Saves a processed image
- Saves recognized text in a report file
- Uses a clean and simple Python structure



4 Technologies Used

- Python
- OpenCV
- Pytesseract
- Pillow
- NumPy

5 Install Tesseract OCR

This project needs the Tesseract OCR engine installed on your computer.

For Windows, the common install path is:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```





6 User Input Example

When the program asks for image path, press Enter to use the default image:

```text
Image path:
```

Or give your own image path:



7 Output

After running the project, check the `outputs` folder.

It will contain:

```text
processed_image.png
recognized_text.txt
```

8 Learning Outcomes

This project demonstrates:

- Image loading
- Image pre-processing
- OCR library integration
- Recognition output handling
- Simple AI workflow using Input, Process, and Output

9 Future Improvements

- Add object detection using MobileNet-SSD
- Add OCR confidence score filtering
- Add support for multiple images
- Add a simple web interface
- Export results into CSV

