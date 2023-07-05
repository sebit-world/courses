# Object Detection

## Using Mobilenet-V2

[91 class labels](ssd_coco_labels.txt)

```bash
cd /jetson-inference/build/aarch64/bin

./detectnet.py --network=ssd-mobilenet-v2 /dev/video0
```

## Detection with custom logic

```bash
cd /jetson-inference/data/codes

python3 demo.py --network=ssd-mobilenet-v2 /dev/video0
```

## Exerciese: Implement custom logic

### Goal

Turn on the relay channels base on the following conditions:

- If no “person” detected → turn **OFF** both channels
- If more than zero & less than or equal to three “person” detected → turn **ON** channel 1 & turn **OFF** channel 2
- If more than three “person” detected → turn **ON** both channels

### Edit & Run the detection with custom logic

**Open a new terminal**, edit the script:

```bash
cd /home/nano/jetson-inference/data/codes/

gedit detectnet.py
```

**Go back to the terminal inside the environment**, to start the code:

```bash
cd /jetson-inference/data/codes/

python3 detectnet.py --network=ssd-mobilenet-v2 /dev/video0
```
