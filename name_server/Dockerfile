# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY . /code

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
#COPY src/ .
EXPOSE 5000
# command to run on container start
CMD [ "python3", "main.py" ]
