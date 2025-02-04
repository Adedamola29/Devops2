pipeline {
	agent any
stages{
	stage('Clone repo') {
	steps {
	git 'https://github.com/Adedamola29/Devops2'
	}
}
	stage ('Run ETL Job') {
	steps {
		archiveArtifacts artifacts: 'output.csv' , fingerprint: true
}
}
}
}
