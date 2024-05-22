from dataclasses import dataclass
from pathlib import Path

from pheval.runners.runner import PhEvalRunner

from pheval_oak.prepare.prepare import prepare_inputs


@dataclass
class PhenologRunner(PhEvalRunner):
    input_dir: Path
    testdata_dir: Path
    tmp_dir: Path
    output_dir: Path
    config_file: Path
    version: str

    def prepare(self):
        """
        Pre-process any data and inputs necessary to run the tool.
        """
        print("preparing")
        prepare_inputs(testdata_dir=self.testdata_dir)

    def run(self):
        """
        Run the tool to produce the raw output.
        """
        # TODO implement Best Matched Average & parse phenotype-gene for ranked list of genes
        print("running with phenolog runner")

    def post_process(self):
        """
        Post-process the raw output into PhEval standardised TSV output.
        """
        # TODO post process the raw output into PhEval standardised TSV output
        print("post processing results to PhEval standardised TSV output.")
