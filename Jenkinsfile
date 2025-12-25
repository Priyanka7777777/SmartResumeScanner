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
stage('Deploy to Kubernetes (CD)') {
    steps {
        sh '''
            echo "Deploying to Kubernetes..."

            kubectl set image deployment/smartresumescanner-deployment \
              smartresumescanner=priyanka7777777/smartresumescanner:latest

            kubectl rollout status deployment/smartresumescanner-deployment
        '''
    }
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
