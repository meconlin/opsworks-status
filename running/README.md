
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
| mysite-staging - virginia-beach | 54.88.222.221  | i-7d941b86 | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|    mysite-production - porto    |      None      | i-41a637b7 | stopped |                   N/A                    |
|    mysite-production - sofia    | 54.173.30.112  | i-6ea7369y | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|      mysite-staging - boise     |  54.175.83.39  | i-9f57b07g | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|     mysite-development - nix    | 54.166.188.243 | i-15ca48eh | running | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
+-----------------------------------+----------------+------------+---------+------------------------------------------+
+----------------------------------+------------------------------------------+
|               url                |                   hash                   |
+----------------------------------+------------------------------------------+
| http://development.mysite.com/ | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
|   http://staging.mysite.com/   | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
| http://production.mysite.com/  | 41f9cdc77ae640ba0ad46f601f94b3926455c925 |
+----------------------------------+------------------------------------------+
```
