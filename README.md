# Eye Control Mouse

This Python script utilizes computer vision to create an eye-tracking mouse control system. The script uses the MediaPipe library for face mesh detection and PyAutoGUI for mouse control.

## Setup

### Prerequisites

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

### Installation

1. Install the required dependencies:

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/rajiv2004-cloud/Eye-Control-Mouse.git
    cd eye-control-mouse
    ```

## Usage

1. Run the script:

    ```bash
    python eye_control_mouse.py
    ```

2. Adjust the camera to have a clear view of your face.

3. Move your eyes to control the mouse cursor.

4. Blink both eyes simultaneously to perform a click.

## Features

- Real-time eye tracking for mouse control.
- Blink detection for mouse clicks.
- Dynamic adjustment of mouse sensitivity based on eye movement.
- On-screen visualization of eye and click points.

## Customization

- Modify the `screen_x` and `screen_y` variables to adjust the initial mouse cursor position.
- Adjust the sensitivity factor in the mouse movement calculations for personalized control.

## Known Issues

- The script may require fine-tuning for different lighting conditions.
- Blink detection sensitivity may need adjustment based on individual user behavior.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.


## Acknowledgments

- The script uses the [MediaPipe](https://mediapipe.dev/) library for face mesh detection.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) is used for mouse control.

Feel free to customize the README file further based on your project's specific details and requirements.
