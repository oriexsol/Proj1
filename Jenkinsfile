node {
	stage("Build") {
		checkout scm
		try{
			sh 'docker rmi oriexsol/my_app:latest'
		}catch(all){
			sh 'echo "image: oriexsol/my_app:latest out"'
		}
		sh 'docker build -t oriexsol/my_app:latest .'
	}
}
