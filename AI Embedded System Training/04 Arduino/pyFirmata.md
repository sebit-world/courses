# Enrichment: pyFirmata

## Using Python to control Arduino Board

```bash
cd /home/nano/jetson-inference
```

```bash
sudo ./start.sh
```

```bash
cd /jetson-inference/data/codes/pyfirmata
```

### Start demo1

```bash
python3 demo1.py
```

### Start demo2

```bash
python3 demo2.py
```

### Start demo3

```bash
python3 demo3.py
```

### Start demo4

```bash
python3 demo4.py
```

## Bonus Exercise Obejct Detection & Arduino

```bash
cd /jetson-inference/data/codes/pyfirmata
```

### Start sample code

```bash
python3 detectnet_led.py --network=ssd-mobilenet-v2 /dev/video0
```

### Edit bonus_exercise.py

Open a new Terminal

```bash
cd /home/nano/jetson-inference/data/codes/pyfirmata
```

```bash
gedit bonus_exercise.py
```

Switch to the docker terminal, run the bonus_exercise.py

```bash
cd /jetson-inference/data/codes/pyfirmata
```

```bash
python3 bonus_exercise.py --network=ssd-mobilenet-v2 /dev/video0
```
