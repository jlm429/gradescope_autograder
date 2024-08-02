# Manual Docker Build for Custom Environments on Gradescope

1.**Clone the Repository:**
    ```sh
    git clone https://github.com/jlm429/gradescope_autograder
    ```

2.**Select a [base image](https://hub.docker.com/r/gradescope/autograder-base) and modify the Dockerfile or setup.sh to customize the environment**

(Examples)

3.**Change to the Docker Directory and Build the Image:**
    ```sh
    cd gradescope_autograder/docker
    docker build -t username/image_name:tag .
    ```

4.**Push the Image to DockerHub:**
    ```sh
    docker push username/image_name:tag 
    ```

5.**Use the Image on Gradescope:**
    - Pull the Docker image on Gradescope.
    - Submit `example_submit.py` for testing.

6.**Optional: Test the Build Locally:**
    ```sh
    docker run --rm -v /path/to/submission:/autograder/submission -v /path/to/results:/autograder/results username/image_name:tag /autograder/run_autograder && cat /path/to/results/results.json
    ```

For more detailed instructions, refer to the [Gradescope Autograders Documentation](https://gradescope-autograders.readthedocs.io/en/latest/manual_docker/).
