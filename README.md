# CO-WIN API - SETU

## Setup
1. Install the requirements using pip
```
pip install -r requirements.txt
```
2. Create a new file "variables.py" and create variables as mentioned below:
```
mobile = "ENTER PHONE NUMBER HERE"
beneficiary_id = "ENTER BENEFICIARY ID"
filename = "certificate_{}".format(beneficiary_id)
```
3. Run "script.py"
```
python script.py
```

## About
There are a total of four functions in thr script
1. requestOTP(mobile) - returns a txnId
2. confirmOTP(txnId, OTP) - At this point, the shell asks you to enter the OTP received; returns the bearer token.
3. SHA_hash(OTP) - hashes the OTP with SHA256 algorithm.
4. generateCertificate(token) - Generates the certificate in .pdf format in the same folder.