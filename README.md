# ColorAssist

**ColorAssist** is a user-friendly tool designed to assist color-blind individuals, web developers, and anyone in need of precise color identification. By analyzing the color under your mouse pointer, it provides the color’s name, RGB values, and HEX code in real time, making it an invaluable resource for accessibility and design.

---

## What is this project?

The **ColorAssist** application continuously tracks your mouse pointer and identifies the color beneath it. It leverages a carefully curated color dataset to deliver exact color names and their corresponding HEX and RGB values. The tool’s goal is to ensure accurate color recognition and facilitate the work of developers, designers, and anyone with color vision deficiencies.

### Key features:
- **Real-time color detection:** Continuously displays the color under your cursor.  
- **Precise color names:** Matches color names from a pre-defined, highly accurate dataset.  
- **User-friendly interface:** Designed to be intuitive, allowing easy access to color data.  
- **Inclusive for all users:** A helpful resource for both color-blind individuals and web professionals.

---

## Requirements

To run this project locally, ensure you have:
- **Python:** Version 3.6 or higher.  
- **Required Python libraries:**
  - numpy
  - pandas
  - opencv-python
  - pyautogui
  - tkinter (standard with Python)

You can install the dependencies by running:

+ Install dependencies:
 
```bash
pip install -r requirements.txt
```

## How to Use
## STEP 1: Clone the repository

Use Git to download the project locally:

```bash
git clone https://github.com/arvind88765/ColorAssist.git
```

## STEP 2: Navigate to the project directory
- Change to the project’s root folder:
  
```bash
cd ColorAssist
```

## STEP 3: Install the required dependencies
Install all necessary Python packages:

```bash
pip install -r requirements.txt
```

## STEP 4: Run the application
- Start the tool:

```bash
python app.py
```

## STEP 5: Access the application
Once running, move your mouse pointer, and the application will display:

The name of the color beneath the pointer.
Its corresponding RGB values.
The HEX code for the color.





