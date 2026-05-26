from ultralytics import YOLO

model=YOLO("Model/best.pt")

results=model.predict(
    source="(144).png",
    save=True,
    conf=0.75
)

print("Detection termine")