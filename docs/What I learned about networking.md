---
id: What I learned about networking
aliases: []
tags:
  - port scanner
  - network
What I learned about networkingaliases:
  - What I learned about networking
---

# What I Learned About Networking So Far

## TCP / TCP Handshake

**TCP (Transmission Control Protocol)** is a widely used protocol for communication between devices. It is well known for its **reliability**. This reliability can be attributed to the fact that it checks after any action is done (connecting, sending packets, etc.).

One of the ways that it ensures safety is by the **3-way handshake**.

The 3-way handshake works like this:

- **SYN:** Device **A** sends an ISN (Initial Sequence Number), which is a randomly generated number.
    
- **SYN-ACK:** Device **B** receives the ISN. To show that it has received the ISN, it adds 1 to it and sends it back along with its own ISN, which is also random.
    
- **ACK:** **A** receives **B**'s ISN and its own ISN + 1, and sends back **B**'s ISN + 1.
    
- **DATA:** Finally, **B** receives the packets and they start transferring files or whatever they do.
    

### The TCP Header

The TCP header is **20–60 bytes**. 40 bytes are reserved for options and padding, so a header that is 20 bytes has no options or padding.

|**Field**|**Size**|**Description**|
|---|---|---|
|**Source Port**|16 bits|The port address of the application sending the data segment.|
|**Destination Port**|16 bits|The port address of the application receiving the data segment.|
|**Sequence Number**|32 bits|Used for reassembling messages received out of order.|
|**Acknowledgment Number**|32 bits|Holds the acknowledgment (ACK) of previous bytes received successfully (ISN + 1).|
|**Header Length**|4 bits|Indicates the length of the header.|
|**Window Size**|16 bits|The size of the window for sending TCP bytes (flow control).|
|**Checksum**|16 bits|Used for error control; mandatory in TCP.|
|**Urgent Pointer**|16 bits|Points to data that needs to reach the receiving process urgently.|

**Control Flags (6 bits total):**

- **URG:** Urgent pointer is valid.
    
- **ACK:** Acknowledgment number is valid.
    
- **PSH:** Request to push data.
    
- **RST:** Connection reset.
    
- **SYN:** Synchronize sequence numbers.
    
- **FIN:** Connection termination.
    

---

## What is UDP?

From what I understand, **UDP (User Datagram Protocol)** is TCP without the checks like the 3-way handshake. It prioritizes speed over reliability.

---

## What is a Socket?

A **socket** is an endpoint for two devices to communicate through.

---

## What is a Port?

A **port** is a number which the OS uses to identify a specific process or service. This way, other devices can make requests or send packets through those ports.

- A port is an **unsigned 16-bit integer** (ranging from 0 to 65535).
    
- When sending a packet, the destination address is the **IP** of the destination device combined with the **port number**.
    

> **Note:** It is important to understand that a socket is not a port. A socket is just for two-way communicating. There can be multiple sockets on a single port.

So the gist is that when a socket opens at, say, **Port 53**, the process connected to that socket says to the OS: _"Any packets that arrive at this port, direct them to me."_
