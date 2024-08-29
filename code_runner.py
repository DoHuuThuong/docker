import docker

def run_code_in_docker(code, language):
    client = docker.from_env()
    image = "openjdk" if language == "Java" else "gcc"
    
    # Create a temporary directory to store the code
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        extension = "java" if language == "Java" else "c"
        file_name = f"{temp_dir}/main.{extension}"
        
        # Write the code to a file
        with open(file_name, 'w') as code_file:
            code_file.write(code)
        
        # Run the Docker container and mount the temp directory
        container = client.containers.run(
            image,
            command="sh",
            detach=True,
            stdin_open=True,
            tty=True,
            volumes={temp_dir: {'bind': '/app', 'mode': 'rw'}}
        )
        
        if language == "Java":
            compile_result = container.exec_run("javac /app/Main.java")
            if compile_result.exit_code != 0:
                
                return compile_result.output.decode()  # Return compile error
            run_result = container.exec_run("java -cp /app Main")

        else:
            compile_result = container.exec_run("gcc /app/main.c -o /app/main")
            if compile_result.exit_code != 0:
                
                return compile_result.output.decode().strip()  # Return compile error
            run_result = container.exec_run("/app/main")
        return run_result.output.decode().strip()
        container.stop()
        container.remove()
        
        return run_result.output.decode()  # Return the actual output
