# CoS to DSCP mapping

## Introduction
The objective of this tutorial is to implement 802.1q CoS to IPv4 DSCP mapping.
https://www.cisco.com/c/en/us/support/docs/smb/routers/cisco-rv-series-small-business-routers/smb1295-map-class-of-service-cos-settings-to-differentiated-services.html

## Step 1: Fill *TODOs* 
You need to fill *TODOs* in file `cos_to_dscp.p4` that will handle CoS to DSCP mapping. If you have some problems you can check folder `solution` to see an example solution.

## Step 2: Run program
In your shell, run:
 ```bash
   make
```
This will:
* compile `cop_to_dscp.p4`, and

* start a Mininet instance with one switches (`s1`) connected to
    two hosts (`h1`, `h2`).
* The hosts are assigned IPs of `10.0.1.1` and `10.0.2.2`.
  

Open two **Wiresharks** and choose select `s1-eth1` and `s1-eth2` interfaces to monitor both sides of the switch.

Then, you can run
```bash
   h1 ./send.py h2 <priority>
```
to send sample 802.1Q packet from `h1` to `h2`.
Then, you can check on `Wiresharks` if priority is correctly mapped.