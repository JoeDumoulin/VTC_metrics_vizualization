## VTC Metrics from VanDam-5-minutes

### Usage

#### 01 - Setup

Prepare VanDam-5-minutes dataset for evaluation:

1. Download the .cha and .wav files from VanDam-5-minutes repo on Homebank
2. Convert .cha files to rttm files for `reference` values, maintaining the names of the files so that they match the names of the .wav files.

Run VTC

3. download and run inference using VTC-2.  This easiest way to accomplish this is using the accompanying Dockerfile to create an image and run inference.  See the accompanying docker/Docker-Readme.md. The output directory of this process contains the `hypothesis` rttms.
4. Initialize uv in the directory by running `uv sync`.

#### 02 - Run Metrics

1. Edit the inference_and_metrics script, indicating the `reference` and `hypothesis` directories, as well as the output location for the metrics file, by changing the values in the script.  
2. Run the script:

```
uv run python inference_and_metrics.py

```

This script will run a sequence of metrics from `pyannote_metrics`.  You can check out the documentation of `pyannote_metrics` to see the reasoning and implementation details of each metric.

#### Visualize the Results

1. start a `jupyter notebook` session:

```
uv run jupyter notebook

```

2. In the notebook, navigate to `notebooks/vizualize VTC metrics`
3. Data from the last run is saved and you will see it in the notebook.  To load your new inferences, change the value of `METRICS_PATH` to point to the metrics file you generated in the steps above.

