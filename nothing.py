import cv2
import mediapipe as mp
import time
from collections import deque

mp_face_detection = mp.solutions.face_detection

cap = cv2.VideoCapture(0)

prev_time = 0
fps_history = deque(maxlen=10)

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
        prev_time = curr_time

        fps_history.append(fps)
        avg_fps = sum(fps_history) / len(fps_history)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x_min = int(bbox.xmin * w)
                y_min = int(bbox.ymin * h)
                box_w = int(bbox.width * w)
                box_h = int(bbox.height * h)

                margin_w = int(box_w * 0.2)
                margin_h = int(box_h * 0.2)

                x_min = max(0, x_min - margin_w // 2)
                y_min = max(0, y_min - margin_h // 2)
                box_w = min(w - x_min, box_w + margin_w)
                box_h = min(h - y_min, box_h + margin_h)

                cv2.rectangle(frame, (x_min, y_min), (x_min + box_w, y_min + box_h), (0, 0, 0), -1)

        cv2.putText(frame, f"FPS: {int(avg_fps)}", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Nothing", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
