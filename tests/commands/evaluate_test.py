# pylint: disable=invalid-name,no-self-use
import argparse
import json
import os

from allennlp.common.testing import AllenNlpTestCase
from allennlp.commands.evaluate import evaluate, evaluate_from_args, add_subparser
from allennlp.models import Model
from allennlp.training.metrics import BooleanAccuracy
import torch
import numpy


class TestEvaluate(AllenNlpTestCase):

    def setUp(self):
        self.old_get_metrics = Model.get_metrics

        def mock_get_metrics(self, reset: bool = False):  # pylint: disable=unused-argument
            return {"mock_accuracy": 0.75}

        Model.get_metrics = mock_get_metrics

    def tearDown(self):
        Model.get_metrics = self.old_get_metrics

    def test_evaluate_from_args(self):
        parser = argparse.ArgumentParser(description="Testing")
        subparsers = parser.add_subparsers(title='Commands', metavar='')
        add_subparser(subparsers)

        raw_args = ["evaluate",
                    "--config_file", "tests/fixtures/evaluate_srl/experiment.json",
                    "--weights_file", "tests/fixtures/evaluate_srl/best.th",
                    "--evaluation_data_file", "tests/fixtures/evaluate_srl/data"]

        args = parser.parse_args(raw_args)

        metrics = evaluate_from_args(args)

        # TODO(joelgrus) once the SRL model returns metrics, check them
        assert metrics == {"mock_accuracy": 0.75}
