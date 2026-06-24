# IT Risk Assessment

| ID | Threat Type | Layer | Attacks | Likelihood | Impact | Risk Level |
|:---:|---|---|---|:---:|:---:|:---:|
| T.01 | Compromised Credentials | Identity | Theft and misuse of credentials (username and password)<br>via **Email Phishing**. | 3 | 1 | 🟢 3 Low |
| T.02 | Insider Threats | Identity | Information leakage or cyber threats originating from<br>**internal company sources (employees)**. | 2 | 2 | 🟩 6 Low to Moderate |
| T.03 | Supply Chain Attacks | Application | Infiltration into company communication systems via **third parties (middle-man)**<br>using email manipulation techniques (email phishing / domain spoofing).<br>Attackers impersonate official vendors to deceive the supply chain<br>into transferring funds to the attacker's account. | 1 | 2 | 🟢 5 Low |
| T.04 | API & Integration Vulnerabilities | Application | Exploitation of integration points between systems (API Endpoints)<br>due to weak authentication mechanisms and security vulnerabilities,<br>allowing unauthorized parties to access internal data. | 3 | 2 | 🟩 8 Low to Moderate |
| T.05 | Lateral Movement | Network | Malicious programs (BOT or Crypto Mining) infiltrate a user's device<br>and then spread across systems/computers within the<br>same network segment (VLAN). | 4 | 1 | 🟢 4 Low |
| T.06 | IoT/OT Vulnerabilities | Network | Attacks exploiting security vulnerabilities in internet-connected hardware<br>(Smart Sensors, CNC assembly machines, or production control systems). | 1 | 1 | 🟢 1 Low |
| T.07 | Replay Attacks | Network | Historically an unprecedented incident issue (attacks on Fingerprint,<br>Access Cards, Voice Recordings, and Face Recognition<br>have never occurred). | 3 | 2 | 🟩 8 Low to Moderate |
| T.08 | Advanced Persistent Threats (APT) | Infrastructure | Implanting extremely small files (such as keygens / .c files<br>the size of a notepad script) that attempt to extract data slowly. | 4 | 1 | 🟢 4 Low |
| T.09 | Ransomware & Malware Injection | Infrastructure | Locking data access or encrypting critical systems by **Petya-type Ransomware**<br>targeting user computers outside the company's secure network,<br>followed by a ransom demand. | 3 | 3 | 🟡 13 Moderate |
| T.10 | Industrial Espionage | Data | Illegal attempts to steal trade secrets, technical specifications,<br>blueprints (CAD), and aerospace product formulas<br>for the benefit of competitors. | 1 | 4 | 🟡 15 Moderate |
| T.11 | Disaster | Infrastructure | Large-scale and massive disasters such as Natural Disasters,<br>Human Errors, War, and technical disruptions<br>like regional power outages. | 1 | 4 | 🟡 15 Moderate |
