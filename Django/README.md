# ToDo List  

Todo List is a Fullstack Web App that features a list of errands and other tasks that one needs to accomplish.

## Tech

ToDo List is written in Python3 and Django3.  
  
## Installation  
  
### Windows 10 Users

Please install and set up the following packages first. Ugrade if you find the package already installed:  
*Download [Python3](https://www.python.org/downloads/). It is advisable to install the package as an administrator. Click on the 'Add path' checkbox before moving on to the next step of the installation process. Run this command in your terminal to see the version you have installed.

  ```sh
  python -V
  ```  

* Download [pip](https://pip.pypa.io/en/latest/installing) and follow the instructions in the link as an installation guide.  
* [SQLite3](https://sqlitebrowser.org/) (Ensure it is installed).
* It is advisable to install Django in a virtual environment. The README uses [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation) to create this virtual environment. You could use any virtualenv package of your choice but for Windows, install this wrapper with:

  ```sh
  py -m pip install virtualenvwrapper-win 
  ```
  
* Create a new virtual environment:

  ```sh
  mkvirtualenv <envname>
  ```

* Change your directory to the directory of the virtual environment

* Activate the virtual environment with:

  ```sh
  <envname>\Scripts\activate
  ```

* Install requirements in the virtual environment created:

  ```sh
  pip install django 
  ```

  ```sh
  pip install -r requirements.txt
  ```

* Run server to ensure everything is running properly.

  ```sh
  python manage.py runserver
  ```

* Deactivate the virtual environment with:

  ```sh
  deactivate
  ```
