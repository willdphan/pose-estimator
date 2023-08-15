# Pose Estimator

## Overview

The provided code leverages the `mediapipe` library to detect and track body poses in real-time, either from camera feeds or video files. This real-time pose detection extracts key landmarks on the body and visualizes them on the video feed. The program also calculates and displays the frames per second (FPS) to monitor performance.

## Features

**Pose Detector Class**

Organized for reusability and easier integration into other projects.

Detects body poses and visualizes the landmarks and their connections.

[Module](pose-module.py)
<br/>

**Real-time FPS Calculation**

Allows for performance and processing speed monitoring.

**Simple Script**

A standalone version that reads a video feed and estimates body poses without the need for a class structure.

[Script](pose.py)
<br/>

## Usage

**Prerequisites**

Install the required libraries:

`pip install opencv-python mediapipe`

**Execution**

Run the scripts using:

`python pose-module.py`

or

`python pose.py`

---

## Note

Ensure you have a working camera or a valid video file path.
Adjust the `cv2.VideoCapture('PoseVideos/3.mp4')` parameter depending on which source you want to use.
Check for the availability of the video file before processing to avoid runtime errors.

---

## License

This script is open-source and is licensed under the MIT License. For more information, consult the [LICENSE](LICENSE) file.
