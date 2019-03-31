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
    
    stage('Trigger') {
        sh("bin/trigger")
    }

    stage('Archive') {
        archiveArtifacts artifacts: "script-${BUILD_ID}-*.py", fingerprint: true   
    }
    
    cleanWs()
}
