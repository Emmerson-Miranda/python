# Source
https://medium.com/@udiyosovzon/things-you-should-know-when-developing-python-package-5fefc1ea3606

https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

https://jfrog.com/help/r/jfrog-artifactory-documentation/pypi-repositories

https://realpython.com/pypi-publish-python-package/


# setup.py

The setup.py script builds your code into a distribution. It looks for packages inside the root folder, 
so it must be in the root folder. 

Notice that inside the root folder there is a folder with the exact same name as the root folder, my_package. 
In this way you make sure setup.py will find a package with the name my_package.

## setup.cfg
ini file that contains option defaults for setup.py commands.   

## README.rst / README.md¶
All projects should contain a readme file that covers the goal of the project.

## MANIFEST.in¶
A MANIFEST.in is needed when you need to package additional files that are not automatically included 
in a source distribution.

## LICENSE.txt¶
Every package should include a license file detailing the terms of distribution.

# Development mode
You can install a project in “editable” or “develop” mode while you’re working on it.
To install in development mode open terminal and type "python3 -m pip install -e  <path\to\package>". 
If in terminal you are in the package’s directory you can type: "python3 -m pip install -e ."

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

# Packaging your project
Verify before create distribution
```
python3 -m pip install twine
twine check dist/*
```

Create a distribution
```
python3 -m pip install build
```

## Upload your distributions¶
```
twine upload dist/*
```