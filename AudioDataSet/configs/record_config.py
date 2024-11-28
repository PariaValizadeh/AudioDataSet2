from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RecorderConfig:
    """
    Configuration for the AudioRecorder.

    Attributes:
        output_dir (str): Directory to save the recorded files.
        duration (int): Duration of the recording in seconds.
        sample_rate (int): Sampling rate in Hz.
        channels (int): Number of audio input channels.
        device (Optional[int]): Device ID or name. Defaults to None for the default device.
        gain (float): Gain factor to apply to each channel.
    """
    output_dir: str = "recordings"
    duration: int = 5
    sample_rate: int = 48000
    channels: int = 8
    device: Optional[int] = None
    gain: float = 1.0


@dataclass
class ExperimentConfig:
    """
    Configuration for the overall experiment.

    Attributes:
        recorder (RecorderConfig): Configuration for the audio recorder.
        dataset_dir (Optional[str]): Directory for storing or loading datasets.
    """
    recorder: RecorderConfig = field(default_factory=RecorderConfig)
    dataset_dir: Optional[str] = None


@dataclass
class HardwareConfig:
    """
    Dynamic configuration based on a provided dictionary.

    This class initializes attributes based on key-value pairs from a dictionary.

    Attributes:
        Dynamic attributes set from the provided configuration dictionary.
    """
    def __init__(self, config_dict: dict):
        for key, value in config_dict.items():
            setattr(self, key, value)
