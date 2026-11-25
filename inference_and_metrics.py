# inference_and_metrics.py - For each wav file in VanDam-5minutes, run inference and metrics, saving the results in appropriately named files.

from pyannote.metrics.detection import DetectionPrecisionRecallFMeasure
from pyannote.metrics.diarization import DiarizationErrorRate
from pyannote.metrics.diarization import DiarizationCoverage, DiarizationPurity
from pyannote.metrics.segmentation import SegmentationCoverage, SegmentationPurity, SegmentationPurityCoverageFMeasure
from pyannote.metrics.identification import IdentificationPrecision, IdentificationRecall
from pyannote.database.util import load_rttm
from pyannote.core import Segment, Timeline, Annotation
from pathlib import Path
import json

REF_PATH = Path("/media/joe/slepnir1/Datasets/ALSSA/VanDam-5minute/rttm")
INF_PATH = Path("/media/joe/slepnir1/Datasets/ALSSA/VanDam-5minute/VTC-inferred/rttm")
METRICS_PATH = Path("/media/joe/slepnir1/Datasets/ALSSA/VanDam-5minute/VTC-inferred/metrics")

# create metrics folder if it doesn't exists
METRICS_PATH.mkdir(parents=True, exist_ok=True)

def get_metric(metric, ref, hyp):
    metric_dict = metric.compute_components(ref, hyp)
    metric_results = metric.compute_metric(metric_dict)
    return(metric_dict, metric_results)

for ref_pth in REF_PATH.glob('**/*.rttm'):
    # get the inferred rttm
    inf_pth = INF_PATH.joinpath(ref_pth.name)
    if not inf_pth.exists():
        print(f'{ref_pth.name}')
        continue

    # get annotations
    reference = load_rttm(str(ref_pth))
    hypothesis = load_rttm(str(inf_pth))

    name = ref_pth.stem
    r = reference[name]
    h = hypothesis[name]

    print(f' processing {name}')

    # calculate the desired metrics
    metrics_dict = {name: {}}
    for m in [DiarizationErrorRate(), DiarizationCoverage(), DiarizationPurity(), SegmentationCoverage(), SegmentationPurity(), DetectionPrecisionRecallFMeasure(), SegmentationPurityCoverageFMeasure(), IdentificationPrecision(), IdentificationRecall()]:
        d, result = get_metric(m, r, h)
        metrics_dict[name][m.__class__.__name__] =  {'components':d, 'value':result}

    #print(metrics_dict)
    # create/open the output path
    metrics_pth = METRICS_PATH.joinpath(ref_pth.parents[0].parts[-1])
    metrics_pth.mkdir(parents=True, exist_ok=True)
    metrics_pth = metrics_pth.joinpath(name + '.json')

    with open(metrics_pth, "w") as fd:
        json.dump(metrics_dict, fd)






