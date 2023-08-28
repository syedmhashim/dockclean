import docker
import re


def remove_all_dangling(logger):
    logger.info("Removing all dangling images.")
    client = docker.from_env()
    images = client.images
    current_images = images.list(filters={"dangling": True})
    count = 0
    for image in current_images:
        try:
            images.remove(image.id)
            logger.debug(f"Removed image -> {image.id}")
            count += 1
        except:
            logger.error(f"Exception occurred while removing image -> {image.id}")
    logger.info(f"Total {count} dangling images removed.")


def remove_with_pattern(pattern, exclude, logger):
    logger.info(f"Removing all images with pattern -> {pattern}")
    client = docker.from_env()
    images = client.images
    current_images = images.list()
    count = 0
    for image in current_images:
        match = re.search(pattern, image.tags[0])
        if match:
            logger.debug(f"image tag {image.tags[0]}")
            if exclude:
                if re.search(exclude, image.tags[0]):
                    continue
            try:
                images.remove(image=image.id)
                logger.debug(f"Removed image -> {image.tags[0]}")
                count += 1
            except Exception as e:
                logger.error(f"Error while removing image -> {image.tags[0]}. {str(e)}")
    logger.info(f"Total {count} images, with pattern -> {pattern}, removed.")


def remove_all_from_repository(repository, exclude, logger):
    logger.info(f"Removing all images belonging to repostory, {repository}")
    client = docker.from_env()
    images = client.images
    current_images = images.list()
    pattern = f"^{repository}/.+:(.+)$"
    count = 0
    for image in current_images:
        match = re.search(pattern, image.tags[0])
        if match:
            logger.debug(f"image tag {image.tags[0]}")
            match = re.search(exclude, image.tags[0])
            if match:
                continue
            try:
                images.remove(image.attrs["Id"])
                logger.debug(f"Removed image -> {image.tags[0]}")
                count += 1
            except:
                logger.error(
                    f"Exception occurred while removing image -> {image.tags[0]}"
                )
    logger.info(f"Total {count} images belonging to repository, {repository}, removed.")
