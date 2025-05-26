from phonemizer.backend.espeak.wrapper import EspeakWrapper
from phonemizer import phonemize  # noqa: F401
import espeakng_loader

EspeakWrapper.set_library(espeakng_loader.get_library_path())
EspeakWrapper.set_data_path(espeakng_loader.get_data_path())
