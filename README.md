# Flask MNIST Digit Classification Web Service

## Overview

This web service is built using Flask and utilizes a neural network model trained on the MNIST dataset for handwritten digit classification. The model is implemented with TensorFlow and Keras libraries. Users can upload JPEG images of handwritten digits, and the service will predict the digit class using the trained neural network.

## Features

- **MNIST Digit Classification:** The web service is designed to classify handwritten digits using a pre-trained neural network model.
- **Web Interface:** Users can upload JPEG images through a user-friendly web interface.
- **MYSQL Connection:** Automatically stores the Predictions and Images uploaded to the web service. 
- **Dockerized:** The application is containerized using Docker for easy deployment and scalability.
- **Kubernetes Deployment:** The Dockerized application is deployed on Kubernetes for efficient management and scaling.

## Prerequisites

Before running the web service, make sure you have the following installed:

- Docker
- Kubernetes

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/keerthikkn/MNIST_Project.git
    cd MNIST_Project
    ```
2.**Go to "src/db.py" and update the MYSQL Connection credentials**

3. **Build Docker Image:**

    ```bash
    docker build -t mnist-digit-classification:latest .
    ```

4. **Run Docker Container:**

    ```bash
    docker run -p 5000:5000 mnist-digit-classification
    ```

5. **Access the Web Interface:**

    Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Kubernetes Deployment

1. **Apply Kubernetes Configuration:**

    ```bash
    kubectl apply -f kubernetes/deployment.yaml
    ```

2. **Access the Web Service:**

    Find the external IP of the service using:

    ```bash
    kubectl get services
    ```

    Open your web browser and navigate to [http://external-ip:5000](http://external-ip:5000).

## Usage

1. **Upload Image:**

    - Navigate to the web interface.
    - Click the "Choose File" button to upload a JPEG image of a handwritten digit.

2. **View Prediction:**
    - Click the upload button.
    - After uploading, the web service will display the predicted digit class.
    - And stores the uploaded image and prediction in the provided MYSQL database


## Contributing

Feel free to contribute by submitting issues, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The model used in this project is based on the TensorFlow and Keras MNIST example.
- Flask, TensorFlow, and Keras communities for their excellent documentation and resources.

## Contact

For any inquiries or support, please contact [keerthikkn2000@gmail.com](mailto:keerthikkn2000@gmail.com).
