# Challenges

## First

1. Start the mininet-wifi docker image;
2. Use the `devcontainer` extension on vscode if you want;
3. Move the code in [/socks/](/tarc/socks) to the docker container;
4. Start the controller in [atv_01.py](/tarc/atv_01.py) (default running o port 6969);
5. Now run for both nodes: `xterm h1` and `xterm h2`
6. On `h1` run: `python /socks/server.py`
7. And on `h2`: run `python /socks/client.py`

## Second

You need to run ryu as: `ryu-manager --observe-links`
