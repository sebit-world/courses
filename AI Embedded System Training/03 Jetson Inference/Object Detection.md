# Object Detection

## Using Mobilenet-V2

[91 class labels](ssd_coco_labels.txt)

```bash
cd /jetson-inference/build/aarch64/bin

./detectnet.py --network=ssd-mobilenet-v2 /dev/video0
```
