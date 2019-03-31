node {
    stage('Build') {
        checkout scm
        sh("ls -alh")
        sh("bin/build")
    }

    stage('Push') {
        sh("bin/push")
    }
    
    cleanWs()
}
