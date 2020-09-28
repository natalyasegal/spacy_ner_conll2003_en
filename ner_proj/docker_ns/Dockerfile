# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# install dependencies
COPY requirements.txt /app/. 
RUN pip install -r requirements.txt

# install spacy's english words
RUN python -m spacy download en 

# expose port
EXPOSE 5000

# Deploy our model
COPY en_model-0.0.0.tar.gz /app/.
RUN tar -xzf /app/en_model-0.0.0.tar.gz

# Copy the current directory contents into the container at /app
COPY src/* /app/

# Run your application!
CMD ["python","app.py"]