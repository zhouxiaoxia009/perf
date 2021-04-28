Function:
When there exist a number of checks to add, and they have identical parts, datacheck-ini.py will creat or overwrite a txt file named as "ini.txt".

What is needed: 
(1) checkadd.txt: Variables list in columns. Naming rule is $var1, $var2,...$var[n]
(2) config.txt: This is a pattern which needs you to write it manually.

How to run:
Step 1: write a pattern in the config.txt
Step 2: fill the checkadd.txt
Step 3: If the checkadd, config and datacheck-ini.py are in the same folder, just double click the datacheck-ini.py, then you will get the ini file. If the datacheck-ini.py is in different path from the checkadd, config file, use "-o" to specify the folder where checkadd and config file are in. The output ini.txt file can be found in the same path.

Here is an example config.txt and an example checkadd.txt.
