pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "priyanka7777777"
        IMAGE_NAME = "smartresumescanner"
        IMAGE_TAG = "latest"
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
    }

    post {
        success {
            echo "✅ Docker image pushed successfully to Docker Hub"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
