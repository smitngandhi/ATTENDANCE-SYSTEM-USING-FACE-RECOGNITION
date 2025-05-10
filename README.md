
# Face Recognition Attendance System

This is a Python-based project that utilizes the `face_recognition` library to mark attendance based on face detection. The system captures live video, detects faces, and records the attendance of identified individuals in a CSV file.

## Prerequisites

1. Python 3.x (preferably Python 3.8 or higher).
2. A webcam for capturing video input.

## Installation

### Step 1: Set Up a Virtual Environment

Before installing the dependencies, it's best practice to create a virtual environment. To do this, run the following commands:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Step 2: Install CMake

The `dlib` library, which is required for face recognition, requires CMake for installation. You can install CMake using the following steps:

- For Windows, you can use Chocolatey:
  ```bash
  choco install cmake
  ```

- For Ubuntu/Debian-based systems:
  ```bash
  sudo apt-get install cmake
  ```

### Step 3: Install Required Libraries

Once the virtual environment is activated and CMake is installed, install the necessary Python packages:

1. Install `dlib`:
   ```bash
   pip install dlib
   ```

2. Install `face_recognition`:
   ```bash
   pip install face_recognition
   ```

### Step 4: Set Up the Dataset

Make sure you have the dataset with images of students in the `Test_Photos` folder (you can customize the folder path in the code). Each image should be named with the student's name (e.g., `John_Doe.jpg`). The images should be in one of the following formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, or `.gif`.

### Step 5: Running the Attendance System

After installing the dependencies and setting up the dataset, run the attendance system:

```bash
python attendance.py
```

This will start the video capture from your webcam and begin recognizing faces. When a face is detected, it will compare the face encoding with the images in your dataset. If a match is found, the student’s name is recorded in a CSV file along with the current time.

### Step 6: Exit the System

To exit the system, press the 'q' key on the video window.

### Output

The system will generate an attendance CSV file with the following format:
```
Name, Time
John_Doe, 12-04-2025 08:30:45
Jane_Smith, 12-04-2025 08:31:10
```

### Troubleshooting

1. **Error: `ModuleNotFoundError: No module named 'face_recognition'`**
   - Ensure that you have activated the virtual environment and installed the dependencies.

2. **Error: `CMake is not installed`**
   - Install CMake using the instructions provided above.

3. **Error: `Failed to build dlib`**
   - Ensure that CMake is installed and added to your system's PATH.
   
### Additional Notes

- The system assumes that each student has only one image for recognition.
- You can adjust the face detection frequency by modifying the `s` flag in the code.
- The attendance data is saved in a CSV file with the current date.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
