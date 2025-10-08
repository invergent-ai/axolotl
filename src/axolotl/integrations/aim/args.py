"""Pydantic models for AIM plugin"""

from pydantic import BaseModel, Field


class AimInputConfig(BaseModel):
    aim_enable: bool = Field(
        default=True, description="Enable AIM"
    )
    aim_repo: str | None = Field(
        default=None,
        description="AIM repo",
    )
    aim_experiment: str = Field(
        default="axolotl", description="Experiment description"
    )


class AimInputArgs(BaseModel):
    aim: AimInputConfig = Field(
        default_factory=AimInputConfig,
        description="AIM configuration. Only nested block is supported.",
    )
