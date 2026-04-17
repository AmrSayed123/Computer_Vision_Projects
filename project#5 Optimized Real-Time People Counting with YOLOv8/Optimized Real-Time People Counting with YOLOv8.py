import cv2
from ultralytics import YOLO

# 1. Load the YOLOv8 Nano model (lightweight for real-time performance)
model = YOLO(yolov8n.pt)

try
    # 2. Initialize Video Capture (0 for default webcam)
    path = 0
    cap = cv2.VideoCapture(path)

    # Check if camera opened successfully
    if not cap.isOpened()
        print(Error Could not open video source.)
        exit()

    while True
        ret, frame = cap.read()
        if not ret
            break

        # 3. Streamlined Detection
        # 'classes=[0]' tells YOLO to only detect people (COCO class 0)
        # 'conf=0.5' filters out weak detections for better accuracy
        results = model(frame, classes=[0], conf=0.5, verbose=False)
        
        # 4. Access the boxes from the first result
        detections = results[0].boxes
        person_count = len(detections) # Simply count the number of boxes found

        # 5. Draw bounding boxes for each detected person
        for det in detections
            # Extract coordinates (x1, y1, x2, y2)
            x1, y1, x2, y2 = map(int, det.xyxy[0])
            
            # Draw green rectangle around the person
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, Person, (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 6. Display the total count on the top-left corner
        # Using a background rectangle for better text readability
        cv2.rectangle(frame, (10, 10), (250, 60), (0, 0, 0), -1) 
        cv2.putText(frame, fPeople Count {person_count}, (20, 45), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # 7. Show the processed frame
        cv2.imshow(Optimized People Counting App, frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q')
            break

finally
    # 8. Safely release hardware resources
    cap.release()
    cv2.destroyAllWindows()