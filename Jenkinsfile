node {
    stage('Build') {
        checkout scm
        sh("ls -alh")
        sh("bin/build")
        sh("ls -alh")
    }

    stage('Push') {
        sh("bin/push")
    }
    
    stage('Archive') {
        archiveArtifacts artifacts: "script-*.py", fingerprint: true   
    }
    
    cleanWs()
}
