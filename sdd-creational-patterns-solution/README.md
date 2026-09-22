# Campaign Launchpad

You’re building a tiny backend service for a marketing team that launches online ad campaigns across multiple channels (e.g., Google Ads, Facebook Ads).

## Business requirements

- The company wants to keep track of the global budget when launching different campaigns.
- Marketers choose a channel and the system must create the right client to talk to that channel.
- Campaigns have many optional pieces (budget caps, audiences, creatives, tracking parameters). We need a safe way to assemble a valid campaign.

## Architecture

- **Builder**: `CampaignBuilder` assembles validated `Campaign` objects with a fluent API.
- **Singleton**: `GlobalBudget` — one shared marketing wallet for all campaigns.
- **Factory Method**: `ChannelClientFactory` creates channel-specific clients (Google, Facebook).

## Project layout

```dir_tree
root_dir
├─ campaign_launchpad/
│  ├─ __init__.py
│  ├─ budget.py
│  ├─ campaign.py
│  └─ channels.py
├─ tests/
│  ├─ test_budget.py
│  ├─ test_campaign.py
│  └─ test_channels.py
└─ README.md
```

## Setup

Preferred: [uv](https://docs.astral.sh/uv/). Install uv once per machine (see
uv's docs), then from inside the repo:

```bash
uv venv                              # create a local virtual environment (.venv)
uv pip install -r requirements.txt   # install pytest into it
```

From then on, run any Python command through `uv run` so it uses that
environment automatically:

```bash
uv run pytest -q                            # run all tests
uv run pytest ./tests/test_budget.py        # run budget tests only
uv run python -m campaign_launchpad.app     # run the demo app
```

<details>
<summary>Alternative: plain venv + pip</summary>

```bash
# Unix
python -m venv .venv && source .venv/bin/activate

# Windows:
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python -m pytest -q
python -m pytest ./tests/test_budget.py
python -m campaign_launchpad.app
```

</details>

## How to submit

1. Fork this repo to your own GitHub account. Keep the fork **public** (the
   default when forking a public repo) so it can be reviewed without needing
   collaborator access.
2. Clone your fork and work through the exercises below on a branch, e.g.:

   ```bash
   git switch -c solution
   ```

3. Commit your changes and push the branch to your fork:

   ```bash
   git push origin solution
   ```

4. Open a **pull request** from your branch into this repo's `main` branch.
5. Opening the PR automatically runs the full test suite as a GitHub Actions
   check — see the "Checks" tab on your PR. All three test files
   (`test_budget.py`, `test_campaign.py`, `test_channels.py`) must pass for
   the check to go green.
6. Submit the link to your pull request on Blackboard. This is your
   submission; the green check confirms the tests pass, but the PR itself
   (with your commits and diff) is what gets graded.

## Exercises

### 1. Implement campaign builder

Functional requirements:

- A campaign must have a name.
- A campaign must have a channel.
- The daily budget must be provided and must be positive.
- The start date is required.
- If an end date is provided, the start date must be before or equal to the end date.
- At least one creative (headline and image URL) is required.

To test this part:

```bash
uv run pytest ./tests/test_campaign.py
```

Goal --> Pass campaign tests

### 2. Implement budget

Functional requirements:

- Ensure there is only a single bugdet
- Ensure bugdet cannot go below zero
- Allow no negative allocations

To test this part:

```bash
uv run pytest ./tests/test_budget.py
```

Goal --> Pass budget tests

### 3. Implement channel client factory

Functional requirements:

- Campaigns should allocate their daily budget to the global budget.
- When a campaign is created, a external id should be returned. This id should have a prefix with the initial of the channel i.e. For facebook ads --> "f_<some_id>"
- Two clients are needed: FacebookAds and GoogleAds
- If different channel client is created, and error should arise.

To test this part:

```bash
uv run pytest ./tests/test_channels.py
```

Goal --> Pass channels tests
