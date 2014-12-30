
### What is running in EC2?

Lists all running rails instance and if they have a public IP gets their git hash.   
Also lists all running known envs by domain name and their git hash.   

### Requirements
- python 2.7
- pip
- virtualenv
- aws key and secret in your ~/.aws/credentials file

### Quick Installation

```
$git clone this repo  
$cd running
$virtualenv env  
$. env/bin/activate  
$pip install -r requirements.txt
$python whatsrunning.py
```

### Usage  
```
$ python whatsrunning.py
+-----------------------------------+----------------+------------+---------+------------------------------------------+
|                name               |       ip       |     id     |  state  |                  answer                  |
+-----------------------------------+----------------+------------+---------+------------------------------------------+
| carlingo-staging - virginia-beach | 54.88.220.211  | i-7d941b83 | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|    carlingo-production - porto    |      None      | i-41a637bf | stopped |                   N/A                    |
|    carlingo-production - sofia    | 54.172.29.112  | i-6ea73690 | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|      carlingo-staging - boise     |  54.174.83.39  | i-9f57b072 | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|     carlingo-development - nix    | 54.165.182.243 | i-15ca48eb | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
+-----------------------------------+----------------+------------+---------+------------------------------------------+
+----------------------------------+------------------------------------------+
|               url                |                   hash                   |
+----------------------------------+------------------------------------------+
| http://development.carlingo.com/ | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|   http://staging.carlingo.com/   | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
| http://production.carlingo.com/  | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
+----------------------------------+------------------------------------------+
```
