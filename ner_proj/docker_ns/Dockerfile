# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# install the only library we really need for this, version should match one used for training
RUN pip install spacy==v2.2

# install spacy's english words
RUN python -m spacy download en 

# Deploy or model
RUN tar -xzf /app/en_model-0.0.0.tar.gz

# Run your application!
CMD ["python","app.py"]