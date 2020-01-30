pipeline {
    agent { dockerfile true }

    stages {
        stage('Build') {
            sh 'python -m compileall'
        }

        stage('Test') {
            steps {
                sh 'pytest --cov'
            }
        }
    }
}