# Exercise 2

## Object Detection Customization Example

```bash
cd /jetson-inference/data/codes

python3 detectnet_relay.py --network=ssd-mobilenet-v2 /dev/video0
```

## Exercise: Object Detection Custom Logic

1. Open a new Terminal
2. Create exercise2.py

```bash
cd /home/nano/jetson-inference/data/codes/
cp detectnet_relay.py exercise2.py
gedit exercise2.py
```

3. In the docker terminal, run the exercise2.py

```bash
cd /jetson-inference/data/codes/
python3 exercise2.py --network=ssd-mobilenet-v2 /dev/video0
```
