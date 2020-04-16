node {
	stage("Build") {
		sh 'echo "-----------------------------------------BUILD------------------------------------------"'
		checkout scm
		try{
			sh 'docker rm -f dev_my_app'
			sh 'docker rmi oriexsol/my_app:latest'
		}catch(all){
			sh 'echo "image: oriexsol/my_app:latest out"'
		}
		sh 'docker build -t oriexsol/my_app:latest .'
	}
	stage("Test") {
		sh 'echo "-----------------------------------------Test------------------------------------------"'
		sh 'docker run --name dev_my_app -p 80:80 -dit oriexsol/my_app:latest'
		
	}
}
