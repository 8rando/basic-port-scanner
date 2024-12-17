
# **Basic Port Scanner**  

## **What is this?**  
This is a simple Python script that scans a target IP address to check for **open ports** in a given range. It’s great for learning about **networking** and how ports work. Perfect for anyone starting out in **cybersecurity** or looking to build small projects for their resume.  

---

## **What Does It Do?**  
- Takes an IP address and a range of ports (like 20–80).  
- Checks each port to see if it’s open or closed.  
- Outputs which ports are open.  

---

## **What You Need**  
- **Python 3.11.9 (installed on your computer).  
- Basic knowledge of running Python scripts in the terminal.  

---

## **How to Set It Up**  

1. **Clone the Project**  
   First, download the project from GitHub:  
   ```bash
   git clone https://github.com/<your-username>/basic-port-scanner.git
   cd basic-port-scanner
   ```

2. **Run the Script**  
   Just run the script in your terminal:  
   ```bash
   python port_scanner.py
   ```

3. **Input the Details**  
   When prompted, enter:  
   - The target IP address (e.g., `127.0.0.1` for localhost).  
   - The range of ports to scan (start port and end port).  

---

## **Example Run**  

**Input**:  
```
Enter the target IP address: 127.0.0.1  
Enter start port: 20  
Enter end port: 80  
```

**Output**:  
```
Scanning ports for: 127.0.0.1  
Port 22 is OPEN  
Port 80 is OPEN  
Scan complete.
```

---

## **How It Works (In Simple Terms)**  
1. The script loops through each port in the range you give it.  
2. It tries to "connect" to each port using Python’s `socket` library.  
3. If the connection is successful, the port is marked **OPEN**. If not, it skips to the next one.  




## **Why This Project?**  
- It’s simple but useful.  

---

## **Tools Used**  
- **Python**  
- **Socket Library** (built into Python)  

---

