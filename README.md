# Dessertation
An Affordable Open Source SIEM Solution for Small and Medium Sized Organization with Augmented XDR Features 

	Documentation 

	Wazuh is an open source, security monitoring technology that detects threats, monitors integrity, responds to incidents, and ensures compliance.

	This repository contains the online documentation for this project. Members of the Wazuh team and community members contribute to the site's creation and ongoing enhancement.
	Online Wazuh Documentation : https://documentation.wazuh.com/current/ - current version 

	This document contains step-by-step guidance on how to deploy an all-in-one Wazuh and Open Distro for Elasticsearch Components. :
  https://documentation.wazuh.com/current/installation-guide/open-distro/all-in-one-deployment/all-in-one.html 

	Wazuh Agent Installation guide for linux Systems: https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-linux.html

	Wazuh Agent Installation guide for Windows Systems: https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html

	Suricata Installation on Ubuntu 20.04: https://www.digitalocean.com/community/tutorials/how-to-install-suricata-on-ubuntu-20-04 

	OSINT used to create CDB lists – Integration with AlienVault. The following steps must be applied to Wazuh Manager: 

	- sudo weget https://raw.githubusercontent.com/firehol/blocklistipsets/master/alienvault_reputation.ipset
	-	/var/ossec/etc/lists/alienvault_reputation.ipset sudo wget https://wazuh.com/resources/iplist-to-cdblist.py -O /var/ossec/etc/lists/iplist-to-cdblist.py
	-	sudo chmod +x /var/ossec/etc/lists/iplist-to-cdblist.py 
	-	sudo /var/ossec/etc/lists/iplist-to cdblist.py /var/ossec/etc/lists/alienvault_reputation.ipset /var/ossec/etc/lists/blacklist-alienvault 
	-	sudo rm -f /var/ossec/etc/lists/alienvault_reputation.ipset

	Active Response Integration with Wazuh: https://documentation.wazuh.com/current/user-manual/capabilities/active-response/how-it-works.html 

	VirusTotal link for accessing the API for Wazuh integration - https://www.virustotal.com/gui/home/upload 

	Wazuh is responsible for detecting abnormalities produced by an intruder or malware the following link provides the details : 
  https://documentation.wazuh.com/current/user-			manual/capabilities/anomalies-detection/how-it-works.html

	I edited fortigate rules, and the modified code is now in the repository under the name 0390-fortigate rules. 
  Custom-written scripts for running the code are also included in the 		repository.
