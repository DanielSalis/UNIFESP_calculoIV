## Run

`manim -p -q m test.py --format=mp4`

### Install (Manjaro)

`yay -S manim-git`

### Example

![gif_exemplo](./assets/mainClass_ManimCE_v0.17.3.gif)

## Run with docker

`https://docs.manim.community/en/stable/installation/docker.html`

```
docker run -it --name my-manim-container -v "./:/manim" manimcommunity/manim /bin/bash
/* close container
sudo docker start my-manim-container
sudo docker exec -it my-manim-container manim -qm main.py
```
