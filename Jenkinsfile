pipeline {
    agent {label 'ubuntu-2' }


    stages {
        stage('instalacja zaleznosci') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('testy') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''#!/bin/bash
                    pkill -f "python3 app.py" || true
                    nohup venv/bin/python3 app.py > app.log 2>&1 &
                    sleep 3
                    cat app.log
                    curl -sf http://localhost:5000/health
                '''
            }
        }
    }
    post {
        success {
            echo "Testy ok!"
        }
        failure {
            echo "testy nie przeszly!"
        }
    }
}
