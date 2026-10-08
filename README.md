# Vehicle Density Based Traffic Signal Simulation

A Python and OpenCV prototype that detects vehicles in four still images using pretrained YOLOv4 weights and assigns a green-phase duration to each lane based on its vehicle count. Lanes are served in a fixed sequence, with one green lane per phase.

## Reported example output

These results were reproduced using the supplied YOLOv4 weights and four JPEGs with OpenCV 4.10.0. The two similarly named JPEGs both returned 16 detections; their original lane assignments remain unconfirmed. Annotated validation images are included in `validation_results/`.

| Lane | Detected vehicles | Green phase |
| --- | ---: | ---: |
| 1 | 16 | 45 seconds |
| 2 | 16 | 45 seconds |
| 3 | 4 | 30 seconds |
| 4 | 14 | 30 seconds |

During each phase, the other three lanes are red for the same phase duration. This is not their total red waiting time across the complete cycle.

## Method

1. Read one image for each lane.
2. Detect objects using YOLOv4 through OpenCV DNN.
3. Keep COCO car, motorcycle, bus, train and truck classes.
4. Count detected bounding boxes and draw them on the image.
5. Print each simulated signal phase and save annotated images.

| Vehicle count | Green duration |
| --- | ---: |
| 0–14 | 30 seconds |
| 15–29 | 45 seconds |
| 30 or more | 60 seconds |

The cleaned version fills missing boundary cases in the original script and caps durations at 60 seconds. These are prototype rules, not experimentally optimized traffic timings.

## Setup and usage

Requires Python 3.10 or later.

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

Place the matching pretrained `yolov4.weights` file in `dnn_model/`, alongside the included `yolov4.cfg`. Weights are excluded from Git.  This project performs inference with trained weights.

Run with your four lane images:

```bash
python vehicle_counting.py path/to/lane1.jpg path/to/lane2.jpg path/to/lane3.jpg path/to/lane4.jpg
```

Annotated images are saved in `outputs/`. No GUI display is required.

## Project files

- `vehicle_counting.py`: command-line image counting and phase simulation.
- `vehicle_detector.py`: YOLOv4 inference and vehicle filtering.
- `dnn_model/yolov4.cfg`: supplied model configuration.
- `original/`: unchanged source scripts for reference.
- `examples/`: supplied screenshots and images; lane assignments are not confirmed.