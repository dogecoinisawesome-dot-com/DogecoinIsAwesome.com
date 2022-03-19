# Dogecoin Full Node on a Raspberry Pi

A Raspberry Pi is a great way to run a Dogecoin full node.
In this guide, we’ll setup a headless (no GUI) Dogecoin full node to run on a Raspberry Pi 4.

[TOC]

## Why Should I Run a Dogecoin Node?

There is no monetary incentive for running a Dogecoin.
However, there are still benefits to running a Dogecoin node such as:

- Privacy and security; Transacting with the Dogecoin blockchain directly via a full node wallet, or using a wallet connected to a full node that you own, allows you to send and receive Dogecoin transactions in a trustless manner and avoids you having to go through third-party nodes.
- Educational; Learn Dogecoin development using the most secure Dogecoin interface, `dogecoind`.
- Support the network; Full nodes keep the Dogecoin blockchain decentralized, and protect the ecosystem from bad actors by reducing the need for trust.[^full_node_question]

[^full_node_question]: [https://www.reddit.com/r/BitcoinBeginners/comments/3eq3y7/full_node_question/ctk4lnd/](https://www.reddit.com/r/BitcoinBeginners/comments/3eq3y7/full_node_question/ctk4lnd/)

## Build a Custom Raspberry Pi

![Argon One M.2 Raspberry Pi 4 Case](images/full-node-raspberry-pi/argon40-case.jpg)

### Requirements

To build the custom Raspberry Pi pictured above you’ll need:

- Raspberry Pi 4 Model B - 8GB
- Argon One M.2 Raspberry Pi 4 Case
- Argon One Pi 4 Power Supply (Raspberry Pi)
- WD Green 240GB M.2 Internal SSD
- Cat6A Shielded Snagless RJ45 Ethernet Cable - 2m
- USB stick

Instructions on how to mount the parts can be found on [YouTube](https://youtu.be/Tgrka088ZFk).

### Issues

While I generally recommend this custom setup, there were a few unfortunate issues I ran into:

- The case took over a month and a half to arrive from China and upon arrival I had to pay a customs fee. I purchased the case through the official website.
- The female end of the SSD screw snapped in two when I tried to mount the SSD and I ended up having to tape the SSD down. Be gentle while screwing in the SSD!

## Raspberry Pi Setup

### Generate SSH Keys

In order to connect to the Raspberry Pi securely via SSH, you will have to generate a public/private key pair.
On a Windows computers:

1. Download and install [PuTTY](https://www.putty.org/).
1. Launch PuTTYgen.
1. ![PuTTYgen](images/full-node-raspberry-pi/puttygen.png)
1. Select the option _EdDSA_.
1. Click _Generate_.
1. Enter a _Key passphrase_.
1. Save the output in _Public key for pasting into OpenSSH authorized_keys file_, we'll use this in the next section.
1. Click _Save private key_ and save the private key in `ppk` format somewhere on your computer.

### Install Raspberry Pi OS

1. Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and plugin a USB stick to your computer.
1. Click on _Choose Storage_ and select the USB stick.
1. Click on _Choose OS_, go to _Raspberry Pi OS (Other)_ and select _Raspberry OS Lite (32-bit)_.
