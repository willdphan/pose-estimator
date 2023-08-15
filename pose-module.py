import cv2
import mediapipe as mp
import time
import math

class poseDetector():
    def __init__(self, mode=False, model_complexity=1, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.model_complexity = model_complexity
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        # utils to draw land marks and connections on image
        self.mpDraw = mp.solutions.drawing_utils
        # creating a reference mpPose to the pose module in the solutions namespace of the media pipe library.
        self.mpPose = mp.solutions.pose
        # initialize pose object with mpPose above. Math named params to created params
        self.pose = self.mpPose.Pose(static_image_mode=self.mode, model_complexity=self.model_complexity, smooth_landmarks=self.smooth, min_detection_confidence=self.detectionCon, min_tracking_confidence=self.trackCon)

    # draw means to display on image
    def findPose(self, img, draw=True):
        # convert image/vid to color
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # process imgRGB with pose object
        results = self.pose.process(imgRGB)
        # if results...
        if results.pose_landmarks:
               #  checks the value of the draw argument provided to the findPose function. if landmarks are present...
            if draw:
                # use mpDraw object to draw_landmarks. params include image, results of pose_landmarks from above, 
                # connect key points with mpPose and POSE_CONNECTIONS from mediapipe library
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            # return img
            return img

            # # for every index and landmark that corresponds
            # for id, lm in enumerate(results.pose_landmarks.landmark):
            #     # grab height, width, channels
            #     h, w, c = img.shape
            #     # print id and the landmark val
            #     print(id, lm)
            #     # convert to ints
            #     cx, cy = int(lm.x * w), int(lm.y * h)
            #     # circles drawn on landmark
            #     cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        

# plays the dummy code/preview
def main():
    # grab video
    cap = cv2.VideoCapture('PoseVideos/1.mp4')
    # if you cannot grab video...
    if not cap.isOpened():  # Check if the video was opened successfully
        print("Error: Could not open video.")
        return
    # initialize past time
    pTime = 0
    # initialize detector var with poseDetector() class
    detector = poseDetector()

    while True:
        # returns success and image
        success, img = cap.read()
        # call the findPose() func, func returns img
        img = detector.findPose(img)

        # calc fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        # position of fps
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)
        # show image
        cv2.imshow("Image", img)
        # wait 1 ms
        cv2.waitKey(1)

if __name__ == "__main__":
    main()