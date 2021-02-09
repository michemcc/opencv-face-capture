# opencv-face-capture
Face capture web application using Python and OpenCV, implemented in Django

## To run locally
1. You will need python3 installed on the local system
2. Create a virtual environment using `python3 -m venv /path/to/env`  
  2a. Activate the virtual environment using `source /path/to/env/bin/activate`
3. Clone the repository from github using `git clone <repository_url>`
4. Move into the main project folder (`cd opencv-face-capture`) and install requirements using `pip install -r requirements.txt`
5. Run the commands given below to get the server running:  
  `python manage.py makemigrations`  
  `python manage.py migrate`  
  `python manage.py runserver`

## Notes
The face capture app uses Haar Cascade object detection for the biometric identification. The files are not my own and are sourced from [the opencv data repo](https://github.com/opencv/opencv/tree/master/data/haarcascades). For more information on Haar Cascades, sentdex has a good video [here](https://github.com/opencv/opencv/tree/master/data/haarcascades). Thank you for reading.
