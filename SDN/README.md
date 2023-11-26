# Installing mininet-wifi

1. Build the image:

    ```sh
    docker build -t mn-wifi:v1 .
    ```
2. Running the container: Mininet-WiFi relies on Kernel modules from the host, requires elevated privilege, and the host network interface:
   ```sh
   make create-mininet-wifi-container
   ```

# Running mininet-wifi

- To run the container:
    ```sh
    make run-mininet-wifi:
    ```
- If you want to run `miniedit.py` inside the container you need to allow the docker user to use the x11 socket before running the container:
    ```sh
    make add-docker-to-x11-socket
    ```

    <br>

    > The extension `devcontainer` will make your life a bit less painful !

