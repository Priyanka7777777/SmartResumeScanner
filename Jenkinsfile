pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Priyanka7777777/SmartResumeScanner.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t smartresumescanner:latest .'
            }
        }

        stage('List Docker Images') {
            steps {
                sh 'docker images | grep smartresumescanner'
            }
        }
    }

    post {
        success {
            echo '✅ CI Pipeline completed successfully'
        }
        failure {
            echo '❌ CI Pipeline failed'
        }
    }
}
