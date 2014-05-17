# this is the default target
build: clean
	python iyaccer.py
# this is the target to run the executable
run:
	javac -classpath selenium-server-standalone-2.39.0.jar Target.java
	clear
	java -cp .:selenium-server-standalone-2.39.0.jar Target
# this target will clean the directory
clean:
	rm -rf Target.class