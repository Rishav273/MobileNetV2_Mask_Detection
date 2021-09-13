# Server side architecture for a Face Mask Detection system using the Mobilenet V2 network.

### Further plans:

* Train the network on more data, train multiple networks.
* Create a frontend with the objective of extending it into a fully functional webapp that detects masks in real time. 

## Usage:

* Clone the repo in your local directory.

```  
git clone <repo link>
```

* open shell instance, navigate to the directory you saved the file. Create new virtual environment and install test_requirements.txt file

```  
py -m virtualenv -p=<your preferred python executable (eg: 3.8.3)> <env name>
pip install -r test_requirements.txt 
```

* Note: If you're unsure where your python execs are located, run the following command in the shell

```
where python
```

This will show the paths to all your execs. Copy your favoured path and paste it in <your preferred python executable> part above.

* Run detect_mask.py

```
python detect_mask.py
```
