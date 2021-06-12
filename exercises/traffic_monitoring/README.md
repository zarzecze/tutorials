# Traffic monitoring
In this exercise, you will implement type of traffic monitoring where you can display your network status depending on time window you define.
To do this we will use counters with custom Control Plane.


## How to run the excercise:

1. In your shell run:
```
make run
```
2. You should now see a Mininet command prompt. Now please run command that will simulate traffic between two hosts:
```
h1 ./send.py h2
```
3. Open second terminal and run:
```
./counter.py
```

## How to do excercise:

Code above will work correctly when you will fill properly all TODOs left in the code of [counter.py](./counter.py) and [traffic_monitoring.p4](./traffic_monitoring.p4) 

If you encounter any probles you can help yourself with files in soultion folder.
