# 🚀 Multi-Container Application Development and Deployment

## 📄 Overview

This project demonstrates the development and deployment of a multi-container application using Docker. It involves developing a simple application with two containers: a MySQL database container and a machine learning (ML) model serving API container.

## 🔧 Develop a Simple Application with Two Containers

The task involves creating a custom multi-container application that consists of:

### 🗄️ 1. DB Container (MySQL Database)

- **Database Name**: `Model_Logger`
- **Table**: `Log`
  - **Columns**:
    - `🆔 ID`: Unique identifier for each log entry.
    - `📅 Current_Date_Time`: Timestamp of the log entry.
    - `📥 Input_Params`: Input parameters for the ML model.
    - `📤 Output`: The output generated by the ML model.
    - `⏱️ Response Time`: Time taken to process the input and generate the output.

### 🤖 2. ML Serving API Container

- This container runs a pre-trained ML model as a serving API.
- The API accepts input, processes it with the ML model, generates an output, and then:
  - 📋 Logs the input parameters, output, and response time into the `Log` table in the MySQL database (running in a separate container).
  - 💻 Returns the result to the user.
 
  #### User Interface
    Below is a screenshot of the application's interface:
  
![Screenshot 2024-11-04 184813](https://github.com/user-attachments/assets/b71b84e8-7b6f-464e-bf9c-d2dbd12edc3e)

The interface allows users to input their height and weight, press the **Predict** button, and view the prediction result.

### 🛠️ Docker Compose

- A `docker-compose.yml` file is included to manage both containers.
- With Docker Compose, you can easily start and stop the entire application.

## 📂 Directory Structure

- **app**: Contains the code for the ML model serving API.
- **db-init-scripts**: Contains SQL scripts to initialize the database, create the `Model_Logger` database, and `Log` table.
- **docker-compose.yml**: The Docker Compose file to run and manage both containers.

## 📝 Notes

- Ensure that the ML model API is configured to connect to the MySQL database container for logging purposes.
- Verify that the MySQL container is properly initialized with the required database and table on startup.

## ⚙️ Requirements

- 🐳 Docker
- 📦 Docker Compose

## ▶️ How to Run

1. 📥 Clone the repository.
2. 💾 Ensure Docker and Docker Compose are installed on your machine.
3. 🚀 Run the application:
   ```bash
   docker-compose up

4. 🛑Stop the application:
   ```bash
   docker-compose down

  
