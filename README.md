# Docklean

Docker is commonly used for packaging and shipping softwares. Developers who use docker frequently, often face the issue of disk running low due to docker taking up a lot of space in the shape of docker images, containers, volumes etc.

This utility was created to help developers clean up docker resources that are no longer required. Currently, only images and containers are supported.

## Installation

Install the utility by running the following command:

```sh
pip3 install dockclean
```

## Usage

```sh
> dockclean --help
Usage: dockclean [OPTIONS] COMMAND [ARGS]...

  This tool provides commands to remove unwanted docker images and
  containers

Options:
  --help  Show this message and exit.

Commands:
  containers  Removes unwanted containers.
  images      Removes unwanted images.
```

You can view the usage of the subcommands by simply adding the `--help` flag.

## Images

The `images` subcommand by default only removes the dangling images.

```sh
dockclean images
```

### Remove all images matching a given regex pattern

The following command removes all the the images which have names starting with `python`:

```sh
dockclean images --pattern "^python.*"
```

### Remove all images belonging to a given repository

The following command removes all the images belonging to the repository `amazon`:

```sh
dockclean images --repository "amazon"
```

>Note: repository here represents the text before the first `/` in the image name. For e.g for image `amazon/aws-cli:2.9.17`, the repository is `amazon`.

### Exclude images from being removed

To exclude images to be removed, simply use the `--exclude` or `-e` flag. The `--exclude` similar to `--pattern` flag expects a regex pattern. Any image matching this pattern won't be deleted.

```sh
dockclean images --pattern "^python.*" --exclude ".*3.10-slim.*"
```

The above command would remove all the images with name starting with `python` except for those who have `3.10-slim` text in them.

## Containers

The `containers` subcommand by default removes only stopped/exited containers.

```sh
dockclean containers
```

### Remove all containers

The following command remove all containers whether running or stopped:

```sh
dockclean containers --remove_all
```

## Local Development

For running the project locally, it is recommended to create a python virtual environment first:

1. Ensure that the following are installed:

    a. python3 (Installed based on your distro)

    b. pip3 (`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py`)

    c. virtualenv

2. Open up a terminal

3. Create a directory somewhere `mkdir dockclean-env` and `cd` into it

4. Create a python virtual environment `python3 -m virtualenv .`

5. Activate the virtual environment `source bin/activate`

6. Navigate to the projects root directory where `setup.py` file is located

Now install and run dockclean:

1. Do a `pip install .`.

2. Run the `dockclean`.

## Contributing

I've just started out with this project and there is a lot to be added. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Please support the project by giving it a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request