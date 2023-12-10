FROM python:3.9.13

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 
ENV PORT 2000

# Run the application:
CMD ["gunicorn", "app:app", "--config=config.py"]
