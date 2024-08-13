import os
import subprocess
from pathlib import Path
from packaging import version

from pheval_kghg.prepare.tool_specific_configuration_options import KgHgConfigurations


def run_kghg_local(input_dir: Path,
                   output_dir: Path,
                   tool_input_commands_path: str,
                   config: KgHgConfigurations) -> None:
    """
    Run kghg locally and write command to a file for record keeping
    """

    # Combine arguments into subprocess friendly command format
    subp_command = ["python",
                    config.path_to_kghg,
                    "rank-associations",
                    "-i", input_dir,
                    "-o", output_dir,
                    "-n", config.path_to_nodes,
                    "-e", config.path_to_edges]
    
    # Write command to file
    with open(tool_input_commands_path, 'w') as outfile:
        outfile.write(' '.join([str(v) for v in subp_command])) # Must convert Path objects to strings

    # Run kghg through subprocss
    subprocess.run(subp_command, shell=False)
