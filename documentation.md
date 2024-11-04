# Table of Contents
1. [Overview](#overview)
2. [Setup](#setup)
3. [Dependencies](#dependencies)
4. [Code Structure](#code-structure)
5. [API Documentation](#api-documentation)
6. [Usage Examples](#usage-examples)
7. [Error and Debugging Guidance](#error-and-debugging-guidance)
8. [Searchable and Accessible](#searchable-and-accessible)
9. [Consistent Style and Formatting](#consistent-style-and-formatting)
10. [Assumptions and Prerequisites](#assumptions-and-prerequisites)
11. [Maintenance Tips and Code Style](#maintenance-tips-and-code-style)
12. [Open to Contributions](#open-to-contributions)

## Overview

This codebase is designed to generate professional-looking documentation for a given codebase using markdown conventions.

## Setup

To set up the project, run the following command:
```bash
pip install -r requirements.txt
```
This will install all the necessary dependencies.

## Dependencies

The project depends on the following libraries:

* `setuptools`
* `yaspin`
* `click`
* `groq`
* `openai`

## Code Structure

The code is organized into the following modules:

* `file_processing`: contains functions for processing files and directories
* `ai_assistant`: contains classes and functions for interacting with the AI assistant
* `consts`: contains constants used throughout the codebase
* `llm_cli`: contains functions for interacting with the LLM CLI
* `prompt_llm`: contains classes and functions for prompting the LLM

## API Documentation

### file_processing

* `process_file(file_path)`: reads the content of a file and returns it as a string
* `create_markdown_file(filepath, content)`: creates a markdown file with the given content
* `process_directory(directory)`: walks through the directory and reads each file's content into a string

### ai_assistant

* `AIAssistant(cli)`: initializes the AI assistant with the given CLI
* `run_assistant(prompt, command)`: runs the AI assistant with the given prompt and command

### consts

* `UserRole`: an enum representing the user role
* `AIModel`: an enum representing the AI model
* `COMMANDS`: a dictionary of commands and their corresponding prompts

### llm_cli

* `PromptLlm(llm_options)`: initializes the LLM prompt with the given options
* `prompt(cli)`: prompts the LLM with the given CLI

## Usage Examples

To use the code, simply run the following command:
```bash
python write_doc.py /path/to/directory
```
This will generate documentation for the given directory.

## Error and Debugging Guidance

* If an error occurs while processing a file, the error message will be printed to the console.
* If an error occurs while interacting with the AI assistant, the error message will be printed to the console.

## Searchable and Accessible

The documentation is designed to be searchable and accessible.

## Consistent Style and Formatting

The code follows a consistent style and formatting throughout.

## Assumptions and Prerequisites

* The user has Python installed on their system.
* The user has the necessary dependencies installed.

## Maintenance Tips and Code Style

* The code is designed to be maintainable and follows best practices.
* The code is formatted using a consistent style throughout.

## Open to Contributions

The project is open to contributions. If you would like to contribute, please submit a pull request.