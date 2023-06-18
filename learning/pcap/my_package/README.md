# Source
https://medium.com/@udiyosovzon/things-you-should-know-when-developing-python-package-5fefc1ea3606

# setup.py

The setup.py script builds your code into a distribution. It looks for packages inside the root folder, 
so it must be in the root folder. 

Notice that inside the root folder there is a folder with the exact same name as the root folder, my_package. 
In this way you make sure setup.py will find a package with the name my_package.

# Development mode

To install in development mode open terminal and type "pip install -e <path\to\package>". 
If in terminal you are in the package’s directory you can type: "pip install -e ."

Output:
```
my_package % pip install -e .
Obtaining file:///Users/owl/GitHub/python/learning/pcap/my_package
  Preparing metadata (setup.py) ... done
Installing collected packages: myPkg
  Running setup.py develop for myPkg
Successfully installed myPkg-1.0.0

[notice] A new release of pip is available: 23.0.1 -> 23.1.2
[notice] To update, run: python3.10 -m pip install --upgrade pip

```
