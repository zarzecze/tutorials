# BPDU frame filtering

## Introduction
The objective of this tutorial is to create mechanism for blocking incoming BPDU frames arriving at certain ports of the switch.
https://www.ciscopress.com/articles/article.asp?p=2995351&seqNum=3

BPDU frames used in Spaning Tree Protocol have very interessting characteristic as they always have their destination address set to `01:80:C2:00:00:00` this makes the easy to detect and block/forward/proccess the frame.
Cisco Per VLAN Spanning Tree uses diffrent destination mac address `01:00:0C:CC:CC:CD`
## Step 1: Fill *TODOs* 

Your job will be to do the following:

1. **TODO:** In `block_bpdu.p4` create table definition that will contain definition of BPDU frames
2. **TODO:** In `block_bpdu.p4` apply the table and if frame was matched explicitly drop the frame
3. **TODO:** In `s1-runtime.json` and `s2-runtime.json` add entries to the tables to drop all BPDU frames coming from host respectivly h1 nad h2. (We don't want them to become root of the spanning tree ;) )

## Step 2: Run program
In your shell, run:
 ```bash
   make
```
This will:
* compile `block_bpdu.p4`, and

* start a Mininet instance with two switches (`s1` `s2`) connected to
    two hosts (`h1`, `h2`).
* The hosts are assigned IPs of `10.0.1.1` and `10.0.2.2`.
  

Open **Wireshark** and select `s1-eth1` interface to monitor if you sent correct BPDU frame.

Then, you can run
```bash
   h1 ./send_bpdu.py
```
To send sample BPDU frame packet from `h1` to `s1` switch.
Then, you can check on `Wiresharks` if your is in fact BPDU.
You can confirm that BPDU frame has been detected and explicitly blocked by greping the log file.

```
cat logs/s1.log  | grep "Table 'MyIngress.drop_mac_bpdu_exact': hit" -A 9
```
