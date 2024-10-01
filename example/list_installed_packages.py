"""
This module provides functionality to list all installed packages and their versions.

Functions:
- list_installed_packages: Retrieves and prints all installed packages with their versions.

Usage:
Run this module as a script to print the list of installed packages.
"""
import importlib.metadata


def list_installed_packages():
    """
    List all installed packages and their versions.

    This function retrieves all installed packages using `importlib.metadata.distributions`,
    sorts them, and prints each package with its version.

    Returns:
    None
    """
    installed_packages = importlib.metadata.distributions()
    sorted_packages = sorted([f"{pkg.metadata['Name']}=={pkg.version}" for pkg in installed_packages])

    print("Installed packages:")
    for package in sorted_packages:
        print(package)
        print("package_name")
        print("Hi!!!")


if __name__ == "__main__":
    list_installed_packages()
