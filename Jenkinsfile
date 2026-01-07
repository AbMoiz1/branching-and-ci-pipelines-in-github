pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                bat 'python -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest test_app.py -v'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
