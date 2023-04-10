pipeline {
    agent any

    stages {
        stage('Install Packages') {
            steps {
                sh 'echo "Installing Package"'
                sh '''
                python3 -m pip install --upgrade pip
                python3 -m pip install ncclient
                python3 -m pip install pandas
                python3 -m pip install ipaddress
                python3 -m pip install netaddr
                python3 -m pip install prettytable
                python3 -m pip install pylint
                pip3 install netmiko==3.0.0
                '''
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
                sh 'python3 netman_netconf_obj2.py'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'python3 stg4_unit.py'
            }
        }
    }
}
