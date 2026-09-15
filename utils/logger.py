import logging

def get_logger(name: str = "scanner", level: int = logging.INFO, log_file: str = None) -> logging.Logger:
    """
    Create and return a logger.

    Args:
        name (str): Logger name (default: "scanner").
        level (int): Logging level (default: INFO).
        log_file (str): Optional file path for log output.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)

    # Avoid adding handlers multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Optional file output
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        logger.setLevel(level)

    return logger


