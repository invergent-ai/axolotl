"""AIM plugin for Axolotl"""

from typing import List, Callable, Dict

from axolotl.integrations.base import BasePlugin
from .args import AimInputArgs
from .callback import AimCallback


class AimPlugin(BasePlugin):

    def __init__(self):
        super().__init__()
        self.enabled = None

    def register(self, cfg: Dict):
        args = AimInputArgs(**{k: cfg.get(k) for k in AimInputArgs.model_fields})
        self.enabled = args.aim.aim_enable

    def get_input_args(self):
        return "axolotl.integrations.aim.AimInputArgs"

    def add_callbacks_pre_trainer(self, cfg, model) -> List[Callable]:
        if not getattr(self, "enabled", True):
            return []
        args = AimInputArgs(**{k: cfg.get(k) for k in AimInputArgs.model_fields})
        cb = AimCallback(
            repo=args.aim.aim_repo,
            experiment=args.aim.aim_experiment
        )
        return [cb]
