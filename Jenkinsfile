pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Mikorolo/testJenkins.git'
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }
    }
}
