pipeline {
    agent any

    stages {

        stage('Code Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Isharohira/Lambda-API-Gateway-and-DynamoDB-AWS-Project'
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t serverless:latest ."
            }
        }

        stage('Push to Docker Hub and Deploy') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerHUbCred', passwordVariable: 'dockerhubpass', usernameVariable: 'dockerhubuser')]) {

                    sh "docker login -u $dockerhubuser -p $dockerhubpass "

                    sh "docker tag serverless:latest $dockerhubuser/serverless:v${BUILD_NUMBER}"
                    sh "docker tag serverless:latest $dockerhubuser/serverless:latest"

                    sh "docker push $dockerhubuser/serverless:v${BUILD_NUMBER}"
                    sh "docker push $dockerhubuser/serverless:latest"

                    sh "docker run -d  -p 5000:5000 $dockerhubuser/serverless:latest"

                }
            }
        }

    }
}
