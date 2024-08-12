pipeline {
    agent any
        
    // Pipeline stages
    stages {
            
        // Stage One: Getting code from the GIT repository
        stage('Checkout') {
            steps {
                // Use GIT to clone the repository
                git branch: 'ci-setup', url: 'https://github.com/YanaDevOps/Python_project_1'
            }
        }
        
        // Checkout Dockerfile and other resources from main branch
        stage('Checkout main branch') {
            steps {
                git branch: 'main', url: 'https://github.com/YanaDevOps/Python_project_1'
            }
        }

        // Stage two: Project assembly
        stage('Build') {
            steps {
                // The command to build the project.
                sh 'echo "Build step: No build required for this project."'
            }
        }
            
        // Stage three: Docker build
        stage('Docker build') {
            steps {
                // Build a Docker image with the tag using the Dockerfile from the repository
                sh 'docker build -t yanixdo/python_project_1 .'
            }
        }
            
        // Stage Four: Publish the Docker image to Docker Hub
        stage('Docker Push') {
            steps {
                script {
                    // Use withCredentials to get the saved variables
                    withCredentials([usernamePassword(credentialsId: '8c33c3c8-12a6-43b7-9aeb-0df7a56952ac', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                    
                    // Login to Docker Hub
                    def login = sh(script: 'echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_USERNAME" --password-stdin', returnStatus: true)
                    
                    // Check if the login was successful
                    if (login == 0) {
                        echo 'Login to Docker Hub succeeded'
                        
                        // Пушим образ в Docker Hub
                        sh 'docker push yanixdo/python_project_1:latest'
                    } else {
                        error('Login to Docker Hub failed')
                    }
                }
            }
        }
    }
            
    // Stage five: Deploy to the server (if necessary)
    stage('Deploy') {
        steps {
            // Here you can add an upload to the server
            sh 'echo "Deploy step: Deployment not implemented."'
        }
    }
}
        
    // After pipeline work ended
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
            
        failure {
            echo 'Pipeline failed.'
        }
    }
}
