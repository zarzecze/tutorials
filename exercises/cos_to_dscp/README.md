# CoS to DSCP mapping

## Introduction
The objective of this tutorial is to implement 802.1q CoS to IPv4 DSCP mapping.
https://www.cisco.com/c/en/us/support/docs/smb/routers/cisco-rv-series-small-business-routers/smb1295-map-class-of-service-cos-settings-to-differentiated-services.html

802.1q frame format is described here: https://en.wikipedia.org/wiki/IEEE_802.1Q#Frame_format
You need to map field PCP (CoS priority) in ethernet 802.1q header to field DSCP in IPV4 Header https://en.wikipedia.org/wiki/IPv4#Header

## Step 1: Fill *TODOs* 

Your job will be to do the following:

1. **TODO:** Add missing fields to ethernet 802.1q header definition
2. **TODO:** Define action that takes dscp priority as parameter and sets diffserv in ipv4 header to this value
3. **TODO:** Define table that takes search for CoS priority and launches an action created above with proper parameter
4. **TODO:** Add entries to a table declared above in `s1-runtime.json`

If you have some problems you can check folder `solution` to see an example solution.


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