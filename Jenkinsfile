pipeline {
	agent any
stages{
	stage('Clone repo') {
	steps {
	git 'https://github.com/Adedamola29/Devops2'
	}
}
	stage ('Run ETL Job') {
	steps{
		sh 'python3 etl.py'
	}
}
	stage('Save Output') {
	steps {
		archiveArtifacts artifacts: 'output.csv' , fingerprint: true

	}
      }
    }
}
