# ADLS List Assignment

A Python script that connects to a public Azure Blob Storage container and lists all files ending in `.csv.gz`. A GitHub Actions workflow is included to run the script automatically in CI.

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── adls_list.yml
├── adls_practice/
│   ├── list_contents.py
│   └── requirements.txt
└── README.md
```

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r adls_practice/requirements.txt
   ```

2. Run the script:
   ```bash
   python adls_practice/list_contents.py
   ```

## Running via GitHub Actions

1. Go to the **Actions** tab in this repository.
2. Select **Run ADLS List Script** from the sidebar.
3. Click **Run workflow** to trigger it manually.
4. Open the running job to view the `.csv.gz` file names printed in the logs.

## Clarifying Questions

While completing this assignment, I identified a few areas where I would welcome clarification in a collaborative setting:

1. **File placement** — Step 2 lists the files to add without specifying their paths. I relied on the repository structure diagram at the bottom of the instructions to determine correct placement (e.g. `list_contents.py` and `requirements.txt` under `adls_practice/`). Is that the intended interpretation?

2. **Unit testing** — I noticed there is no test validating that the script does not miss any matching file names in the container. Should I include a unit test to verify the file extension matching logic?

3. **Local testing expectations** — Is local testing of the Python script expected before pushing, or should we rely directly on running the GitHub Action for validating the script output?

4. **Output format** — Should the script print the full blob path or just the leaf filename? Additionally, should I include any metadata such as a file count or file size to help verify the results?
