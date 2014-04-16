
import subprocess

# Give .java file name here
javaFileName = 'Sample'

p1 = subprocess.Popen('javac ' + javaFileName + '.java', stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
(output1, err1) = p1.communicate()

if err1 == '':

    print 'Compiled!..\n'

    p2 = subprocess.Popen('java ' + javaFileName, stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
    (output2, err2) = p2.communicate()

    if err2 == '':
        print 'Output:\n', output2
    else:
        print 'Error:\n', err2

else:
    print 'Compile time error:\n' + err1
