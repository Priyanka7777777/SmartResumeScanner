pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "priyanka7777777"
        IMAGE_NAME = "smartresumescanner"
        IMAGE_TAG = "latest"
        CONTAINER_NAME = "smartresumescanner-app"
        HOST_PORT = "5001"
        CONTAINER_PORT = "5000"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Priyanka7777777/SmartResumeScanner.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh '''
                  docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

       stage('Deploy Application (CD)') {
    steps {
        sh '''
          echo "Stopping any container using port 5001..."
          docker ps -q --filter "publish=5001" | xargs -r docker stop
          docker ps -aq --filter "publish=5001" | xargs -r docker rm

          echo "Starting new container..."
          docker run -d \
            --name smartresumescanner-app \
            -p 5001:5000 \
            priyanka7777777/smartresumescanner:latest
        '''
    }

       }
    }
    post {
        success {
            echo "✅ Application deployed successfully on port ${HOST_PORT}"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
