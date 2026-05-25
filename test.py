from ultralytics import YOLO
import cv2

model_coco = YOLO("yolov8n.pt")   # classes principales
model_plastic = YOLO("Model/best.pt")   # ta classe plastic_bag

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Détection COCO
    results_coco = model_coco(frame, conf=0.5)
    frame = results_coco[0].plot()

    # Détection plastic_bag
    results_plastic = model_plastic(frame, conf=0.75)
    frame = results_plastic[0].plot()

    cv2.imshow("YOLO COCO + Plastic Bag", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()