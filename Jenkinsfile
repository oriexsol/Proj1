node {
	stage("Build") {
		sh 'echo "-----------------------------------------BUILD-----------------------------------------"'
		checkout scm
		withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			sh 'docker login -u $USERNAME -p $PASSWORD '
		}
		sh 'docker build -t oriexsol/my_app:build .'
		sh "docker tag oriexsol/my_app:build oriexsol/my_app:${BUILD_NUMBER}"
		sh 'docker push oriexsol/my_app:build'
		sh "docker push oriexsol/my_app:${BUILD_NUMBER}"
	}
	stage("Test") {
		sh 'echo "-----------------------------------------Test------------------------------------------"'
		withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			sh 'docker login -u $USERNAME -p $PASSWORD '
		}
		sh 'docker pull oriexsol/my_app:build'
		sh 'docker tag oriexsol/my_app:build oriexsol/my_app:test'
		sh 'docker push oriexsol/my_app:test'
		sh 'docker rm -f dev_my_app || true'
		sh 'docker run --name dev_my_app -p 443:80 -dit oriexsol/my_appt:test'
		sh 'chmod +x isalive.sh'
		def isalive = sh (script: "./isalive.sh", returnStdout: true)
		sh 'docker rm -f dev_my_app'
		if ("${isalive}") {
			echo "Testing completed successfully!"
			echo "$isalive"
		}
		else {
			echo "Failed The Testing"
			currentBuild.result = 'FAILURE'
		}
	}
	stage ("Deploy") {
		sh 'echo "-----------------------------------------Deploy------------------------------------------"'
		withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
			sh 'docker login -u $USERNAME -p $PASSWORD '
		}
		sh 'docker pull oriexsol/my_app:test'
		sh 'docker tag oriexsol/my_app:test oriexsol/my_app:deploy'
		sh 'docker push oriexsol/my_app:deploy'
		sh 'docker rm -f my_app_prod || true'
		sh 'docker run --name my_app_prod -p 80:80 -dit oriexsol/my_app:deploy'
	}
}
