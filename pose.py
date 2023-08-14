import cv2
import mediapipe as mp
import time

# utils to draw land marks and connections on image
mpDraw = mp.solutions.drawing_utils
# creating a reference mpPose to the pose module in the solutions namespace of the media pipe library.
mpPose = mp.solutions.pose
# initialize pose object with mpPose above
pose = mpPose.Pose()

# grab video
cap = cv2.VideoCapture('PoseVideos/3.mp4')
# initialize past time
pTime = 0

while True:
    # returns success and image
    success, img = cap.read()
    # convert image/vid to color
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # process imgRGB with pose object
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    # if results...
    if results.pose_landmarks:
        # use mpDraw object to draw_landmarks. params include image, results of pose_landmarks from above, 
        # connect key points with mpPose and POSE_CONNECTIONS from mediapipe library
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        # for every index and landmark that corresponds
        for id, lm in enumerate(results.pose_landmarks.landmark):
            # grab height, width, channels
            h, w, c = img.shape
            # print id and the landmark val
            print(id, lm)
            # convert to ints
            cx, cy = int(lm.x * w), int(lm.y * h)
            # circles drawn on landmark
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    
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