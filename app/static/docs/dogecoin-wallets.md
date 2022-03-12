# Dogecoin Wallets

As Dogecoin is a digital asset, it can be very un-intuitive to store safely. Historically many people have lost their coins but with proper understanding the risks can be eliminated. **If your Dogecoins do end up lost or stolen then there's almost certainly nothing that can be done to get them back.**

[TOC]

## What Is A Dogecoin Wallet?

A Dogecoin wallet can either be a software, service or gadget that saves your private and public keys and communicates with the blockchain. Your wallet's public key, that also serves as your "wallet address", can be viewed as the account number of your Dogecoin bank account. The private key of your wallet can be seen as the password for your Dogecoin bank account, which you can use to send Dogecoin from your wallet to another.<sup>[\[1\]](#references)</sup>

## What Is The Best Dogecoin Wallet?

The best way to store Dogecoin is to either use a hardware wallet, a multi-signature wallet or a cold storage wallet. Have your wallet create a seed phrase, write it down on paper and store it in a safe place (or several safe places, as backups). Ideally the wallet should be backed by your own [full node](/full-node).

The art and science of storing Dogecoins is about keeping your private keys safe, yet remaining easily available to you when you want to make a transaction. It also requires verifying that you received real Dogecoins, and stopping an adversary from spying on you.

### Protection From Accidental Loss

In the past many people have accidentally lost Dogecoins because of failed backups, mistyped letters, forgotten hard drives, corrupted SSD devices, or numerous other slip ups.

The key to protecting yourself from data loss of any kind is to have redundant backups so that if one is lost or destroyed, you still have others you can use when you need them. All good wallet software asks their users to write down the seed recovery phrase of the wallet as a backup, so that if your primary wallet is lost or damaged, you can use the seed recovery phrase to restore access to your coins. If you have more than one backup location, they should be in places where various disasters won't affect both of your backups. For example, its much better to store two backups in a home safe and in a safe deposit box (as long as your seed is protected by a passphrase) than to store two backups in your bedroom and one in your garage.

Also important is regularly verifying that your backup still exists and is in good condition. This can be as simple as ensuring your backups are still where you put them a couple times a year.

The best practices for backing up a seed is to store the seed using pencil and paper or metal seed phrase backup and storing in multiple secure locations.

### Verification And Privacy

Storing a seed phrase only stores private keys, but it cannot tell you if or how many Dogecoins you have actually received. For that you need wallet software.

If you received cash banknotes or gold coins as payment, you wouldn't accept them without inspecting them and verifying that they are genuine. The same is true with Dogecoin. Wallet software can automatically verify that a payment has been made and when that payment has been completed (by being mined into a number of blocks). The most secure kind of wallet is one which independently verifies all the rules of Dogecoin, known as a full node. When receiving large volumes, it is essential to use wallet software that connects to a full node you run yourself. If Dogecoin is digital gold, then a full node is your own personal digital goldsmith who checks that received Dogecoin payments are actually real. Lightweight wallets have a number of security downsides because they don't check all of Dogecoin's rules, and so should only be used for receiving smaller amounts or when you trust the sender. See the article about [full nodes](/full-node).

Your wallet software will also need to learn the history and balance of its wallet. For a lightweight wallet this usually involves querying a third-party server which leads to a privacy problem as that server can spy on you by seeing your entire balance, all your transactions and usually linking it with your IP address. Using a full node avoids this problem because the software connects directly to the Dogecoin P2P network and downloads the entire blockchain, so any adversary will find it much harder to obtain information.

So for verification and privacy, a good storage solution should be backed by a full node under your own control for use when receiving payments. The full node wallet on an online computer can be a watch-only wallet. This means that it can detect transaction involving addresses belonging to the user and can display transaction information about them, but still does not have the ability to actually spend the Dogecoins.

### Protection From Theft

Possession of Dogecoins comes from your ability to keep the private keys under your exclusive control. In Dogecoin, keys are money. Any malware or hackers who learn what your private keys are can create a valid Dogecoin transaction sending your coins to themselves, stealing your Dogecoins. The average person's computer is usually vulnerable to malware, so that must be taken into account when deciding on storage solutions.

Anybody else who discovers a wallet's seed phrase can steal all the Dogecoins if the seed isn't also protected by a secret passphrase. Even when using a passphrase, a seed should be kept safe and secret like jewels or cash. For example, no part of a seed should ever be typed into any website, and no one should store a seed on an internet-connected computer unless they are an advanced user who has researched what they're doing.

Seed phrases can store any amount of Dogecoins. It doesn't seem secure to possibly have enough money to purchase the entire building just sitting on a sheet of paper without any protection. For this reason many wallets make it possible to encrypt a seed phrase with a passphrase.

### Easy Access

Some users may not need to actually move their Dogecoins very often, especially if they own Dogecoin as an investment. Other users will want to be able to quickly and easily move their coins. A solution for storing Dogecoins should take into account how convenient it is to spend from depending on the user's needs.

### Summary

In Dogecoin: Dogecoin wallets should be backed up by writing down their seed phrase, this phrase must be kept safe and secret, and when sending or receiving transactions the wallet software should obtain information about the Dogecoin network from your own full node.

## What Kind Of Dogecoin Wallets Are There?

There are many different types of Dogecoin wallets available. The possibilities range from digital wallets that can be accessed via your phone and computer to real physical hardware wallets. The different kind of wallets and their properties are described below.

### Hardware Wallets

Hardware wallets are special purpose security-hardened devices for storing Dogecoins on a peripheral that is trusted to generate wallet keys and sign transactions.

A hardware wallet holds the seed in its internal storage and is typically designed to be resistant to both physical and digital attacks. The device signs the transactions internally and only transmits the signed transactions to the computer, never communicating any secret data to the devices it connects to. The separation of the private keys from the vulnerable environment allows the user to spend Dogecoins without running any risk even when using an untrustworthy computer. Hardware wallets are relatively user-friendly and are one of the best ways to store Dogecoins.

Some downsides are that hardware wallets are recognizable physical objects which could be discovered and which give away that you probably own Dogecoins. This is worth considering when for example crossing borders. They also cost more than software wallets. Still, physical access to a hardware wallet does not mean that the keys are easily compromised, even though it does make it easier to compromise the hardware wallet. The groups that have created the most popular hardware wallets have gone to great lengths to harden the devices to physical threats and, though not impossible, only technically skilled people with specialized equipment have been able to get access to the private keys without the owner's consent. However, physically-powerful people such as armed border guards upon seeing the hardware wallet could force you to type in the PIN number to unlock the device and steal the Dogecoins.

### Multi-Signature Wallets

A multi-signature wallet is one where multiple private keys are required to move the Dogecoins instead of a single key. Such a wallet can be used for requiring agreement among multiple people to spend, can eliminate a single point of failure, and can be used as form of backup, among other applications.

These private keys can be spread across multiple machines in various locations with the rationale that malware and hackers are unlikely to infect all of them. The multisig wallet can be of the m-of-n type where any m private keys out of a possible n are required to move the money. For example a 2-of-3 multisig wallet might have your private keys spread across a desktop, laptop, and smartphone, any two of which are required to move the money, but the compromise or total loss of any one key does not result in loss of money, even if that key has no backups.

Multi-signature wallets have the advantage of being cheaper than hardware wallets since they are implemented in software and can be downloaded for free, and can be nearly as convenient since all keys are online and the wallet user interfaces are typically easy to use.

Hardware and multi-signature wallets can be combined by having a multi-signature wallet with the private keys held on hardware wallets; after all a single hardware wallet is still a single point of failure. Cold storage and multi-signature can also be combined, by having the multi-signature wallet with the private keys held in cold storage to avoid them being kept online.

### Cold Storage Wallets

A cold wallet generates and stores private wallet keys offline on a clean, newly-installed air-gapped computer. Payments are received online with a watch-only wallet. Unsigned transactions are generated online, transferred offline for signing, and the signed transaction is transferred online to be broadcast to the Dogecoin network.

This allows funds to be managed offline in Cold storage. Used correctly a cold wallet is protected against online threats, such as viruses and hackers. Cold wallets are similar to hardware wallets, except that a general purpose computing device is used instead of a special purpose peripheral. The downside is that the transferring of transactions to and fro can be fiddly and unweilding, and less practical for carrying around like a hardware wallet.

### Hot Wallets

A hot wallet refers to keeping single-signature wallets with private keys kept on an online computer or mobile phone. Most Dogecoin wallet software out there is a hot wallet. The Dogecoins are easy to spend but are maximally vulnerable to malware or hackers. Hot wallets may be appropriate for small amounts and day-to-day spending.

A user might have a spending account hot wallet for day-to-day convenient spending with the majority of their funds on a savings account which is stored with much more security (cold storage / hardware wallet / multi-signature).

### Bad Wallet Ideas

#### Custodial Wallets

Custodial wallets are where an exchange, broker or other third party holds your Dogecoins in trust.

The number one rule to storing Dogecoin is this: if you don’t hold the private keys, you don’t actually own the assets. There are many historical examples of loss due to custodial wallets: Silk Road, Bitfloor, MTGOX, Sheep Marketplace, BTC-e, Bitstamp, Bitfinex, Bithumb, Cryptsy, Bter, Mintpal and many more.

**"Isn't it just like keeping your money in a bank?"**

There are trade offs with everything, but trusting Coinbase with your Dogecoin is not the same as trusting a bank with your dollars:

Suppose 5 people are needed to access the funds, within Coinbase, e.g. the CEO, the tech lead engineer and 3 other senior employees. Suppose one day they wake up and decide to be evil and move all the Dogecoin to some private account of theirs, and perhaps make up a story in the press about how they've been "hacked". You have a serious problem, as you might find there is a protracted legal battle (see MtGox), but you can't actually retrieve the funds unless in some way the company is re-stocked with Dogecoin, or perhaps an equivalent in fiat.

If on the other hand you controlled the funds with a majority of keys in a multisig i.e. you own both of the two needed keys of a 2-of-3 multisig, then it would always effectively be your Dogecoin, even though the third key may belong to a trusted third party custodian. But this also comes with the responsibility that if you get hacked, you lose all your funds. That is why it's prudent, in a 2-of-3 multisig where you have the two needed keys, to have them in separate systems/locations. If one of them fails, you can go to the custodian to supply the third key and transfer your funds again to safety. But the custodian alone, cannot touch your funds just by virtue of having the third key.

Now, if your bank gets hacked similarly - 5 key operatives in the bank decide to swipe your money and pretend it was external hackers - SWIFT transfers are made to accounts in China. Here it will always ultimately be at the discretion of legal agencies whether you "actually" still have the money that is stolen. Because dollars are not real, they can be created at a whim, and while reversing international transfers is not quite so simple, very often that reversal can be achieved (e.g. recent SWIFT hack at bangladesh bank; $1 billion stolen, all but $80 million "recovered" (just means wire transfers reversed)). Added to that consider that fiat money is insured, so even when transfers can't be reversed, the money can be "recovered". If too many banks get hacked all at once the Federal Reserve and the government together can make up some "fund" that magically reassigns balances any time they like, with sufficient political will (that's essentially what was happening in 2008 TARP etc).

So far no insurance company has ever paid out on a Dogecoin company's claim. Worth considering also.

You might say, since it's risky both ways, why not trust Coinbase? Aren't they more competent in security than me?

Almost certainly, but this argument has two massive holes in it: (1) because they concentrate funds they are a massive target for hackers, while you are not - at all. (2) they are a trusted third party so the situation is strictly worse - not only do you have to trust their security skills, but you also have to trust them not to steal (modulo multisig, as mentioned above) (3) as well as literal stealing, there is things like political confiscation.

#### Web Wallets

Web wallets have all the downsides of custodial wallets (no direct possession, private keys are held by a third party) along with all the downsides of hot wallets (exposed private keys), as well as all the downsides of lightweight wallets (not verifying Dogecoin's rules, someone could send you a billion Dogecoins and under certain conditions the dumb web wallet would happily accept it).

Someone who needs the easy access of a web wallet should download a lightweight wallet.

#### Paper Wallets

So-called paper wallets are an obsolete and unsafe method of storing Dogecoin which should not be recommended to beginners. They simply store a single private/public keypair on paper. They promote address reuse and require unwieldy and complicated live OS system boots to be safe, they risk theft by printers, and typically rely on Javascript cryptography.

Paper wallets also do not provide any method of displaying to the user when money has arrived. There's no practical way to use a full node wallet. Users are typically driven to use third-party blockchain explorers which can lie to them and spy on them.

A much better way to accomplish what paper wallets do is to use seed phrases instead.

#### Cloud Storage

This means storing your encrypted (or not) wallet file on a cloud storage solution such as Dropbox, or emailing them to yourself on Gmail. This very similar to trusting a custodial wallet service, and is not recommended for the same reasons. You might say you use encryption for two-factor authentication, but uploading the wallet to the cloud reduces this to one-factor. Furthermore, there are a variety of ways in which 2FA can be compromised, in particular SMS-based 2FA, such as via a SIM-Swap.

#### "Physical" Dogecoins

Physical Coins and other mechanism with a pre-manufactured key or seed are not a good way to store Dogecoins because they keys are already potentially compromised by whoever created the key. You should not consider Dogecoin yours if its stored on a key created by someone else. It only becomes yours when you transfer the Dogecoin to a key that you own and exclusively control.

## Which Dogecoin Wallets Do We Recommend?

- Full node wallet: [Dogecoin Core](https://dogecoin.com/) is a full Dogecoin client and builds the backbone of the network. It offers high levels of security, privacy, and stability. However, it has fewer features and it takes a lot of space and memory.
- Hardware wallets: [Ledger](https://shop.ledger.com/products/ledger-nano-s), [Trezor](https://shop.trezor.io/)
- Light wallet: [MultiDoge](https://dogecoin.com/) syncs with the blockchain by "skimming" through the blockchain, providing fast sync times.

---

# References

1. [https://anycoindirect.eu/en/wallets/litecoin](https://anycoindirect.eu/en/wallets/litecoin)

This work, "Dogecoin Wallets", is a derivative of "[Storing bitcoins](https://en.bitcoin.it/wiki/Storing_bitcoins)", used under [CC BY](https://creativecommons.org/licenses/by/3.0/). "Dogecoin Wallets" is licensed under [CC BY](https://creativecommons.org/licenses/by/4.0/) by DogecoinIsAwesome.com
