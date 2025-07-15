pipeline {
    agent any
    stages{
        stage('checkout'){
            steps {
                git branch: 'main', url: 'https://github.com/amiragalal98/tax-dashboard.git'

            }
        }

        stage('build docker image'){
            steps{
                sh 'docker build -t flask-matrics-app .'
            }
        }

        stage('deploy'){
            steps{
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}
