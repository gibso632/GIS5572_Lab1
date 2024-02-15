# Enable Dockerfile to read Python
FROM python:3.10-slim

# Set work directory to the created flask application
WORKDIR /ArcII_flask_app

# Copy the directory contents into /ArcII_slask_app container
COPY . /ArcII_flask_app

# Install needed packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to public
EXPOSE 80

# Create variable for environment
ENV NAME World

# Run the flask application when container opens
CMD ["python","ArcII_flask_app.py"]

