# 🧮 Subnet Calculator

A simple and beginner-friendly **Python Subnet Calculator** that calculates important IPv4 subnet information from an IP address with CIDR notation.

## ✨ Features

* Calculate **Network Address**
* Calculate **Broadcast Address**
* Calculate **Subnet Mask**
* Calculate **Wildcard Mask**
* Display **CIDR Notation**
* Calculate **Total IP Addresses**
* Calculate **Usable Host Addresses**
* Display **First Usable Host**
* Display **Last Usable Host**
* Input validation for invalid IP/CIDR
* Colored terminal output
* Simple subnet calculation animation

## 🛠️ Technologies Used

* **Python 3**
* Python `ipaddress` module
* Python `sys` module
* Python `time` module

## 📂 Project Structure

```text
Subnet-Calculator/
│
├── subnet_calculator.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Enter the Project Directory

```bash
cd Subnet-Calculator
```

### 3. Run the Program

```bash
python3 subnet_calculator.py
```

## 💻 Usage

When the program starts, enter an IPv4 address with CIDR notation.

Example:

```text
Enter IP address with CIDR (e.g. 192.168.1.10/24):
192.168.1.10/24
```

The program will calculate and display:

```text
Network Address   : 192.168.1.0
Broadcast Address : 192.168.1.255
Subnet Mask       : 255.255.255.0
Wildcard Mask     : 0.0.0.255
CIDR Notation     : /24
Total Addresses   : 256
Usable Hosts      : 254
First Usable Host : 192.168.1.1
Last Usable Host  : 192.168.1.254
```

## ❌ Invalid Input

The program validates the entered IP/CIDR format.

Example:

```text
192.168.1.999/24
```

will produce an invalid IP/CIDR error message.

## 📚 What I Learned

This project helped me practice:

* IPv4 addressing
* CIDR notation
* Subnetting concepts
* Network and broadcast addresses
* Host address calculation
* Python's `ipaddress` module
* Python exception handling
* Command-line interfaces
* Basic terminal formatting and ANSI colors

## 🎯 Purpose

This project was created as a **networking practice project** to strengthen my understanding of IP addressing and subnetting while developing practical Python skills.

## 👨‍💻 Developer

**4RCH-M3G**

---

⭐ If you find this project useful, consider giving the repository a star!
