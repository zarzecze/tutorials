# BPDU frame filtering

## Introduction
The objective of this tutorial is to create mechanism for blocking incoming BPDU frames arriving at certain ports of the switch.
https://www.ciscopress.com/articles/article.asp?p=2995351&seqNum=3

## Step 1: Fill *TODOs* 
You need to fill *TODOs* in files [`block_bpdu.p4`, `s1-runtime.json`, `s2-runtime.json`] and that will detect and block BPDU frame. If you have some problems you can check folder `solution` to see an example solution.

## Step 2: Run program
In your shell, run:
 ```bash
   make
```
This will:
* compile `block_bpdu.p4`, and

* start a Mininet instance with one switches (`s1`) connected to
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

