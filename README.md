# Real-Time-Video-Object-Detection-with-YOLOv8

<h2>📌 Project Description</h2>

<p>
  This project is a custom object detection system built with 
  <strong>YOLOv8</strong> and <strong>OpenCV</strong>.
  The goal is to detect <strong>plastic bags</strong> in images, videos,
  and real-time webcam streams.
</p>

<p>
  A custom dataset was collected from Kaggle, annotated using Roboflow,
  and trained on Google Colab. The final model can identify plastic bags
  and draw bounding boxes with confidence scores.
</p>

<h2>🎥 Demo</h2>

<p>
  Real-time plastic bag detection using YOLOv8 and OpenCV.
</p>

<a href="demo/demo.mp4">Watch Demo Video</a>
<a href="demo/demo.mp4">
  <img src="results/result.png" width="600">
</a>


<h2>🚀 Features</h2>
<ul>
  <li>eal-time webcam object detection</li>
  <li>Custom YOLOv8 model training</li>
  <li>Plastic bag detection</li>
  <li>OpenCV webcam integration</li>
  <li>Bounding box visualization</li>
  <li>Confidence score display</li>
  <li>Video and image prediction support</li>
</ul>


<h2>🛠️ Technologies Used</h2>

<p align="center">

  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="70">

  

  <img src="https://opencv.org/wp-content/uploads/2020/07/OpenCV_logo_no_text_.png" width="70">

  

  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="70">

  

  <img src="https://avatars.githubusercontent.com/u/26833451?s=200&v=4" width="70">

  

</p>

<p align="center">
  Python &nbsp;&nbsp; OpenCV &nbsp;&nbsp; YOLOv8 &nbsp;&nbsp; Roboflow
</p>


<h2>📂 Project Structure</h2>

<pre>
Real-Time-Video-Object-Detection-with-YOLOv8/
│
├── demo/
│   └── demo.mp4
│
├── datasets/
│   └── .gitkeep
│
├── Model/
│   └── best.pt
│
├── results/
│   └── result.png
│
├── test.py
├── results.py
├── requirements.txt
├── README.md
└── 
</pre>

<h2>⚙️ Installation</h2>

<pre>
# Clone repository
git clone https://github.com/hbakaz693/Real-Time-Video-Object-Detection-with-YOLOv8

# Go to project folder
cd Real-Time-Video-Object-Detection-with-YOLOv8

# Create virtual environment
py -3.11 -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
</pre>

<h2>▶️ Usage</h2>

<h3>Run Real-Time Webcam Detection</h3>

<pre>
python test.py
</pre>

<h3>Run Image Detection</h3>

<pre>
python results.py
</pre>

<p>
The model will detect plastic bags and display bounding boxes with confidence scores.
</p>



<h2>📊 Results</h2>

<p>
The custom YOLOv8 model achieved high detection accuracy for real-time plastic bag detection.
</p>

<table>
  <tr>
    <th>Metric</th>
    <th>Value</th>
  </tr>

  <tr>
    <td>Precision</td>
    <td>0.996</td>
  </tr>

  <tr>
    <td>Recall</td>
    <td>1.000</td>
  </tr>

  <tr>
    <td>mAP50</td>
    <td>0.995</td>
  </tr>

  <tr>
    <td>mAP50-95</td>
    <td>0.804</td>
  </tr>
</table>

<br>

<img src="results/result.png" width="700">


<h2>📈 Model Performance</h2>

<p>
  The model was trained for 20 epochs using YOLOv8 on a custom plastic bag dataset.
</p>

<ul>
  <li>Final Precision: <strong>99.6%</strong></li>
  <li>Final Recall: <strong>100%</strong></li>
  <li>mAP50: <strong>99.5%</strong></li>
  <li>mAP50-95: <strong>80.4%</strong></li>
</ul>

<h2>🚀 Future Improvements</h2>

<ul>
  <li>Add more images to improve generalization</li>
  <li>Train the model on more plastic waste types</li>
  <li>Deploy the model in a web or mobile application</li>
  <li>Improve real-time detection speed</li>
</ul>

<h2>👤 Author</h2>

<p>
  <strong>Hicham Bakaz</strong><br>
  Master Student in Data Science & Artificial Intelligence
</p>
