#!/usr/bin/env python
import sys
import warnings
import datetime
from cve_review.crew import CveReview


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the CVE Review.
    """
    inputs = {
        'date': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    CveReview().crew().kickoff(inputs=inputs)
