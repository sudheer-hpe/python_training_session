# Virtual Environment Showcase

Welcome to the Virtual Environment Showcase repository! This project demonstrates the importance and utility of virtual environments in Python development.
Here, you'll find detailed instructions on how to install and set up a virtual environment, along with examples of its practical applications.

## Features

- **Virtual Environment Installation:** Step-by-step guidance on how to install and configure virtual environments for your Python projects.
- **Practical Examples:** Real-world scenarios showcasing how virtual environments can help manage project dependencies and maintain clean development environments.
- **Git Usage:** Learn how to effectively use Git for version control, including best practices for committing changes, branching, and collaborating with others.

## Getting Started

Follow the instructions in the repository to set up your own virtual environment and begin exploring its benefits.

## Creating a Virtual Environment with Poetry

Follow these steps to set up a virtual environment for your Python project using Poetry:

### Step 1: Install Poetry

If you haven't installed Poetry yet, run the following command:

```bash
python -m pip install --upgrade pip
pip install poetry
```

You can also refer to the [official installation guide](https://python-poetry.org/docs/#installation) for more options.

### Step 2: Initialize the Virtual Environment

To create and install the virtual environment, run:

```bash
poetry install
```

This command sets up the virtual environment and installs any dependencies listed in the `pyproject.toml` file.

### Step 3: Activate the Virtual Environment

Activate the virtual environment by running:

```bash
poetry shell
```

This opens a new shell with the virtual environment activated.

### Step 4: Add Dependencies

To add a dependency, use the following command:

```bash
poetry add package-name
```

Replace `package-name` with the name of the package you want to install.

### Step 5: Deactivate the Virtual Environment

When you're done, exit the virtual environment by typing:

```bash
exit
```

Happy coding!
