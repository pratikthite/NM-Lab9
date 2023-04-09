pipeline {
    agent any

    stages {
        stage('Install Packages') {
            steps {
                sh 'echo "Installing Packages"'
                sh 'pip list | grep -E "ncclient|pandas|ipaddress|netaddr|prettytable|pylint"; pip install ncclient pandas; pip install ipaddress netaddr; pip install prettytable pylint'
            }
        }
        stage('Fix Violation') {
            steps {
                sh 'echo "Checking code for violations"'
                sh '''
                if pylint netman_netconf_obj2.py | grep / | grep -o "^[^.]*" | awk -F" " \'$7 > 5\' &> /dev/null; then
                  echo "The code rate was rated above 5"
                else
                  echo "The code rate was 5 or below. Pipeline failed. Check the code to match the style-guide"
                  exit 1
                fi
                '''
            }
        }
        stage('Execute Python Script') {
            steps {
                sh '/usr/bin/python3 netman_netconf_obj2.py'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Hello Brother'
            }
        }
    }
}
