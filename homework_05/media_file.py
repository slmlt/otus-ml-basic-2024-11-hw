import enum
from dataclasses import dataclass
from datetime import datetime


@enum.unique
class MediaType(enum.Enum):
    """
    Supported MIME types of MediaFiles
    """
    Image = "image"
    Audio = "audio"
    Video = "video"


@dataclass(frozen=True)
class MediaFormat:
    """
    MediaFile type information in MIME-like structure
    :param type one of supported media file type, see MediaType
    :param format arbitrary MediaType subtype
    """
    type: MediaType
    format: str

    def as_mime_type(self) -> str:
        return f"{self.type}/{self.format}"


@dataclass(frozen=True)
class MediaFile:
    id: str
    name: str
    uri: str
    format: str
    size_bytes: int
    type: MediaFormat
    preview_url: str
    created_at: datetime
    modified_at: datetime
    owner_id: str
    metadata: dict[str, str]
