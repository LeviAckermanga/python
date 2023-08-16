pipeline {
    agent {
        label 'agent1'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    def mvnHome = tool name: 'Maven', type: 'hudson.tasks.Maven$MavenInstallation'
                    def pythonHome = tool name: 'Python', type: 'hudson.plugins.python.PythonInstallation'
                    
                    if (mvnHome) {
                        def mvnCmd = "${mvnHome}/bin/mvn"
                        sh "${mvnCmd} clean package"
                    } else {
                        error "Maven not configured"
                    }
                    
                    if (pythonHome) {
                        sh "${pythonHome}/bin/python -m venv venv"
                        sh "source venv/bin/activate && pip install -r requirements.txt"
                    } else {
                        error "Python not configured"
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    def pythonHome = tool name: 'Python', type: 'hudson.plugins.python.PythonInstallation'
                    
                    if (pythonHome) {
                        sh "source venv/bin/activate && python -m pytest tests"
                    } else {
                        error "Python not configured"
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                sh "nohup venv/bin/python app.py > app.log 2>&1 &"
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
