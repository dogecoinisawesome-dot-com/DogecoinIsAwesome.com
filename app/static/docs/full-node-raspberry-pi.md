# Running a Dogecoin Full Node on a Raspberry Pi

In this guide, we'll setup a headless (no GUI) Dogecoin full node to run on a Raspberry Pi 4.

[TOC]

## Why Run a Dogecoin Node?

There is no monetary incentive for running a Dogecoin node.

However, there are still many benefits to running a Dogecoin node such as:

- **Privacy and security**. You can transact with the Dogecoin blockchain directly via a full node wallet, or by using a wallet connected to a full node that you own. This allows you to send and receive Dogecoin transactions in a trustless manner and avoids you having to go through third-party nodes.
- **Education**. Learn Dogecoin development using the most secure Dogecoin interface, `dogecoind`.
- **Support the network**. Full nodes keep the Dogecoin blockchain decentralized, and protect the ecosystem from bad actors by reducing the need for trust.[^full_node_question]

[^full_node_question]: [https://www.reddit.com/r/BitcoinBeginners/comments/3eq3y7/full_node_question/ctk4lnd/](https://www.reddit.com/r/BitcoinBeginners/comments/3eq3y7/full_node_question/ctk4lnd/)

## Build a Custom Raspberry Pi

Here is the custom Raspberry Pi we'll be building to run our Dogecoin node:

![Argon One M.2 Raspberry Pi 4 Case](images/full-node-raspberry-pi/argon40-case.jpg)

### Requirements

To build the Raspberry Pi pictured above you’ll need:

- Raspberry Pi 4 Model B - 8GB
- Argon One M.2 Raspberry Pi 4 Case
- Argon One Pi 4 Power Supply (Raspberry Pi)
- WD Green 240GB M.2 Internal SSD
- Cat6A Shielded Snagless RJ45 Ethernet Cable - 2m
- USB stick

Instructions on how to mount the parts can be found on [YouTube](https://youtu.be/Tgrka088ZFk).

### Issues

There are a few issues I ran into with this setup:

- The case took over a month and a half to arrive from China and upon arrival I had to pay a customs fee. I purchased the case through the official website.
- The female end of the SSD screw snapped in two when I tried to mount the SSD and I ended up having to tape the SSD down. Be gentle while screwing in the SSD!

## Raspberry Pi Setup

At this point you should have assembled a custom Raspberry Pi, now it's time to get it running.

### Generate SSH Keys

In order to connect to the Raspberry Pi securely via SSH, you will have to generate a public/private key pair.

On Windows:

1.  Download and install [PuTTY](https://www.putty.org/).
1.  Launch PuTTYgen.
1.  Select the option _EdDSA_.
1.  Click _Generate_.
1.  Enter a _Key passphrase_.
1.  Save the output in _Public key for pasting into OpenSSH authorized_keys file_, we'll use this in the next section.
1.  Click _Save private key_ and save the private key in `ppk` format on your computer.

    ![PuTTYgen](images/full-node-raspberry-pi/puttygen.png)

### Install Raspberry Pi OS

#### Write the Raspberry Pi OS to a USB Stick

1.  Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and plug in a USB stick to your computer.
1.  Click on _Choose Storage_ and select the USB stick.
1.  Click on _Choose OS_, go to _Raspberry Pi OS (Other)_ and select _Raspberry OS Lite (32-bit)_.
1.  Click on the _Advanced Options_ icon and configure the following settings:
    - Set _Image customization options_ to _always use_.
    - Set _Enable SSH_, _Allow public-key authentication only_, and paste the public key generated in PuTTYgen into _Set authorized keys for 'pi'_.
    - Set a password for the `pi` user.
    - Optionally, disable telemetry, select locale, and configure WiFi credentials.
      ![PuTTYgen](images/full-node-raspberry-pi/raspberry-pi-imager-options.png)
1.  Click on _SAVE_ and then _WRITE_.
1.  Once the image is written to the USB stick eject it from your computer and plug it into the Argon One M.2 case.
1.  Press the power button on the Argon One case, the Raspberry Pi OS should now boot from USB.

#### Connect to the Raspberry Pi

To connect to your Raspberry Pi via SSH:

1.  Find the IP address of your Raspberry Pi.

    The easiest way to do this is to login to your router (e.g., [http://192.168.1.1/](http://192.168.1.1/)):
    ![PuTTYgen](images/full-node-raspberry-pi/raspberry-pi-ip-address.png)

1.  Launch PuTTY and configure the following settings:

    - Enter the IP address into _Host Name (or IP address)_

          ![PuTTYgen](images/full-node-raspberry-pi/putty-configuration.png)

    - Go to _Connections_, _SSH_, _Auth_, and _Browse_ for the private key you created in PuTTYgen.
    - Go back to _Session_, click _Save_ and _Open_.

1.  You will be prompted for a username, enter `pi`, next enter the password for your SSH key.

1.  You should now be logged in.

_Optional_: If you would like to have a prettier PuTTY console, follow the instructions for installing [Pretty PuTTY](https://github.com/jacektrocinski/pretty-putty).

#### Clone the Raspberry Pi OS to the Internal SSD

Once you're logged in to your Raspberry Pi:

1.  Pull down the `rpi-clone` repository.

        git clone https://github.com/billw2/rpi-clone.git

1.  Install `rpi-clone`.

        sudo cp rpi-clone rpi-clone-setup /usr/local/sbin

1.  Clone Raspberry Pi OS to the internal disk.

        sudo rpi-clone sda

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

1.  Once cloning is done, run `sudo shutdown -h now` and remove the USB stick from the Argon One case.

1.  Power up Argon One, Raspberry Pi OS should now boot from the internal disk.

### Network Configuration

In order to setup a Dogecoin node you may have to forward certain ports in your router.

Follow the steps outlined in the guide _[Running a Full Node](/full-node#enabling-connections)_ to get setup.

### Argon One Configuration

Run the following command to install the Argon One configurations needed to run the fan inside the case:

    curl https://download.argon40.com/argon1.sh | bash

### UFW Configuration

To configure a basic firewall:

1.  Install `ufw`.

        sudo apt install ufw

    **Note**: `ufw` default rules allow for all outgoing connections, but block all incoming connections.[^bitcoin_full_node_on_rbp3]

    [^bitcoin_full_node_on_rbp3]: [https://medium.com/@meeDamian/bitcoin-full-node-on-rbp3-revised-88bb7c8ef1d1](https://medium.com/@meeDamian/bitcoin-full-node-on-rbp3-revised-88bb7c8ef1d1)

1.  Limit SSH access.

        sudo ufw limit ssh

1.  Allow SSH access from the internal network.

        sudo ufw allow from 192.168.1.0/24 to any port 22

1.  Allow Dogecoin traffic:

        # for mainnet …
        sudo ufw allow 22556 comment "Dogecoin mainnet"

        # … or, for testnet
        sudo ufw allow 44556 comment "Dogecoin testnet"

1.  Apply the settings.

        sudo ufw enable

## Dogecoin Node Installation

Finally, we can install the software that will run our Dogecoin node.

1.  Go to the [Dogecoin Releases](https://github.com/dogecoin/dogecoin/releases) page and download the latest ARM Linux release.

    ![PuTTYgen](images/full-node-raspberry-pi/dogecoin-releases.png)

        wget https://github.com/dogecoin/dogecoin/releases/download/v1.14.5/dogecoin-1.14.5-arm-linux-gnueabihf.tar.gz

1.  Unpack the file contents.

        tar xzf dogecoin-1.14.5-arm-linux-gnueabihf.tar.gz

1.  Install the Dogecoin node.

        sudo install -m 0755 -o root -g root -t /usr/local/bin dogecoin-1.14.5/bin/*

1.  Start up the Dogecoin node.

        dogecoind -daemon

1.  Download an example Dogecoin configuration file.

        cd ~/.dogecoin; wget https://github.com/dogecoin/dogecoin/blob/master/contrib/debian/examples/dogecoin.conf

1.  Add the following configurations to the `dogecoin.conf` file:

        maxconnections=32
        server=1
        rpcuser=DogecoinIsAwesome
        rpcpassword=A_SAFE_PASSWORD

You're done! The Dogecoin node will take around two days to fully sync the entire blockchain.
