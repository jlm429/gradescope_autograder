# Manual Docker Build for Custom Environments on Gradescope

1.**Clone the Repository:**

    ```
    git clone https://github.com/jlm429/gradescope_autograder
    ```

2.**Customize the Docker Environment:**
- Select a base image:  See [Gradescope Docker Hub repository](https://hub.docker.com/r/gradescope/autograder-base).
- Modify Dockerfile or setup.sh: Customize the environment by editing the Dockerfile or the setup.sh script.
  - Example: 
    - In the Dockerfile: Add commands to update the package list and install necessary packages.
    
          ```
          RUN apt-get update && \
              apt-get install -yq --no-install-recommends \
              python3-pip \
              && apt-get clean
          ```

    - In setup.sh: Add commands to upgrade pip and install required Python packages.

          ```
          #!/usr/bin/env bash
          pip install --no-cache-dir --upgrade pip 
          pip install --no-cache-dir torch
          pip install -r /autograder/source/requirements.txt
          ```

3.**Change to the Docker Directory and Build the Image:**

    ```
    cd gradescope_autograder/docker
    docker build -t username/image_name:tag .
    ```

4.**Push the Image to DockerHub:**

    ```
    docker push username/image_name:tag 
    ```

5.**Use the Image on Gradescope:**
- Pull the Docker image on Gradescope by entering the DockerHub username/image_name:tag.
- Submit `example_submit.py` for testing.

6.**Optional: Test the Build Locally:**

    ```
    docker run --rm -v /path/to/submission:/autograder/submission -v /path/to/results:/autograder/results username/image_name:tag /autograder/run_autograder && cat /path/to/results/results.json
    ```

For more detailed instructions, refer to the [Gradescope Autograders Documentation](https://gradescope-autograders.readthedocs.io/en/latest/manual_docker/).
