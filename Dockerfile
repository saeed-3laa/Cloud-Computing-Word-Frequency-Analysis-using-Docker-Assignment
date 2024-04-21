# Use the official Python image from Docker Hub
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and text file into the container
COPY asss.py /app/
COPY random_paragraphs.txt /app/


# Install NLTK using pip
RUN pip install nltk

# Download NLTK data for stopwords and punkt tokenizer
RUN python3 -m nltk.downloader stopwords punkt

# Set the default command to run the Python script
CMD ["python3", "asss.py"]
