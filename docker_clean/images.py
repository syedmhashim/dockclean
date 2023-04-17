import docker
import re


def remove_all_dangling(logger):
    print("Removing all dangling images.")
    client = docker.from_env()
    images = client.images
    current_images = images.list(filters={"dangling": True})
    count = 0
    for image in current_images:
        try:
            images.remove(image.id)
            logger.info(f"Removed image -> {image.id}")
            count += 1
        except:
            logger.error(f"Exception occurred while removing image -> {image.id}")
    print(f"Total {count} dangling images removed.")


def remove_with_pattern(pattern, logger):
    print(f"Removing all images with pattern -> {pattern}")
    client = docker.from_env()
    images = client.images
    current_images = images.list()
    count = 0
    for image in current_images:
        m = re.search(pattern, image.tags[0])
        if m:
            try:
                images.remove(image=image.id, force=True)
                logger.info(f"Removed image -> {image.tags[0]}")
                count += 1
            except Exception as e:
                logger.error(
                    f"Error while removing image -> {image.tags[0]}. {str(e)}"
                )
    print(f"Total {count} images, with pattern -> {pattern}, removed.")


def remove_all_intechww_images_except_with_version(version, logger):
    repository = "intechww-docker-local.jfrog.io"
    print(
        f"Removing all images belonging to repostory, {repository}, except those with version {version}"
    )
    client = docker.from_env()
    images = client.images
    current_images = images.list()
    pattern = f"^{repository}/.+:(.+)$"
    count = 0
    for image in current_images:
        m = re.search(pattern, image.tags[0])
        if m and m.group(1) != version:
            try:
                images.remove(image.attrs["Id"])
                logger.info(f"Removed image -> {image.tags[0]}")
                count += 1
            except:
                logger.error(
                    f"Exception occurred while removing image -> {image.tags[0]}"
                )
    print(f"Total {count} images belonging to repository, {repository}, removed.")
