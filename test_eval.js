const data = [
      {
        id: "T.10",
        title: "Industrial Espionage",
        mode: 4,
        modeLabel: "Highly Relevant",
        expertNotes: "Cisometric Consulting Manager: <br> add 8.1 User endpoint devices (prevent access to or theft of information from employee laptops or lab workstations)",
        fgd: "According to the Consulting Manager at Cisometric, Control 8.1 User Endpoint Devices, can be added with the statement: �?oCan prevent unauthorized access, disclosure, or theft of information.�?? The forum agreed to add this control because industrial espionage often occurs via employees�?T laptops or lab workstations.",
        preControls: ["8.12 DLP", "8.3 Access restriction", "5.12 Classification", "8.15 Logging"],
        postControls: [{ name: "8.1 User Endpoint Devices", status: "added" }]
      },
      {
        id: "T.11",
        title: "Disaster",
        mode: 4,
        modeLabel: "Highly Relevant",
        expertNotes: "No additional notes from experts",
        fgd: "No changes",
        preControls: ["8.14 Redundancy", "5.30 ICT readiness", "5.29 Information security during disruption"],
        postControls: []
      },
      {
        id: "T.09",
        title: "Ransomware & Malware Injection",
        mode: 4,
        modeLabel: "Highly Relevant",
        expertNotes: "IT Security Supervisor: <br> add 8.15 Logging (logs to support 8.16 Monitoring Activity)",
        fgd: "According to experts, DetereCo�?Ts IT Security Supervisor can add Control 8.15 (Logging) with the statement: �?oCapable of logging all intrusion attempts and supporting Control 8.16 (Activity Monitoring).�?? The forum agreed to add the control because it provides an audit trail for early threat detection and post-incident root cause analysis.",
        preControls: ["8.8 Vulnerability Management", "8.7 Anti-malware", "8.16 Monitoring", "5.26 Response", "8.13 Backup"],
        postControls: [{ name: "8.15 Logging", status: "added" }]
      },
      {
        id: "T.04",
        title: "API & Integration Vulnerabilities",
        mode: 3,
        modeLabel: "Relevant",
        expertNotes: "Cisometric Consulting Manager: <br> add 8.27 Secure Architecture (pen tests show exposed API keys; �?osecure by design�?? is not yet optimal) <br><br> IT Planning & Strategy Manager at DetereCo: <br> add 5.12 Classification (categorize data that may or may not be exposed via API)",
        fgd: "According to the expert, Cisometric�?Ts Consulting Manager, Control 8.27 should be added, stating, �?~The results of penetration testing indicate that the �?osecure by design�?? principle has not been optimally implemented.�?T The forum agreed to add the control because it aligns with Tenet 3, which applies on a per-session basis. <br><br> According to the IT Planning & Strategy Manager at DetereCo, control 5.12 should be added, stating: �?oData must be categorized into those that may and may not be transmitted via the API.�?? The forum agreed to add this control because it ensures the API automatically blocks data classified as �?oConfidential�??.",
        preControls: ["8.5 Authentication", "8.26 Application Security", "8.22 Segregation"],
        postControls: [{ name: "8.27 Secure Architecture", status: "added" }, { name: "5.12 Classification", status: "added" }]
      },
      {
        id: "T.07",
        title: "Replay Attacks",
        mode: 4,
        modeLabel: "Highly Relevant",
        expertNotes: "No additional notes",
        fgd: "No changes",
        preControls: ["8.5 Secure authentication", "8.24 Use of cryptography"],
        postControls: [];