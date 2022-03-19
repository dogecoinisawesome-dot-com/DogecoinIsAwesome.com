# Dogecoin Full Node on a Raspberry Pi

A Raspberry Pi is a great way to run a Dogecoin full node.

In this guide, we’ll setup a headless (no GUI) Dogecoin full node to run on a Raspberry Pi 4.

[TOC]

## Why Run a Dogecoin Node?

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

On Windows:

1.  Download and install [PuTTY](https://www.putty.org/).
1.  Launch PuTTYgen.
1.  Select the option _EdDSA_.
1.  Click _Generate_.
1.  Enter a _Key passphrase_.
1.  Save the output in _Public key for pasting into OpenSSH authorized_keys file_, we'll use this in the next section.
1.  Click _Save private key_ and save the private key in `ppk` format somewhere on your computer.

    ![PuTTYgen](images/full-node-raspberry-pi/puttygen.png)

### Install Raspberry Pi OS

#### Write Raspberry Pi OS to a USB Stick

1.  Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and plug in a USB stick to your computer.
1.  Click on _Choose Storage_ and select the USB stick.
1.  Click on _Choose OS_, go to _Raspberry Pi OS (Other)_ and select _Raspberry OS Lite (32-bit)_.
1.  Click on the _Advanced Options_ icon and configure the following settings:
    - Set _Image customization options_ to _always use_.
    - Set _Enable SSH_, _Allow public-key authentication only_, and paste the public key generated in PuTTYgen into _Set authorized keys for 'pi'_.
    - Set a password for the `pi` user.
    - Optionally, disable telemetry, select locale, and configure WiFi credentials.
      ![PuTTYgen](images/full-node-raspberry-pi/raspberry-pi-imager-options.png)
1.  Click on _WRITE_.
1.  Once the image is written to the USB stick eject it from your computer and plug it into the Argon One M.2 case.
1.  Press the power button on the Argon One case, Raspberry Pi OS will boot now from the USB stick.

#### Clone Raspberry Pi OS to Internal SSD

1.  `git clone https://github.com/billw2/rpi-clone.git`
1.  `sudo cp rpi-clone rpi-clone-setup /usr/local/sbin`
1.  `sudo rpi-clone sda`

        Booted disk: sdb 7.9GB Destination disk: sda 240.1GB
        ---------------------------------------------------------------------------
        Part Size FS Label Part Size FS Label
        1 /boot 256.0M fat32 --
        2 root 7.1G ext4 rootfs
        ---------------------------------------------------------------------------
        == Initialize: IMAGE partition table - partition number mismatch: 2 -> 0 ==
        1 /boot (48.0M used) : MKFS SYNC to sda1
        2 root (1.4G used) : RESIZE MKFS SYNC to sda2
        ---------------------------------------------------------------------------
        Run setup script : no.
        Verbose mode : no.
        -----------------------:
        ** WARNING ** : All destination disk sda data will be overwritten!
        -----------------------:

        Initialize and clone to the destination disk sda?  (yes/no): yes
        Optional destination ext type file system label (16 chars max): raspberry-pi

1.  Once cloning is done, run `sudo shutdown -h now` and remove the USB stick from the Argone One case.

Power up the Argone One, Raspberry Pi OS will now boot from internal disk.
